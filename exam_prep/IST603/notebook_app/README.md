# Note-taking application (UML)

Implements **Notebook** and **Note** from the class diagram, plus an interactive **Menu** for command-line interaction.

## Python

- `note.py` — **Note**: `memo`, `creation_date`, `tags`, `match(search_filter)`
- `notebook.py` — **Notebook**: `notes`, `search(filter)`, `new_note(memo, tags="")`, `modify_memo(note_id, memo)`, `modify_tags(note_id, tags)`
- `menu.py` — **Menu**: Interactive command-line interface with options:
  1. Show notes
  2. Search notes
  3. Add note
  4. Modify note
  5. Quit

Run from this folder:
```bash
python demo.py
```

## Java

- `java/ist603/notebook/Note.java` — same attributes and `match(String)`
- `java/ist603/notebook/Notebook.java` — same operations (method names: `newNote`, `modifyMemo`, `modifyTags`)
- `java/ist603/notebook/Menu.java` — Interactive command-line interface with the same 5 options

Compile and run from `java`:
```bash
cd java
javac ist603/notebook/*.java
java ist603.notebook.Demo
```

The **Menu** class provides a user-friendly terminal interface for all notebook operations.
