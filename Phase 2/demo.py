# Demo for Hash Table, Binary Search Tree, and Linked List

from binary import BookBST
from hash import LibraryCatalog
from linkedlist import CheckedOutBooks


def demo_library_management():
    # Initialize the data structures
    catalog = LibraryCatalog()
    bst = BookBST()
    checked_out_books = CheckedOutBooks()

    # Add books to the catalog
    catalog.add_book("978-0262046305", "Introduction to Algorithms", "Thomas H. Cormen")
    catalog.add_book("978-0131103627", "The C Programming Language", "Brian W. Kernighan")
    catalog.add_book("978-0201616224", "The Mythical Man-Month", "Frederick P. Brooks")

    # Insert books into Binary Search Tree (BST) by title
    bst.insert("Introduction to Algorithms", "978-0262046305")
    bst.insert("The C Programming Language", "978-0131103627")
    bst.insert("The Mythical Man-Month", "978-0201616224")

    # Display results from Hash Table
    print("\n--- Hash Table Demo ---")
    print(f"Search by ISBN (978-0262046305): {catalog.search_by_isbn('978-0262046305')}")
    print(f"Search by Title (The C Programming Language): {catalog.search_by_title('The C Programming Language')}")
    print(f"Search by Author (Thomas H. Cormen): {catalog.search_by_author('Thomas H. Cormen')}")

    # Demonstrate Binary Search Tree
    print("\n--- Binary Search Tree Demo ---")
    search_result = bst.search("Introduction to Algorithms")
    if search_result:
        print(f"Book found in BST: {search_result.key} -> ISBN: {search_result.value}")
    else:
        print("Book not found in BST")

    # Check out and return books using Linked List
    print("\n--- Linked List Demo (Checked Out Books) ---")
    print("Checking out 'Introduction to Algorithms'...")
    checked_out_books.check_out("Introduction to Algorithms")
    print("Checking out 'The Mythical Man-Month'...")
    checked_out_books.check_out("The Mythical Man-Month")

    print("Returning 'Introduction to Algorithms'...")
    if checked_out_books.return_book("Introduction to Algorithms"):
        print("Returned successfully!")
    else:
        print("Book not found in checked out list.")

# Run the demo
demo_library_management()
