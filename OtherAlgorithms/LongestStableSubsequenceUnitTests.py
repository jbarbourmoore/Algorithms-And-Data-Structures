import unittest
from LongestStableSubsequence import LongestStableSubsequence

class UsingPolynomialMultiplication_FFT_UnitTests(unittest.TestCase):
    '''
    This class contains basic unit tests for the binary search algorithms
    '''

    def setUp(self):
        pass

    def test_stableSubsequenceLength(self):
        '''
        This method tests finding the length of the longest stable subsequence
        '''

        sequence = LongestStableSubsequence([1, 4, 2, 3, -2, 0, -1, -5, 2, 3])
        n1 = sequence.stableSubsequenceLength(0, -1)
        self.assertEqual( n1 , 5 , msg=f"The longest subsequence length should be 5, but is showing {n1}")
        
    def test_stableSubsequenceLongerLength(self):
        '''
        This method tests finding the length of the longest stable subsequence
        '''

        sequence = LongestStableSubsequence([6, 5, 2, 4, -7, 3, 1, 4, 2, 3, -2, 0, -1, 1, 2, 4, 3, 2, 6, -5, 2, 3])
        n1 = sequence.stableSubsequenceLength(0, -1)
        self.assertEqual( n1 , 11 , msg=f"The longest subsequence length should be 14, but is showing {n1}")

    def test_stableSubsequenceLength_SingularDigit(self):
        '''
        This method tests finding the length of the longest stable subsequence if there is not real stable subsequence so the length is a single digit
        '''

        sequence = LongestStableSubsequence([1, 4, 7, 9, 11, -5, -8, -10])
        n1 = sequence.stableSubsequenceLength(0, -1)
        self.assertEqual( n1 , 1 , msg=f"The longest subsequence length should be 1, but is showing {n1}")

if __name__ == '__main__':
    unittest.main()