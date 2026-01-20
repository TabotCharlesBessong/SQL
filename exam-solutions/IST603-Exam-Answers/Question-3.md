# Question 3: Simple Classes in Python
## IST603 - Object-Oriented Programming with Java and Python
**Total Marks: 18 marks**

---

## Requirements:
Repeat Question 2, this time in the Python language, and using an initializer instead of a constructor.

---

## Part a) ISBN Class in Python (9 marks)

### Solution:

```python
class ISBN:
    """Class to represent an International Standard Book Number."""
    
    def __init__(self, country_number, publisher_number, title_number, check_digit):
        """
        Initializer for ISBN class.
        
        Parameters:
        - country_number: First part of ISBN
        - publisher_number: Second part of ISBN
        - title_number: Third part of ISBN
        - check_digit: Fourth part of ISBN
        """
        self.country_number = country_number
        self.publisher_number = publisher_number
        self.title_number = title_number
        self.check_digit = check_digit
    
    def get_ISBN(self):
        """
        Returns a properly formatted string representing the ISBN.
        
        Returns:
        - Formatted ISBN string with spaces between parts
        """
        return f"{self.country_number} {self.publisher_number} {self.title_number} {self.check_digit}"
    
    def set_ISBN(self, country_number, publisher_number, title_number, check_digit):
        """
        Sets new values for the ISBN instance variables.
        
        Parameters:
        - country_number: New country number
        - publisher_number: New publisher number
        - title_number: New title number
        - check_digit: New check digit
        """
        self.country_number = country_number
        self.publisher_number = publisher_number
        self.title_number = title_number
        self.check_digit = check_digit
```

### Explanation:

1. **`__init__` Method (Initializer):**
   - Python uses `__init__` instead of a constructor
   - `self` is the first parameter (reference to the instance)
   - Takes four integer parameters
   - Initializes instance variables using `self.variable_name`

2. **`get_ISBN()` Method:**
   - Returns formatted string using f-string formatting
   - Format: `"country publisher title check"` with spaces

3. **`set_ISBN()` Method:**
   - Takes four integer parameters
   - Updates all instance variables

### Example Usage:

```python
# Create an ISBN object
isbn = ISBN(0, 941831, 39, 6)

# Get the formatted ISBN
formatted_isbn = isbn.get_ISBN()
print(formatted_isbn)  # Output: "0 941831 39 6"

# Set new ISBN values
isbn.set_ISBN(1, 234567, 89, 0)
print(isbn.get_ISBN())  # Output: "1 234567 89 0"
```

---

## Part b) Book Class in Python (9 marks)

### Solution:

```python
class Book:
    """Class to represent a book with its information."""
    
    def __init__(self, title, author, publisher, city, date_of_publication, price, isbn_num):
        """
        Initializer for Book class.
        
        Parameters:
        - title: Book title
        - author: Book author
        - publisher: Publisher name
        - city: City of publication
        - date_of_publication: Date of publication (string)
        - price: Book price
        - isbn_num: ISBN object
        """
        self.title = title
        self.author = author
        self.publisher = publisher
        self.city = city
        self.date_of_publication = date_of_publication
        self.price = price
        self.isbn_num = isbn_num
    
    def set_book_ISBN(self, isbn_num):
        """
        Sets the ISBN for the book.
        
        Parameters:
        - isbn_num: ISBN object
        """
        self.isbn_num = isbn_num
    
    def get_author(self):
        """
        Returns the author of the book.
        
        Returns:
        - Author name as string
        """
        return self.author
    
    def get_book_ISBN(self):
        """
        Returns the ISBN object of the book.
        
        Returns:
        - ISBN object
        """
        return self.isbn_num
    
    def print_details(self):
        """
        Prints the book information in the specified format.
        """
        print(f"Book Title: {self.title}")
        print(f"Book Author: {self.author}")
        print(f"Publisher: {self.publisher}")
        print(f"ISBN: {self.isbn_num.get_ISBN()}")
```

### Explanation:

1. **`__init__` Method:**
   - Takes all book information as parameters
   - `isbn_num` is an `ISBN` object (composition)
   - Initializes all instance variables

2. **`set_book_ISBN(isbn_num)`:**
   - Takes an `ISBN` object
   - Updates the `isbn_num` instance variable

3. **`get_author()`:**
   - Returns the author string

4. **`get_book_ISBN()`:**
   - Returns the `ISBN` object

5. **`print_details()`:**
   - Prints book information using f-strings
   - Calls `isbn_num.get_ISBN()` to get formatted ISBN string

### Example Usage:

```python
# Create an ISBN object
isbn = ISBN(0, 941831, 39, 6)

# Create a Book object
book = Book(
    "Object First with Java",
    "David j. Barnes and Michael Kolling",
    "Prentice Hall",
    "London",
    "2020",
    45.99,
    isbn
)

# Print book details
book.print_details()
# Output:
# Book Title: Object First with Java
# Book Author: David j. Barnes and Michael Kolling
# Publisher: Prentice Hall
# ISBN: 0 941831 39 6

# Get author
author = book.get_author()
print(author)  # Output: "David j. Barnes and Michael Kolling"

# Get ISBN object
book_isbn = book.get_book_ISBN()
print(book_isbn.get_ISBN())  # Output: "0 941831 39 6"

# Set new ISBN
new_isbn = ISBN(1, 234567, 89, 0)
book.set_book_ISBN(new_isbn)
book.print_details()
# ISBN will now show: "1 234567 89 0"
```

---

## Complete Example with Both Classes:

```python
# ISBN Class
class ISBN:
    def __init__(self, country_number, publisher_number, title_number, check_digit):
        self.country_number = country_number
        self.publisher_number = publisher_number
        self.title_number = title_number
        self.check_digit = check_digit
    
    def get_ISBN(self):
        return f"{self.country_number} {self.publisher_number} {self.title_number} {self.check_digit}"
    
    def set_ISBN(self, country_number, publisher_number, title_number, check_digit):
        self.country_number = country_number
        self.publisher_number = publisher_number
        self.title_number = title_number
        self.check_digit = check_digit


# Book Class
class Book:
    def __init__(self, title, author, publisher, city, date_of_publication, price, isbn_num):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.city = city
        self.date_of_publication = date_of_publication
        self.price = price
        self.isbn_num = isbn_num
    
    def set_book_ISBN(self, isbn_num):
        self.isbn_num = isbn_num
    
    def get_author(self):
        return self.author
    
    def get_book_ISBN(self):
        return self.isbn_num
    
    def print_details(self):
        print(f"Book Title: {self.title}")
        print(f"Book Author: {self.author}")
        print(f"Publisher: {self.publisher}")
        print(f"ISBN: {self.isbn_num.get_ISBN()}")


# Test Program
if __name__ == "__main__":
    # Create ISBN
    isbn = ISBN(0, 941831, 39, 6)
    
    # Create Book
    book = Book(
        "Object First with Java",
        "David j. Barnes and Michael Kolling",
        "Prentice Hall",
        "London",
        "2020",
        45.99,
        isbn
    )
    
    # Print details
    book.print_details()
```

**Output:**
```
Book Title: Object First with Java
Book Author: David j. Barnes and Michael Kolling
Publisher: Prentice Hall
ISBN: 0 941831 39 6
```

---

## Key Differences: Java vs Python

| Feature | Java | Python |
|---------|------|--------|
| Constructor | `public ClassName(...)` | `__init__(self, ...)` |
| Instance Variables | `private int x;` | `self.x = value` |
| Method Definition | `public void method()` | `def method(self):` |
| String Formatting | Concatenation with `+` | f-strings or `.format()` |
| Access Modifiers | `private`, `public` | Convention: `_` prefix for private |
| Return Type | Explicit (`String`, `void`) | Implicit (no return = `None`) |
| Object Creation | `new ClassName(...)` | `ClassName(...)` |

---

## Key Concepts Demonstrated:

1. **Python Initializer:** Using `__init__` instead of constructor
2. **Self Parameter:** Required first parameter in all instance methods
3. **Instance Variables:** Created dynamically using `self.variable_name`
4. **String Formatting:** Using f-strings for clean string formatting
5. **Composition:** Book class contains an ISBN object
6. **Method Naming:** Python convention uses snake_case

---

**End of Question 3**
