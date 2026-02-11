package codes.isbn;

public class Main {
  public static void main(String[] args) {
    // Create an ISBN object
    ISBN isbn = new ISBN(0, 941831, 39, 6);

    // Create a Book object
    Book book = new Book(
        "Object First with Java",
        "David j. Barnes and Michael Kolling",
        "Prentice Hall",
        "London",
        "2020",
        45.99,
        isbn);

    // Print book details
    book.printDetails();
    // Output:
    // Book Title: Object First with Java
    // Book Author: David j. Barnes and Michael Kolling
    // Publisher: Prentice Hall
    // ISBN: 0 941831 39 6

    // Get author
    String author = book.getAuthor();
    System.out.println(author); // Output: "David j. Barnes and Michael Kolling"

    // Get ISBN object
    ISBN bookISBN = book.getBookISBN();
    System.out.println(bookISBN.getISBN()); // Output: "0 941831 39 6"

    // Set new ISBN
    ISBN newISBN = new ISBN(1, 234567, 89, 0);
    book.setBookISBN(newISBN);
    book.printDetails();
    // ISBN will now show: "1 234567 89 0"
  }
}
