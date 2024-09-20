""" 
The code below defines a library catalog that uses hash tables (dictionaries) to store and retrieve books by their ISBN, title,
and author. The LibraryCatalog class allows adding new books and searching for books by their ISBN, title,or author. It maintains
three dictionaries: one mapping ISBNs to book details, another mapping titles to ISBNs for reverse lookup, and a third mapping
authors to lists of ISBNs for books they have written. 
"""

class LibraryCatalog:
    def __init__(self):
        # Hash tables to store books by ISBN, title, and author
        self.books_by_isbn = {}
        self.books_by_title = {}
        self.books_by_author = {}

    def add_book(self, isbn, title, author):
        # Insert book details into hash tables
        self.books_by_isbn[isbn] = (title, author)
        self.books_by_title[title] = isbn
        if author not in self.books_by_author:
            self.books_by_author[author] = []
        self.books_by_author[author].append(isbn)

    def search_by_isbn(self, isbn):
        # Search for book by ISBN
        return self.books_by_isbn.get(isbn, "Book not found")

    def search_by_title(self, title):
        # Search for book by title
        isbn = self.books_by_title.get(title, None)
        return self.search_by_isbn(isbn) if isbn else "Book not found"

    def search_by_author(self, author):
        # Search for books by author
        return self.books_by_author.get(author, [])
