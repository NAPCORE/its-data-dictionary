import os
import yaml
from pathlib import Path
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import SKOS, RDF
from datetime import datetime
from collections import defaultdict
import re

DR_TITLES = {
    "DR_EU_886-2013": "SRTI - Safety-Related Traffic Information",
    "DR_EU_2024-490": "MMTIS - Multimodal Travel Information Services",
    "DR_EU_2015-962": "RTTI - Real-Time Traffic Information",
    "DR_EU_2022-670": "RTTI - Real-Time Traffic Information",  
    "DR_EU_885-2013": "SSTP - Safe and Secure Truck Parking"
}

BADGES = {
    "proposed": "![Status](https://img.shields.io/badge/status-proposed-ff9800)",         # Warm orange for a work-in-progress
    "under review": "![Status](https://img.shields.io/badge/status-under_review-ffc107)", # Amber/gold to indicate scrutiny
    "revised": "![Status](https://img.shields.io/badge/status-revised-673ab7)",   # Deep violet, bold for attention
    "accepted": "![Status](https://img.shields.io/badge/status-accepted-2196f3)", # Classic blue for trust & clarity
    "validated": "![Status](https://img.shields.io/badge/status-validated-4caf50)",   # Deep green for confirmation
    "archived": "![Status](https://img.shields.io/badge/status-archived-bdbdbd)",# Medium grey for obsolescence
    "unclassified": "![Status](https://img.shields.io/badge/status-unclassified-9e9e9e)"       # Neutral grey for ambiguity
}

BASE_DIR = Path(__file__).resolve().parent.parent
DRAFT_ROOT = BASE_DIR / "drafts"
RELEASE_DIR = BASE_DIR / "release"
VOCAB_DIR = BASE_DIR / "vocab"

VERSION_TAG = os.getenv("VERSION_TAG")

EX = Namespace("http://example.org/dictionary#")

def escape_yaml_value(value):
    if not isinstance(value, str):
        return value
    risky_chars = ['<', '>', '[', ']', '(', ')', ':']
    if any(c in value for c in risky_chars) and not value.startswith('"'):
        value = value.replace('"', '\\"')
        return f'"{value}"'
    return value

def escape_yaml_block(yaml_text):
    lines = yaml_text.splitlines()
    fixed_lines = []
    for line in lines:
        if ':' in line and not line.strip().startswith('#'):
            parts = line.split(":", 1)
            key = parts[0].strip()
            value = parts[1].strip()
            if value and not value.lower() in ['true', 'false'] and not value.replace('.', '', 1).isdigit():
                value = escape_yaml_value(value)
            fixed_lines.append(f"{key}: {value}")
        else:
            fixed_lines.append(line)
    return '\n'.join(fixed_lines)

def extract_content(md_text):

    def adjust_relative_links(text):
        # Replace "../../media/" with "../images/"
        text = re.sub(r'\(\.\./\.\./(images/.*?)\)', r'(../\1)', text)
        text = re.sub(r'\(\.\./\.\./(code/.*?)\)', r'(../\1)', text)
        return text

    parts = md_text.split('---')
    if len(parts) < 3:
        return None, md_text

    raw_yaml = escape_yaml_block(parts[1])
    try:
        meta = yaml.safe_load(raw_yaml)
    except yaml.YAMLError as e:
        print(f"⚠️ YAML error: {e}")
        return None, md_text

    content = '---'.join(parts[2:]).strip()
    content = adjust_relative_links(content)

    return meta, content

def generate_rdf(meta):
    g = Graph()
    term = EX[meta['id']]
    lang = meta.get('language', 'en')
    g.add((term, RDF.type, SKOS.Concept))
    g.add((term, SKOS.prefLabel, Literal(meta['label'], lang=lang)))
    g.add((term, SKOS.definition, Literal(meta['definition'], lang=lang)))
    if 'related' in meta:
        g.add((term, SKOS.related, EX[meta['related']]))
    return g

def format_entry(meta, content, heading_level=3):
    # header = f"{'#' * heading_level} {meta.get('label', 'Untitled')}\n\n"
    header = f"{'#' * heading_level} {meta.get('label', 'Untitled')} {BADGES.get(meta.get('status', 'unknown').strip(), 'unknown')}\n\n"
    definition_text = meta.get("definition") or ""
    definition = f"**Definition**: {definition_text.strip()}"

    body = content.strip() if content and content.strip() else None

    if body:
        return f"{header}{definition}\n\n{body}\n\n---\n"
    else:
        return f"{header}{definition}\n\n---\n"

def process_dr_folder(dr_folder):
  
    release_file = RELEASE_DIR / f"{dr_folder.name}.md"
    vocab_path = VOCAB_DIR / dr_folder.name
    os.makedirs(vocab_path, exist_ok=True)

    grouped_entries = defaultdict(list)  # {combined_heading: [(label, meta, content)]}

    for md_file in dr_folder.glob("*.md"):
        with open(md_file, "r", encoding="utf-8") as f:
            raw = f.read()

        meta, body = extract_content(raw)
        if not meta: #or meta.get("status") != "validated"
            print(f"⏩ Skipping {md_file.name} in {dr_folder.name} ... missing metadata") #or not validated
            continue

        category = meta.get("category", "uncategorised").strip()
        raw_subcategory = meta.get("subcategory", [])
        subcategory = [str(item).strip() for item in raw_subcategory] if isinstance(raw_subcategory, list) else [str(raw_subcategory).strip()]
        label = meta.get("label", "").strip()
        
        heading = category
        if subcategory and any(subcategory):
            heading += " – " + " – ".join(subcategory)

        grouped_entries[heading].append((label.lower(), meta, body))

    if grouped_entries:
        title = DR_TITLES.get(dr_folder.name, dr_folder.name)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        combined = f"# Release: {title} ({dr_folder.name})\n\n"
        combined += f"![Version](https://img.shields.io/badge/semantic--dictionary-{VERSION_TAG}-orange?logo=github)\n\n"
        combined += f"**Generated on:** {timestamp}\n\n"

        for heading in sorted(grouped_entries.keys(), key=str.lower):
            combined += f"## {heading}\n\n"
            for _, meta, body in sorted(grouped_entries[heading], key=lambda x: x[0]):
                combined += format_entry(meta, body, heading_level=3)

        with open(release_file, "w", encoding="utf-8") as out:
            out.write(combined)
        print(f"✅ Release generated: {release_file.name}")
        
        for heading in sorted(grouped_entries.keys(), key=str.lower):
            for _, meta, body in sorted(grouped_entries[heading], key=lambda x: x[0]):
                rdf_graph = generate_rdf(meta)
                rdf_graph.serialize(destination=vocab_path / f"{meta['id']}.ttl", format="turtle")
                print(f"✅ Released {meta['id']} in {vocab_path}")
    else:
        print(f"⚠️ No approved items found in {dr_folder.name}")

def main():
    os.makedirs(RELEASE_DIR, exist_ok=True)
    os.makedirs(VOCAB_DIR, exist_ok=True)

    for dr_folder in DRAFT_ROOT.iterdir():
        if dr_folder.is_dir():
            process_dr_folder(dr_folder)

    print("\n🎉 All DR vocabularies released!")

if __name__ == "__main__":
    main()