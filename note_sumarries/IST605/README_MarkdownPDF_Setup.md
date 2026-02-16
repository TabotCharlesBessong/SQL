# Markdown PDF: Show Details/Answers in Export

This folder contains a custom CSS file that forces `<details>` and `<summary>` content to be visible when exporting Markdown to PDF with the **Markdown PDF** extension.

## Setup (Option 2: Custom CSS)

### 1. CSS file

The file `markdown-pdf-style.css` is already in this folder.

### 2. Configure Markdown PDF extension

**A. User settings (affects all workspaces)**

1. Open VS Code Settings: `Ctrl+,` (or `Cmd+,` on Mac).
2. Search for `markdown-pdf.styles`.
3. Click "Add Item" and enter the path to the CSS file.

**Or** edit `settings.json` directly:

1. Open Command Palette: `Ctrl+Shift+P` → type "Preferences: Open User Settings (JSON)".
2. Add or update the `markdown-pdf.styles` array:

```json
"markdown-pdf.styles": [
  "d:\\charlesDevelopment\\SQL\\note_sumarries\\IST605\\markdown-pdf-style.css"
]
```

On Windows, use double backslashes `\\` in the path.

**B. Workspace settings (only this project)**

1. Create or open `.vscode/settings.json` in your project root.
2. Add:

```json
{
  "markdown-pdf.styles": [
    "note_sumarries/IST605/markdown-pdf-style.css"
  ]
}
```

The path is relative to your workspace root (`d:\charlesDevelopment\SQL`).

**C. File-relative path**

If `markdown-pdf.stylesRelativePathFile` is `true`, paths are relative to the Markdown file. For `IST605_Perception_PracticeQuestions.md`, you could use:

```json
"markdown-pdf.styles": [
  "markdown-pdf-style.css"
],
"markdown-pdf.stylesRelativePathFile": true
```

(Place the CSS file in the same folder as the Markdown file, or adjust the path accordingly.)

### 3. Export to PDF

1. Open the Markdown file (e.g. `IST605_Perception_PracticeQuestions.md`).
2. Right-click in the editor → **Markdown PDF: Export (pdf)**
   - Or `Ctrl+Shift+P` → "Markdown PDF: Export (pdf)".

The exported PDF should show answers inside `<details>` blocks.

---

## If answers still do not appear

If the CSS does not show the answers:

1. Use **Option 3** instead: change the Markdown so answers are always visible (no `<details>`).
2. Use **Option 1**: open the Markdown in a browser (e.g. GitHub preview), expand all answers, then print to PDF.
