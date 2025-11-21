# Scripts Folder ⚙️

Python scripts for generating previews and releases.

- 🧪 `generate_preview.py`: scans all Markdown files in drafts/, reads their frontmatter and notes, and outputs into `preview` folder merged per delegated regulation for preview and index file with list of all data types with their statuses.
- 🚀 `generate_release.py`: scans all Markdown files in drafts/, reads their frontmatter and notes, and outputs into `reease` folder merged per delegated regulation as a versioned artefact.

to locally run:
- Make sure `uv` is installed:

```bash
pip install uv
```

- go to the repository (where is pyproject.toml located)

```bash
cd /path/to/the/project
```

- Create a virtual environment and sync dependencies
```bash
uv venv
uv sync
```

- Activate the environment manually
  - On macOS/Linux:
```bash
source .venv/bin/activate
```
- On Windows:
```bash
.venv\Scripts\activate
```