import os
from github import Github, Auth

def beautify_filename(filename: str) -> str:
    name = os.path.splitext(filename)[0]
    name = name.replace("-", " ").replace("  "," ").replace("_", " - ")
    return name

folder_mapping = {
    "DR_EU_2015-962": {"abbr": "RTTI", "emoji": "🚙", "title": "Real-Time Traffic Information (DR 2015/962)"},
    "DR_EU_2022-670": {"abbr": "RTTI", "emoji": "🚙", "title": "Real-Time Traffic Information (DR 2022/670)"},
    "DR_EU_886-2013": {"abbr": "SRTI", "emoji": "🛑", "title": "Safety-Related Traffic Information (DR 886/2013)"},
    "DR_EU_2024-490": {"abbr": "MMTIS", "emoji": "🧭", "title": "Multimodal Travel Information Services (DR 2024/490)"},
    "DR_EU_885-2013": {"abbr": "SSTP", "emoji": "🏁", "title": "Safe and Secure Truck Parking (DR 885/2013)"},
}

def create_issue_from_file(repo, file_path, subdir):
    filename = os.path.basename(file_path)
    folder_info = folder_mapping.get(subdir)

    if folder_info:
        title = f"{folder_info['emoji']} {folder_info['abbr']}: {beautify_filename(filename)}"
    else:
        title = f"📄 term: {beautify_filename(filename)}"

    with open(file_path, "r", encoding="utf-8") as f:
        body_content = f.read()

    body = f"{body_content.rstrip()}\n\n📄 **File Reference:** [{filename}](https://github.com/{repo.full_name}/blob/main/drafts/{subdir}/{filename})"

    labels = [subdir, "term"]
    issue = repo.create_issue(title=title, body=body, labels=labels)
    print(f"Issue created: {issue.title}")

def main():
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise RuntimeError("Set GITHUB_TOKEN environment variable")

    repo_name = "burespe1/semantic-dictionary"  # e.g. burespe1/semantic-dictionary
    gh = Github(auth=Auth.Token(token))
    repo = gh.get_repo(repo_name)

    base_dir = os.path.join(os.path.dirname(__file__), "..", "drafts")

    count = 0
    for subdir, _, files in os.walk(base_dir):
        rel_subdir = os.path.basename(subdir)

        # Skip the top-level drafts folder itself
        if rel_subdir == "drafts":
            continue

        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(subdir, file)
                create_issue_from_file(repo, file_path, rel_subdir)
                count += 1
                if count >= 5:   # limit for test run
                    return

if __name__ == "__main__":
    main()