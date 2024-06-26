import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
  
    
    def test_1_add_book(self): 
        # Create instance
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        # add a book and test if it is in `book_list`.
        test_object.add_book("War of the Worlds", 4)
        self.assertEqual(1,len(test_object.book_list))
        
        
    def test_2_add_book(self):
        # Create instance
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        # add the same book twice. Test if it's in `book_list` only once.
        test_object.add_book("War of the Worlds", 4) 
        expected = len(test_object.book_list)
        test_object.add_book("War of the Worlds", 4)
        actual = len(test_object.book_list)
        self.assertEqual(actual, expected)
        
        
    def test_3_has_read(self): 
        # Create instance
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        # pass a book in the list and test if the answer is `True`.
        test_object.add_book("War of the Worlds", 4)
        self.assertTrue(test_object.has_read("War of the Worlds"))
        
        
    def test_4_has_read(self): 
        # Create instance
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        test_object.add_book("War of the Worlds", 4)
        self.assertFalse(test_object.has_read("Barbie"))
        
        
    def test_5_num_books_read(self): 
        # Create instance
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        # add some books to the list, and test num_books matches expected.
        test_object.add_book("Jane Eyre", 4)
        test_object.add_book("Fight Club", 3)
        test_object.add_book("The Divine Comedy", 5)
        test_object.add_book("The Popol Vuh", 5)
        # Give expected value
        books_in_list = 4
        # Compare expected value with num_books
        self.assertEqual(books_in_list,test_object.num_books)
        
        
    def test_6_fav_books(self):
        # Create instance
        test_object = BookLover("Han Solo", "hsolo@millenniumfalcon.com", "scifi")
        # add some books with ratings to the list, making sure some of them have rating > 3.
        test_object.add_book("Jane Eyre", 4)
        test_object.add_book("Fight Club", 3)
        test_object.add_book("The Divine Comedy", 5)
        test_object.add_book("The Popol Vuh", 5)
        # Your test should check that the returned books have rating  > 3 
        expected_value2 = 3
        self.assertEqual(expected_value2, len(test_object.fav_books()))
        
             
if __name__ == '__main__':
    
    unittest.main(verbosity=3)