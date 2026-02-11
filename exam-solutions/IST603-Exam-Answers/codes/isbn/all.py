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
        
        
        

if __name__ == "__main__":
  # create ISBN
  isbn = ISBN(0,941831,39,6)
  
  # create Book
  book = Book(
    "Object First with Java",
    "David j. Barnes and Michael Kolling",
    "Prentice Hall",
    "London",
    "2020",
    45.99,
    isbn
  )
  
  book.print_details()