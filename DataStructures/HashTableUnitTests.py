import unittest
import HashTable

class HashTableUnitTests(unittest.TestCase):
    '''
    This class contains basic unit tests for the hash table data structue
    '''

    def setUp(self):
        '''
        This method sets up a hash table to be used as the stating point for each unit test

        Starting item count : 4
        Starting row count : 8
        Starting load factor : .5
        '''

        print("SETUP")
        print("Creating a hash table with 4 items, a load factor of .5 and a row count of 8")

        self.hashtable = HashTable.HashTable(debug=True)

        items_to_add = ["Let", "The", "Testing", "Begin"]

        for item_to_add in items_to_add:
            self.hashtable.addItem(item=item_to_add)

        self.hashtable.outputHashTable()
        
        self.assertEqual(self.hashtable.count_items, 4)
        self.assertEqual(self.hashtable.load_factor, .5)
        self.assertEqual(self.hashtable.row_count, 8)



    def test_add_item_int(self):
        '''
        This method tests the addItem method for the hash table with an int value
        '''

        self.hashtable.addItem(23)
        self.hashtable.outputHashTable()     

        self.assertEqual(self.hashtable.count_items, 5)
        self.assertEqual(self.hashtable.load_factor, .3125)
        self.assertEqual(self.hashtable.row_count, 16)    

    def test_add_item_str(self):
        '''
        This method tests the addItem method for the hash table with an string value
        '''

        self.hashtable.addItem("I am a new Item")
        self.hashtable.outputHashTable()     

        self.assertEqual(self.hashtable.count_items, 5)
        self.assertEqual(self.hashtable.load_factor, .3125)
        self.assertEqual(self.hashtable.row_count, 16)      

    def test_add_item_bool(self):
        '''
        This method tests the addItem method for the hash table with an string value
        '''

        self.hashtable.addItem(True)
        self.hashtable.outputHashTable()     

        self.assertEqual(self.hashtable.count_items, 5)
        self.assertEqual(self.hashtable.load_factor, .3125)
        self.assertEqual(self.hashtable.row_count, 16)   

    def test_delete_item(self):
        '''
        This method tests the deleteItem methof for the hash table
        '''

        self.hashtable.deleteItem("Begin")
        self.hashtable.outputHashTable()
        
        self.assertEqual(self.hashtable.count_items, 3)
        self.assertEqual(self.hashtable.load_factor, .375)
        self.assertEqual(self.hashtable.row_count, 8)

    def test_delete_item_dne(self):
        '''
        This method tests the deleteItem method for the hash table if an item is not in the hash table
        '''

        self.hashtable.deleteItem(42)
        self.hashtable.outputHashTable()
        
        self.assertEqual(self.hashtable.count_items, 4)
        self.assertEqual(self.hashtable.load_factor, .5)
        self.assertEqual(self.hashtable.row_count, 8)

if __name__ == '__main__':
    unittest.main()