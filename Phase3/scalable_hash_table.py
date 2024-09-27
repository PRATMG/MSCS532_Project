
"""
This code defines a ScalableHashTable class, which implements a hash table for 
storing book information with dynamic resizing capabilities. It allows adding 
books using their ISBN as the key and associated data (like title and other 
details) as the value. The hash table automatically resizes itself when the 
load factor exceeds 0.75 to maintain efficient performance. It provides methods 
to search for a book by its ISBN and to find an ISBN based on the book's title.
"""
class ScalableHashTable:
    def __init__(self):
        # Initialize the hash table with a default size and empty buckets
        self.table_size = 100
        self.table = [[] for _ in range(self.table_size)]  # List of buckets for chaining
        self.num_entries = 0  # Track the number of entries in the table

    def _hash(self, key):
        # Compute the hash index for a given key
        return hash(key) % self.table_size

    def add_book(self, key, value):
        # Add a book with the given ISBN (key) and book data (value) to the hash table
        index = self._hash(key)
        self.table[index].append((key, value))  # Append to the appropriate bucket
        self.num_entries += 1
        # Resize the table if the load factor exceeds 0.75
        if self.num_entries / self.table_size > 0.75:
            self._resize()

    def _resize(self):
        # Double the table size and rehash all existing entries
        self.table_size *= 2
        new_table = [[] for _ in range(self.table_size)]  # Create a new larger table
        for bucket in self.table:
            for key, value in bucket:
                new_index = hash(key) % self.table_size
                new_table[new_index].append((key, value))  # Rehash entries into new table
        self.table = new_table  # Replace the old table with the new one

    def search_by_isbn(self, isbn):
        # Search for a book by ISBN and return its data
        index = self._hash(isbn)
        for book_isbn, book_data in self.table[index]:
            if book_isbn == isbn:
                return book_data  # Return the book data if ISBN matches
        return "Book not found"

    def search_by_title(self, title):
        # Search for a book by title and return its ISBN
        for bucket in self.table:
            for book_isbn, book_data in bucket:
                if book_data[0] == title:  # Assuming book_data[0] contains the title
                    return book_isbn  # Return the ISBN if title matches
        return "Book not found"
