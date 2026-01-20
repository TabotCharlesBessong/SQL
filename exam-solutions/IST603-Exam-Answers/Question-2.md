# Question 2: Simple Classes in Java
## IST603 - Object-Oriented Programming with Java and Python
**Total Marks: 9 + 9 = 18 marks**

---

## Part a) ISBN Class Design (9 marks)

### Requirements:
Design a class called `ISBN` to represent an International Standard Book Number. The ISBN consists of 10 digits divided into 4 parts:
- **countryNumber**: The first part (e.g., "0")
- **publisherNumber**: The second part (e.g., "941831")
- **titleNumber**: The third part (e.g., "39")
- **checkDigit**: The fourth part (e.g., "6")

**Example:** ISBN `0 941831 39 6`

### Class Requirements:
1. A constructor
2. A method `getISBN` that returns a properly formatted string
3. A method `setISBN` that takes four integers to set new values

### Solution:

```java
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
```

### Explanation:

1. **Instance Variables:**
   - All four parts are stored as `int` values
   - Declared as `private` for encapsulation

2. **Constructor:**
   - Takes four integer parameters
   - Initializes all instance variables using `this` keyword

3. **getISBN() Method:**
   - Returns a formatted string with spaces between parts
   - Concatenates all parts with spaces: `"country publisher title check"`

4. **setISBN() Method:**
   - Takes four integer parameters
   - Updates all instance variables with new values

### Example Usage:

```java
// Create an ISBN object
ISBN isbn = new ISBN(0, 941831, 39, 6);

// Get the formatted ISBN
String formattedISBN = isbn.getISBN();
System.out.println(formattedISBN);  // Output: "0 941831 39 6"

// Set new ISBN values
isbn.setISBN(1, 234567, 89, 0);
System.out.println(isbn.getISBN());  // Output: "1 234567 89 0"
```

---

## Part b) Book Class Design (9 marks)

### Requirements:
Design a `Book` class that represents relevant information about a book, including:
- **title**: The book's title
- **author**: The book's author
- **publisher**: The publisher name
- **city**: The city of publication
- **dateOfPublication**: Date of publication (as a String)
- **price**: The price of the book
- **isbnNum**: An ISBN object (using the ISBN class from part a)

### Class Requirements:
1. A constructor
2. `setBookISBN`: Method to set the ISBN for the book
3. `getAuthor`: Method to return the author of the book
4. `getBookISBN`: Method to get the ISBN of the book
5. `printDetails`: Method to print book information in the specified format

### Solution:

```java
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
    }
}
```

### Explanation:

1. **Instance Variables:**
   - All book information stored as appropriate data types
   - `isbnNum` is of type `ISBN` (composition relationship)
   - All variables are `private` for encapsulation

2. **Constructor:**
   - Takes all book information as parameters
   - Initializes all instance variables

3. **setBookISBN(ISBN isbnNum):**
   - Takes an `ISBN` object as parameter
   - Updates the `isbnNum` instance variable

4. **getAuthor():**
   - Returns the author string

5. **getBookISBN():**
   - Returns the `ISBN` object
   - Note: Returns the object reference, not the formatted string

6. **printDetails():**
   - Prints book information in the specified format:
     - Book Title: [title]
     - Book Author: [author]
     - Publisher: [publisher]
     - ISBN: [formatted ISBN string]

### Example Usage:

```java
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
    isbn
);

// Print book details
book.printDetails();
// Output:
// Book Title: Object First with Java
// Book Author: David j. Barnes and Michael Kolling
// Publisher: Prentice Hall
// ISBN: 0 941831 39 6

// Get author
String author = book.getAuthor();
System.out.println(author);  // Output: "David j. Barnes and Michael Kolling"

// Get ISBN object
ISBN bookISBN = book.getBookISBN();
System.out.println(bookISBN.getISBN());  // Output: "0 941831 39 6"

// Set new ISBN
ISBN newISBN = new ISBN(1, 234567, 89, 0);
book.setBookISBN(newISBN);
book.printDetails();
// ISBN will now show: "1 234567 89 0"
```

### Complete Example with Both Classes:

```java
public class BookTest {
    public static void main(String[] args) {
        // Create ISBN
        ISBN isbn = new ISBN(0, 941831, 39, 6);
        
        // Create Book
        Book book = new Book(
            "Object First with Java",
            "David j. Barnes and Michael Kolling",
            "Prentice Hall",
            "London",
            "2020",
            45.99,
            isbn
        );
        
        // Print details
        book.printDetails();
    }
}
```

**Output:**
```
Book Title: Object First with Java
Book Author: David j. Barnes and Michael Kolling
Publisher: Prentice Hall
ISBN: 0 941831 39 6
```

---

## Key Concepts Demonstrated:

1. **Class Design:** Proper encapsulation with private instance variables
2. **Constructors:** Initializing objects with required data
3. **Methods:** Getter and setter methods for accessing/modifying data
4. **Composition:** Book class contains an ISBN object (has-a relationship)
5. **String Formatting:** Proper formatting of output strings
6. **Method Return Types:** Appropriate return types (String, ISBN, void)

---

**End of Question 2**
