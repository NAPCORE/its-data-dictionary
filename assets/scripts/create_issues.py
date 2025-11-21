import os
from pathlib import Path
import yaml
from github import Github, Auth

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DRAFT_ROOT = BASE_DIR / "drafts"
PREVIEW_DIR = BASE_DIR / "drafts/preview"
INDEX_FILE = DRAFT_ROOT / "INDEX.md"

folder_mapping = {
    "DR_EU_2015-962": {"abbr": "RTTI", "emoji": "🚙", "title": "Real-Time Traffic Information (DR 2015/962)"},
    "DR_EU_2022-670": {"abbr": "RTTI2", "emoji": "🚙", "title": "Real-Time Traffic Information (DR 2022/670)"},
    "DR_EU_886-2013": {"abbr": "SRTI", "emoji": "🛑", "title": "Safety-Related Traffic Information (DR 886/2013)"},
    "DR_EU_2024-490": {"abbr": "MMTIS", "emoji": "🧭", "title": "Multimodal Travel Information Services (DR 2024/490)"},
    "DR_EU_885-2013": {"abbr": "SSTP", "emoji": "🏁", "title": "Safe and Secure Truck Parking (DR 885/2013)"},
}

def extract_content(md_text):

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

    return meta, content

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

def create_issue(repo, md_file):

    with open(md_file, "r", encoding="utf-8") as f:
        raw = f.read()
    
    meta, body = extract_content(raw)    
    
    source = meta.get("source", "").strip()
    label =  meta.get("label", "").strip()
    status = meta.get("status", "unclassified").strip()
    
    if status == "archived":
        print(f"Issue not created: data item [{label}] is archived")
        return 0
    
    info = folder_mapping.get(source)

    if info:
        title = f"{info['emoji']} {info['abbr']}: {label}"
    else:
        title = f"📄 term: {md_file.name}"
 
    body = f"{raw.rstrip()}\n\n📄 **File Reference:** [{md_file.name}](https://github.com/{repo.full_name}/blob/main/drafts/{source}/{md_file.name})"

    labels = [source, "term"]
    issue = repo.create_issue(title=title, body=body, labels=labels)
    print(f"Issue created: {issue.title}")
    
    return 1

def main():
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise RuntimeError("Set GITHUB_TOKEN environment variable")

    repo_name = "NAPCORE/its-data-dictionary"
    gh = Github(auth=Auth.Token(token))
    repo = gh.get_repo(repo_name)

    count = 0
    
    for dr_folder in DRAFT_ROOT.iterdir():
        if dr_folder.is_dir() and dr_folder.name.startswith("DR"):
            for md_file in dr_folder.glob("*.md"):
                val = create_issue(repo, md_file)
                count += val

if __name__ == "__main__":
    main()