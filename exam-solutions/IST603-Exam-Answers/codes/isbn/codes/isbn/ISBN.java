package codes.isbn;

public class ISBN {
  // Instance variables
  private int countryNumber;
  private int publisherNumber;
  private int titleNumber;
  private int checkDigit;

  // Constructor
  public ISBN(int countryNumber, int publisherNumber, int titleNumber, int checkDigit) {
    this.countryNumber = countryNumber;
    this.publisherNumber = publisherNumber;
    this.titleNumber = titleNumber;
    this.checkDigit = checkDigit;
  }

  // Method to get formatted ISBN string
  public String getISBN() {
    return countryNumber + " " + publisherNumber + " " + titleNumber + " " + checkDigit;
  }

  // Method to set new ISBN values
  public void setISBN(int countryNumber, int publisherNumber, int titleNumber, int checkDigit) {
    this.countryNumber = countryNumber;
    this.publisherNumber = publisherNumber;
    this.titleNumber = titleNumber;
    this.checkDigit = checkDigit;
  }
}
