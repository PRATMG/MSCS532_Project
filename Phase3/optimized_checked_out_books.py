
"""
This code defines an OptimizedCheckedOutBooks class that efficiently 
manages a collection of checked-out books using a dictionary for quick 
lookup and updates. The class provides methods to check out a book by 
adding its title to the dictionary and to return a book by removing its 
title from the dictionary. This implementation allows for constant-time 
operations to check if a book is checked out or to update its status.
"""
class OptimizedCheckedOutBooks:
    def __init__(self):
        # Initialize an empty dictionary to store checked-out books
        self.checked_out_books = {}

    def check_out(self, book_title):
        # Mark the book as checked out by adding it to the dictionary
        self.checked_out_books[book_title] = True

    def return_book(self, book_title):
        # Remove the book from the checked-out dictionary; return False if it wasn't checked out
        return self.checked_out_books.pop(book_title, False)
