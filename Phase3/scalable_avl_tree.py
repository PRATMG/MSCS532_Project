"""
This code implements an AVL tree data structure using two classes: AVLNode and ScalableAVLTree. 
The AVLNode class represents individual nodes in the tree, each containing a key, value, and 
pointers to its left and right children. The ScalableAVLTree class manages the overall tree 
structure, providing methods for inserting new nodes and searching for keys. The AVL tree 
automatically balances itself after each insertion to maintain optimal search performance, 
ensuring that operations like insertion and search run in O(log n) time.
"""

class AVLNode:
    def __init__(self, key, value):
        # Initialize a node with a key, value, and height
        self.key = key
        self.value = value
        self.left = None   # Left child
        self.right = None  # Right child
        self.height = 1    # Height of the node for balancing

class ScalableAVLTree:
    def __init__(self):
        # Initialize an empty AVL tree
        self.root = None

    def _get_height(self, node):
        # Return the height of a node, or 0 if None
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        # Calculate and return the balance factor of a node
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _rotate_right(self, y):
        # Perform a right rotation around node y
        x = y.left
        T2 = x.right

        # Rotate nodes
        x.right = y
        y.left = T2

        # Update heights
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))

        # Return new root after rotation
        return x

    def _rotate_left(self, x):
        # Perform a left rotation around node x
        y = x.right
        T2 = y.left

        # Rotate nodes
        y.left = x
        x.right = T2

        # Update heights
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        # Return new root after rotation
        return y

    def insert(self, key, value):
        # Insert a key-value pair into the AVL tree
        if not self.root:
            # If the tree is empty, create a new root node
            self.root = AVLNode(key, value)
        else:
            # Insert recursively starting from the root
            self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        # Recursive helper function to insert a node
        if not node:
            # Insert new node at the correct position
            return AVLNode(key, value)
        if key < node.key:
            # Traverse left subtree
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            # Traverse right subtree
            node.right = self._insert(node.right, key, value)
        else:
            # Duplicate keys are not allowed; return the existing node
            return node

        # Update the height of the ancestor node
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        # Get the balance factor to check if the node is unbalanced
        balance = self._get_balance(node)

        # Left Left Case
        if balance > 1 and key < node.left.key:
            return self._rotate_right(node)

        # Right Right Case
        if balance < -1 and key > node.right.key:
            return self._rotate_left(node)

        # Left Right Case
        if balance > 1 and key > node.left.key:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        # Right Left Case
        if balance < -1 and key < node.right.key:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        # Return the (possibly updated) node pointer
        return node

    def search(self, key):
        # Search for a node by key and return it
        return self._search(self.root, key)

    def _search(self, node, key):
        # Recursive helper function to search for a key
        if not node or node.key == key:
            # Return the node if found, or None if not found
            return node
        if key < node.key:
            # Traverse left subtree
            return self._search(node.left, key)
        # Traverse right subtree
        return self._search(node.right, key)
