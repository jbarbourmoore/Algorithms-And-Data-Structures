import unittest
from BinarySearchTree import BinarySearchTree
from BinarySearchTree import BinarySearchTreeNode

class BinarySearchTreeUnitTests(unittest.TestCase):
    '''
    This class contains basic unit tests for the binary search tree data structure
    '''

    def setUp(self):
        '''
        This method sets up a binary search tree to be used as the stating point for each unit test

        Starting item count : 10
        Starting root node : 5
        '''

        print("SETUP")
        print("Creating a binary search tree with 10 items, and a root node of 5")

        self.intial_ordered_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        values_for_tree = [1,3,2,7,5,6,8,9,4,10]
        self.binarysearchtree = BinarySearchTree(initial_values_list=values_for_tree, debug=False)
        self.binarysearchtree.printNodesInAscendingOrder()

        self.assertEqual(self.binarysearchtree.getNodeValuesAsOrderedList(),self.intial_ordered_list)
        self.assertEqual(self.binarysearchtree.root.getValue(),5)


    def test_add_item_larger(self):
        '''
        This method tests the insertItem method for the binary search tree with a larger item
        '''
        self.binarysearchtree.insertItem(42)


        self.assertEqual(self.binarysearchtree.getNodeValuesAsOrderedList(), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 42])
        self.binarysearchtree.printNodesInAscendingOrder()
        self.assertEqual(self.binarysearchtree.root.getValue(),5)

    def test_add_item_smaller(self):
        '''
        This method tests the insertItem method for the binary search tree with a smaller item
        '''
        self.binarysearchtree.insertItem(0)

        self.assertEqual(self.binarysearchtree.getNodeValuesAsOrderedList(), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.binarysearchtree.printNodesInAscendingOrder()
        self.assertEqual(self.binarysearchtree.root.getValue(),5)

    def test_add_item_already_exists(self):
        '''
        This method tests the insertItem method for the binary search tree with a duplicate item
        '''
        self.binarysearchtree.insertItem(6)

        self.assertEqual(self.binarysearchtree.getNodeValuesAsOrderedList(), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.binarysearchtree.printNodesInAscendingOrder()
        self.assertEqual(self.binarysearchtree.root.getValue(),5)

    def test_delete_root_item(self):
        '''
        This method tests the deleteItem method for the binary search tree with the root item
        '''
        self.binarysearchtree.deleteItem(5)

        self.assertEqual(self.binarysearchtree.getNodeValuesAsOrderedList(), [1, 2, 3, 4, 6, 7, 8, 9, 10])
        self.binarysearchtree.printNodesInAscendingOrder()
        self.assertEqual(self.binarysearchtree.root.getValue(),6)

    def test_delete_leaf(self):
        '''
        This method tests the deleteItem method for the binary search tree with the root item
        '''
        self.binarysearchtree.deleteItem(10)

        self.assertEqual(self.binarysearchtree.getNodeValuesAsOrderedList(), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.binarysearchtree.printNodesInAscendingOrder()
        self.assertEqual(self.binarysearchtree.root.getValue(), 5)

    def test_delete_dne(self):
        '''
        This method tests the deleteItem method for the binary search tree with the root item
        '''
        self.binarysearchtree.deleteItem(42)

        self.assertEqual(self.binarysearchtree.getNodeValuesAsOrderedList(), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.binarysearchtree.printNodesInAscendingOrder()
        self.assertEqual(self.binarysearchtree.root.getValue(), 5)

    def test_delete_all_items(self):
        '''
        This method tests the deleteItem method for the binary search tree with all items
        '''
        for item in self.intial_ordered_list:
            self.binarysearchtree.printNodesInAscendingOrder()
            self.binarysearchtree.deleteItem(item)

        self.assertEqual(self.binarysearchtree.getNodeValuesAsOrderedList(), [])
        self.binarysearchtree.printNodesInAscendingOrder()

if __name__ == '__main__':
    unittest.main()