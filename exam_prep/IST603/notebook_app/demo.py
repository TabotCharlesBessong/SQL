"""
Demo for the note-taking application with interactive menu.
"""

from menu import Menu
from notebook import Notebook


def main() -> None:
    notebook = Notebook()
    menu = Menu(notebook)
    menu.run()


if __name__ == "__main__":
    main()
