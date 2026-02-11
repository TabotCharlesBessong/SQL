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