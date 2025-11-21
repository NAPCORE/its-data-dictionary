import os
import re
from pathlib import Path

# === CONFIG ===
SOURCE_FOLDER = "../source"
SOURCE_FILES = sorted(Path(SOURCE_FOLDER).glob("*.md"))
MAX_FILENAME_LENGTH = 128  # or 100 to be extra safe
MAX_SUBCATEGORY_WORDS = 3
MAX_LABEL_WORDS = 4


# === PATTERNS ===
category_pattern = re.compile(r"^###\s+(.*)")
item_pattern = re.compile(r"\*\*(.+?)\*\*\s*:?\s*(.*)")
code_block_pattern = re.compile(r"```(\w+)?\n(.*?)```", re.DOTALL)

generated_ids = {}

# === NORMALIZATION FUNCTION ===
def normalize_item_metadata(label_raw, generated_ids):
    import re

    label_raw = label_raw.replace('–', '-').replace('—', '-').replace('/', '_').rstrip(':')

    # Split by dash only if present
    if '-' in label_raw:
        parts = [p.strip() for p in label_raw.split('-') if p.strip()]
    else:
        parts = []

    if len(parts) >= 2:
        subcategories = parts[:-1]
        label_clean = parts[-1]
        first_subcategory = parts[0]
    else:
        subcategories = []
        label_clean = label_raw.strip()
        first_subcategory = None

    # Strip markdown tokens
    label_clean = re.sub(r'^[_*]+|[_*]+$', '', label_clean)

    # Remove parenthetical content
    def strip_parens(text):
        return re.sub(r'\s*\(.*?\)', '', text).strip()

    # Extract edges with ".." if words are trimmed
    def extract_edges(text, keep=2):
        words = re.sub(r'\s+', ' ', text).split()
        return words if len(words) <= keep * 2 else words[:keep] + ['..'] + words[-keep:]

    sub_id_raw = strip_parens(first_subcategory or "")
    label_id_raw = strip_parens(label_clean)

    sub_words = extract_edges(sub_id_raw)
    label_words = extract_edges(label_id_raw)

    sub_id = '-'.join(sub_words)
    label_id = '-'.join(label_words)

    # Construct base_id depending on presence of subcategory
    base_id = f"{sub_id}_{label_id}" if first_subcategory else label_id
    base_id = base_id.lower()
    base_id = re.sub(r'[^\w\s-]', '', base_id)
    base_id = re.sub(r'\s+', '-', base_id).strip('-')

    # Uniqueness handling
    if base_id in generated_ids:
        count = generated_ids[base_id] + 1
        unique_id = f"{base_id}_{count}"
        generated_ids[base_id] = count
    else:
        unique_id = base_id
        generated_ids[base_id] = 1

    return {
        "id": unique_id,
        "label": label_clean,
        "subcategory": [first_subcategory] if first_subcategory else []
    }

# === PROCESS BUFFER ===
def process_buffer(buffer, category, source_name, target_dir, code_dir):
    i = 0
    while i < len(buffer):
        line = buffer[i]
        item_match = item_pattern.match(line)
        if item_match:
            label_raw = item_match.group(1).strip()
            definition = item_match.group(2).strip()

            meta = normalize_item_metadata(label_raw, generated_ids)
            item_id = meta["id"]
            label_clean = meta["label"]
            subcategory = meta["subcategory"]

            body_lines = []
            skip_lines = {
                f"**{label_raw}**".strip(),
                definition.strip()
            }
            i += 1
            while i < len(buffer) and not item_pattern.match(buffer[i]) and not category_pattern.match(buffer[i]):
                line_clean = buffer[i].strip()
                if line_clean not in skip_lines:
                    body_lines.append(buffer[i])
                i += 1

            body = "\n".join(body_lines)

            code_md = ""
            code_blocks = code_block_pattern.findall(body)
            for j, (lang, code) in enumerate(code_blocks):
                lang = lang if lang else "txt"
                filename = f"{item_id}_snippet_{j+1}.{lang}"
                code_path = code_dir / filename
                with open(code_path, "w", encoding="utf-8") as cf:
                    cf.write(code.strip())
                code_md += f"\n[View Code Sample](../../code/{source_name}/{filename})\n"

            definition_clean = code_block_pattern.sub("", definition).strip()

            frontmatter_lines = [
                "---",
                f"id: {item_id}",
                f"label: {label_clean}",
                f"definition: {definition_clean}",
                f"category: {category}",
                "language: en",
                "status: approved",
                f"source: {source_name}"
            ]

            if subcategory:  # ✅ subcategory is now a list
                frontmatter_lines.append("subcategory:")
                for sub in subcategory:
                    frontmatter_lines.append(f"  - {sub}")

            frontmatter_lines.append("---")
            frontmatter = "\n".join(frontmatter_lines)

            draft_md = f"{frontmatter}\n\n{body}\n{code_md}"
            file_path = target_dir / f"{item_id}.md"
            with open(file_path, "w", encoding="utf-8") as out:
                out.write(draft_md)
            print(f"✅ Created: {source_name}/{item_id}.md")
        else:
            i += 1

# === MAIN LOOP ===
for source_file in SOURCE_FILES:
    source_name = source_file.stem.replace(" ", "_").replace("(", "").replace(")", "")
    target_dir = Path(f"../drafts/{source_name}")
    code_dir = Path(f"../code/{source_name}")
    os.makedirs(target_dir, exist_ok=True)
    os.makedirs(code_dir, exist_ok=True)

    print(f"\n📄 Processing: {source_file.name}")
    current_category = "Uncategorized"
    buffer = []

    with open(source_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if category_pattern.match(line):
                if buffer:
                    process_buffer(buffer, current_category, source_name, target_dir, code_dir)
                    buffer = []
                current_category = category_pattern.match(line).group(1).strip()
            else:
                buffer.append(line)

    if buffer:
        process_buffer(buffer, current_category, source_name, target_dir, code_dir)