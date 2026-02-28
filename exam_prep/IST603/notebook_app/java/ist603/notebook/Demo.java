package ist603.notebook;

/**
 * Demo for the note-taking application with interactive menu.
 */
public class Demo {
    public static void main(String[] args) {
        Notebook notebook = new Notebook();
        Menu menu = new Menu(notebook);
        menu.run();
    }
}
