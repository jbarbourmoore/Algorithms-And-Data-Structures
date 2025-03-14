import unittest
import BinarySearch

import HelperClasses.GenerateArrays as genArrays

class BinarySearchUnitTests(unittest.TestCase):
    '''
    This class contains basic unit tests for the binary search algorithms
    '''

    def setUp(self):
        pass

    def test_recursive_item_smaller_than_smallest(self):
        '''
        This method tests that the binary search algorithm functions properly with an item smaller than the smallest 
        '''

        test_array = [3,4,6,8,9,13,17,23,34]
        item_searched = 2
        result,counter = BinarySearch.recursiveBinarySearch(test_array, item_searched)
        self.assertEqual(result, None)
    
    def test_loop_based_item_smaller_than_smallest(self):
        '''
        This method tests that the binary search algorithm functions properly with an item smaller than the smallest 
        '''

        test_array = [3,4,6,8,9,13,17,23,34]
        item_searched = 2
        result,counter = BinarySearch.loop_based_binary_search(test_array, item_searched)
        self.assertEqual(result, None)

    def test_recursive_item_bigger_than_largest(self):
        '''
        This method tests that the binary search algorithm functions properly with an item bigger than the largest 
        '''

        test_array = [3,4,6,8,9,13,17,23,34]
        item_searched = 54
        result,counter = BinarySearch.recursiveBinarySearch(test_array, item_searched)
        self.assertEqual(result, None)

    def test_loop_based_item_bigger_than_largest(self):
        '''
        This method tests that the binary search algorithm functions properly with an item bigger than the largest 
        '''

        test_array = [3,4,6,8,9,13,17,23,34]
        item_searched = 54
        result,counter = BinarySearch.loop_based_binary_search(test_array, item_searched)
        self.assertEqual(result, None)

    def test_recursive_item_in_middle(self):
        '''
        This method tests that the binary search algorithm functions properly with an item in the middle
        '''

        test_array = [3,4,6,8,9,13,17,23,34]
        item_searched = 9
        result,counter = BinarySearch.recursiveBinarySearch(test_array, item_searched)
        self.assertEqual(result, 4)
    
    def test_loop_based_item_in_middle(self):
        '''
        This method tests that the binary search algorithm functions properly with an item in the middle
        '''

        test_array = [3,4,6,8,9,13,17,23,34]
        item_searched = 9
        result,counter = BinarySearch.loop_based_binary_search(test_array, item_searched)
        self.assertEqual(result, 4)

    def test_recursive_smallest_item(self):
        '''
        This method tests that the binary search algorithm functions properly with the smallest item
        '''

        test_array = [3,4,6,8,9,13,17,23,34]
        item_searched = 3
        result,counter = BinarySearch.recursiveBinarySearch(test_array, item_searched)
        self.assertEqual(result, 0)
    
    def test_loop_based_smallest_item(self):
        '''
        This method tests that the binary search algorithm functions properly with the smallest item
        '''

        test_array = [3,4,6,8,9,13,17,23,34]
        item_searched = 3
        result,counter = BinarySearch.loop_based_binary_search(test_array, item_searched)
        self.assertEqual(result, 0)

    def test_recursive_largest_item(self):
        '''
        This method tests that the binary search algorithm functions properly with the largest item
        '''

        test_array = [3,4,6,8,9,13,17,23,34]
        item_searched = 34
        result,counter = BinarySearch.recursiveBinarySearch(test_array, item_searched)
        self.assertEqual(result, 8)

    def test_loop_based_largest_item(self):
        '''
        This method tests that the binary search algorithm functions properly with the largest item
        '''

        test_array = [3,4,6,8,9,13,17,23,34]
        item_searched = 34
        result,counter = BinarySearch.loop_based_binary_search(test_array, item_searched)
        self.assertEqual(result, 8)

    def test_recursive_10000_item_random_array(self):
        '''
        This method tests that the the binary search algorithm functions properly with an large random array
        '''

        test_array = genArrays.generate_random_array(10000,0,20000)
        item_searched = test_array[0]
        test_array.sort()
        result,counter = BinarySearch.recursiveBinarySearch(test_array, item_searched)
        self.assertEqual(item_searched, test_array[result])
    
    def test_loop_based_10000_item_random_array(self):
        '''
        This method tests that the the binary search algorithm functions properly with an large random array
        '''

        test_array = genArrays.generate_random_array(10000,0,20000)
        item_searched = test_array[0]
        test_array.sort()
        result,counter = BinarySearch.loop_based_binary_search(test_array, item_searched)
        self.assertEqual(item_searched, test_array[result])

    def test_recursive_100_50_item_random_arrays(self):
        '''
        This method tests that the the binary search algorithm functions properly with multiple 50 element arrays
        '''

        for _ in range(0,100):
            test_array = genArrays.generate_random_array(50,0,100)
            item_searched = test_array[0]
            test_array.sort()
            result,counter = BinarySearch.recursiveBinarySearch(test_array, item_searched)
            self.assertEqual(item_searched, test_array[result])

    def test_loop_based_100_50_item_random_arrays(self):
        '''
        This method tests that the the binary search algorithm functions properly with multiple 50 element arrays
        '''

        for _ in range(0,100):
            test_array = genArrays.generate_random_array(50,0,100)
            item_searched = test_array[0]
            test_array.sort()
            result,counter = BinarySearch.loop_based_binary_search(test_array, item_searched)
            self.assertEqual(item_searched, test_array[result])

if __name__ == '__main__':
    unittest.main()