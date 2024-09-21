""" 
The code below defines a simple linked list structure to manage books that have been checked out from a library. 
The CheckedOutBooks class allows for checking out books by adding them to the front of the list and returning books 
by removing them from the list. Each book is represented by a ListNode, which stores the book's title and a reference 
to the next node in the list. The class supports operations to check out a book and return a book by searching through
the linked list.
"""


class ListNode:
    # Initialize a node with the book title and a pointer to the next node.
    def __init__(self, book_title):
        self.book_title = book_title  # Book title stored in this node
        self.next = None  # Pointer to the next node (None by default)

class CheckedOutBooks:
    # Initialize an empty list to track checked-out books. 
    def __init__(self):
        self.head = None  # Head of the linked list (None means no books are checked out)
    def check_out(self, book_title):
        # Check out a book by adding it to the front of the list.
        new_node = ListNode(book_title)  # Create a new node for the checked-out book
        new_node.next = self.head  # Point the new node to the current head (previous book)
        self.head = new_node  # Make the new node the new head (most recent book)
    
    def return_book(self, book_title):
        # Return a book by removing it from the list. Return True if successful, False if the book wasn't found.
        prev = None  # Pointer to track the previous node
        curr = self.head  # Start at the head of the list
        # Traverse the list to find the book
        while curr is not None:
            if curr.book_title == book_title:  # If the book is found
                if prev:  # If the book is not the head of the list
                    prev.next = curr.next  # Remove the current node by linking the previous node to the next one
                else:  # If the book is the head of the list
                    self.head = curr.next  # Update the head to the next node
                return True  # Book successfully returned
            prev = curr  # Move the previous pointer to the current node
            curr = curr.next  # Move to the next node
        return False  # Book not found in the list
