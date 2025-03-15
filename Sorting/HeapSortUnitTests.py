import unittest
import HeapSort
import HelperClasses.GenerateArrays as genArrays

class HeapSortUnitTests(unittest.TestCase):
    '''
    This class contains basic unit tests for the heap sort algorithm
    '''

    def setUp(self):
        pass

    def test_empty_array(self):
        '''
        This method tests that the heap sort algorithm functions properly with an empty list
        '''
        test_array = []
        test_array_result, _ = HeapSort.HeapSort(test_array.copy())
        self.assertEqual(test_array_result, test_array)

    def test_one_item_array(self):
        '''
        This method tests that the heap sort algorithm functions properly with an array of one item
        '''

        test_array = [5]
        test_array_result, _ = HeapSort.HeapSort(test_array.copy())
        self.assertEqual(test_array_result, test_array)

        
    def test_five_item_sorted_array(self):
        '''
        This method tests that the heap sort algorithm functions properly with pre sorted array
        '''

        test_array = [1,2,3,4,5]
        test_array_result, _ = HeapSort.HeapSort(test_array.copy())
        self.assertEqual(test_array_result, test_array)

    def test_five_item_reverse_array(self):
        '''
        This method tests that the heap sort algorithm functions properly with a reversed array
        '''

        test_array = [5,4,3,2,1]
        test_array_expected_result = [1,2,3,4,5]
        test_array_result = test_array.copy()
        test_array_result, _ = HeapSort.HeapSort(test_array)
        self.assertEqual(test_array_result, test_array_expected_result)

    def test_10000_item_random_array(self):
        '''
        This method tests that the heap sort algorithm functions properly with an large random array
        '''

        test_array = genArrays.generate_random_array(10000,0,20000)
        test_array_expected_result = test_array.copy()
        test_array_expected_result.sort()
        test_array_result, _ = HeapSort.HeapSort(test_array)
        self.assertEqual(test_array_result, test_array_expected_result)

    def test_100_50_item_random_arrays(self):
        '''
        This method tests that the heap sort algorithm functions properly with multiple 50 element arrays
        '''

        for i in range(0,100):
            test_array = genArrays.generate_random_array(50,0,100)
            test_array_expected_result = test_array.copy()
            test_array_expected_result.sort()
            test_array_result, _ = HeapSort.HeapSort(test_array)
            self.assertEqual(test_array_result, test_array_expected_result)

if __name__ == '__main__':
    unittest.main()