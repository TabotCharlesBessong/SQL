
class Book:
  """Class to represent a book with its information."""
  
  def __init__(self,title,author,publisher,city,date_of_publication, price, isbn_num):
    """
    Initializer for Book class
    
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