import unittest
import QuickSelect

class QuickSelextUnitTests(unittest.TestCase):
    '''
    This class contains basic unit tests for the quick select algorithms
    '''

    def setUp(self):
        pass

    def test_2nd_smallest_when_sorted(self):
        '''
        This method tests the quick select algorithm for the 2nd smallest on a sorted array 
        '''

        test_array = [3,4,6,8,9,13,17,23,34]
        k = 2
        quickselect = QuickSelect.QuickSelect(test_array, k=k, smallest=True, debug=True)

        self.assertEqual(quickselect.result, 4)

    def test_2nd_largest_when_sorted(self):
        '''
        This method tests the quick select algorithm for the 2nd bigest on a sorted array
        '''

        test_array = [3,4,6,8,9,13,17,23,34]
        k = 2
        quickselect = QuickSelect.QuickSelect(test_array, k=k, smallest=False, debug=True)

        self.assertEqual(quickselect.result, 23)

    def test_5th_smallest_when_unsorted(self):
        '''
        This method tests quick select algorithm for the 5th smallest on an unsorted array
        '''

        test_array = [13,6,9,23,17,3,4,34,8]
        k = 5
        quickselect = QuickSelect.QuickSelect(test_array, k=k, smallest=True, debug=True)

        self.assertEqual(quickselect.result, 9)

    def test_5th_largest_when_unsorted(self):
        '''
        This method tests the quick select algorithm for the 5th largest on an unsorted array
        '''

        test_array = [13,6,9,23,17,3,4,34,8]
        k = 5
        quickselect = QuickSelect.QuickSelect(test_array, k=k, smallest=False, debug=True)

        self.assertEqual(quickselect.result, 9)

    def test_20th_smallest_outofbounds(self):
        '''
        This method tests the quick select algorithm for the 20th smallest when that is out of bounds
        '''

        test_array = [13,6,9,23,17,3,4,34,8]
        k = 20
        quickselect = QuickSelect.QuickSelect(test_array, k=k, smallest=True, debug=True)

        self.assertEqual(quickselect.result, None)

    def test_20th_largest_outofbounds(self):
        '''
        This method tests the quick select algorithm for the 20th biggest when that is out of bounds
        '''

        test_array = [13,6,9,23,17,3,4,34,8]
        k = 20
        quickselect = QuickSelect.QuickSelect(test_array, k=k, smallest=False, debug=True)

        self.assertEqual(quickselect.result, None)
        
if __name__ == '__main__':
    unittest.main()