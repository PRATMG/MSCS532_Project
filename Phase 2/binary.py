"""
The code  below defines a binary search tree (BST) for books, where each node 
stores the book title as the key and a dictionary containing ISBN and author 
information as the value. The BookBST class allows for inserting new books into 
the tree while maintaining the binary search property (left child is smaller, 
right child is larger) and searching for books by their title.

"""

class TreeNode:
    def __init__(self, key, value):
        self.key = key  # Book title (used as the node's key)
        self.value = value  # Dictionary containing book details (ISBN, author)
        self.left = None  # Left child node (smaller keys)
        self.right = None  # Right child node (larger keys)

class BookBST:
    # Initialize an empty binary search tree.
    def __init__(self):
        self.root = None  # Root of the BST

    def insert(self, key, value):
       # Insert a book into the BST using the book title (key) and details (value). 
       # If the root is empty, the new node becomes the root.
        if self.root is None:
            self.root = TreeNode(key, value)  # Insert at the root if tree is empty
        else:
            self._insert(self.root, key, value)  # Delegate to helper method for recursive insertion
    
    def _insert(self, node, key, value):
        # Recursively insert a new book into the BST.
        # Insert left if the key is smaller, and right if larger.
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key, value)  # Insert as left child
            else:
                self._insert(node.left, key, value)  # Recur on the left subtree
        elif key > node.key:
            if node.right is None:
                node.right = TreeNode(key, value)  # Insert as right child
            else:
                self._insert(node.right, key, value)  # Recur on the right subtree

    def search(self, key):
        # Search for a book by title (key) in the BST. 
       #  Return the node if found, otherwise return None.
        return self._search(self.root, key)  # Start search from the root
    
    def _search(self, node, key):
        # Recursively search for a node with the given key (book title).
        # Return the node if found, otherwise return None.
        if node is None or node.key == key:
            return node  # Base case: found the node or reached the end of the tree
        if key < node.key:
            return self._search(node.left, key)  # Recur on the left subtree
        return self._search(node.right, key)  # Recur on the right subtree
