package codes.isbn;

public class Book {
  // Instance variables
  private String title;
  private String author;
  private String publisher;
  private String city;
  private String dateOfPublication;
  private double price;
  private ISBN isbnNum;

  // Constructor
  public Book(String title, String author, String publisher, String city,
      String dateOfPublication, double price, ISBN isbnNum) {
    this.title = title;
    this.author = author;
    this.publisher = publisher;
    this.city = city;
    this.dateOfPublication = dateOfPublication;
    this.price = price;
    this.isbnNum = isbnNum;
  }

  // Method to set the ISBN for the book
  public void setBookISBN(ISBN isbnNum) {
    this.isbnNum = isbnNum;
  }

  // Method to get the author of the book
  public String getAuthor() {
    return author;
  }

  // Method to get the ISBN of the book
  public ISBN getBookISBN() {
    return isbnNum;
  }

  // Method to print book details in the specified format
  public void printDetails() {
    System.out.println("Book Title: " + title);
    System.out.println("Book Author: " + author);
    System.out.println("Publisher: " + publisher);
    System.out.println("ISBN: " + isbnNum.getISBN());
    System.out.println("City: " + city);
    System.out.println("Date of Publication: " + dateOfPublication);
    System.out.println("Price: $" + price);
  }
}
