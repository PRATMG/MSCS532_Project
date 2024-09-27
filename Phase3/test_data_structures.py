"""
This code provides a comprehensive set of test cases for three data structures: 
ScalableAVLTree, ScalableHashTable, and OptimizedCheckedOutBooks. Each test function 
evaluates the basic functionality of its respective data structure by inserting 
sample data, performing searches or updates, and using assertions to ensure correctness. 
The code also includes stress tests that measure the performance of bulk operations, 
such as inserting a large number of entries. The run_all_tests function orchestrates 
the execution of all individual tests, and the script executes this function when run as 
the main module.
"""

import time
from scalable_avl_tree import ScalableAVLTree
from scalable_hash_table import ScalableHashTable
from optimized_checked_out_books import OptimizedCheckedOutBooks

# Comprehensive set of test cases for AVL Tree, Hash Table, and Checked Out Books (Hash Map)

def test_avl_tree():
    """
    Test the basic functionality and performance of the ScalableAVLTree class.
    This includes insertion, search, and stress testing with a large dataset.
    """
    print("Testing AVL Tree...")
    avl_tree = ScalableAVLTree()
    
    # Insert sample books into AVL Tree
    avl_tree.insert("Introduction to Algorithms", "978-0262046305")
    avl_tree.insert("The C Programming Language", "978-0131103627")
    avl_tree.insert("The Mythical Man-Month", "978-0201616224")
    
    # Test search functionality
    assert avl_tree.search("Introduction to Algorithms").value == "978-0262046305", \
        "Failed to find correct ISBN for 'Introduction to Algorithms'"
    assert avl_tree.search("The C Programming Language").value == "978-0131103627", \
        "Failed to find correct ISBN for 'The C Programming Language'"
    assert avl_tree.search("Non-Existent Book") == None, \
        "Non-existent book should return None"
    
    print("AVL Tree basic tests passed.")

    # Stress test AVL tree with a large number of insertions
    print("Stress testing AVL Tree...")
    start_time = time.time()
    for i in range(100000):
        avl_tree.insert(f"Book {i}", f"ISBN-{i}")
    end_time = time.time()
    print(f"Inserting 100,000 books into AVL Tree took {end_time - start_time:.2f} seconds.")

def test_hash_table():
    """
    Test the basic functionality and performance of the ScalableHashTable class.
    This includes adding books, searching by ISBN, and stress testing with a large dataset.
    """
    print("Testing Hash Table...")
    catalog = ScalableHashTable()
    
    # Insert sample books into Hash Table
    catalog.add_book("978-0262046305", ("Introduction to Algorithms", "Thomas H. Cormen"))
    catalog.add_book("978-0131103627", ("The C Programming Language", "Brian W. Kernighan"))
    
    # Test search functionality by ISBN
    assert catalog.search_by_isbn("978-0262046305") == ("Introduction to Algorithms", "Thomas H. Cormen"), \
        "Failed to find correct book for ISBN 978-0262046305"
    assert catalog.search_by_isbn("978-0131103627") == ("The C Programming Language", "Brian W. Kernighan"), \
        "Failed to find correct book for ISBN 978-0131103627"
    assert catalog.search_by_isbn("Non-Existent ISBN") == "Book not found", \
        "Should return 'Book not found' for non-existent ISBN"
    
    print("Hash Table basic tests passed.")
    
    # Stress test Hash Table with a large number of insertions
    print("Stress testing Hash Table...")
    start_time = time.time()
    for i in range(1000000):
        catalog.add_book(f"978-{i}", (f"Book {i}", f"Author {i}"))
    end_time = time.time()
    print(f"Inserting 1 million books into Hash Table took {end_time - start_time:.2f} seconds.")

def test_checked_out_books():
    """
    Test the basic functionality and performance of the OptimizedCheckedOutBooks class.
    This includes checking out and returning books, and stress testing with a large dataset.
    """
    print("Testing Checked Out Books (Hash Map)...")
    checked_out_books = OptimizedCheckedOutBooks()
    
    # Check out sample books
    checked_out_books.check_out("Introduction to Algorithms")
    checked_out_books.check_out("The C Programming Language")
    
    # Return books and test functionality
    assert checked_out_books.return_book("Introduction to Algorithms") == True, \
        "Failed to return 'Introduction to Algorithms'"
    assert checked_out_books.return_book("Non-Existent Book") == False, \
        "Returning a non-existent book should return False"
    
    print("Checked Out Books basic tests passed.")
    
    # Stress test Checked Out Books with a large number of check-outs
    print("Stress testing Checked Out Books...")
    start_time = time.time()
    for i in range(1000000):
        checked_out_books.check_out(f"Book {i}")
    end_time = time.time()
    print(f"Checking out 1 million books took {end_time - start_time:.2f} seconds.")

def run_all_tests():
    """
    Run all test functions for the different data structures.
    """
    print("Running all tests...")
    
    # Run tests for AVL Tree
    test_avl_tree()
    
    # Run tests for Hash Table
    test_hash_table()
    
    # Run tests for Checked Out Books
    test_checked_out_books()
    
    print("All tests passed successfully.")

# To execute tests, call run_all_tests()
if __name__ == "__main__":
    # If the script is run directly, execute all tests
    run_all_tests()
