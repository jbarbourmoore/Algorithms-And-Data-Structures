
class LongestStableSubsequence():
    '''
    This class finds the longest "stable" subseqence using dynamic programming

    Stable in this case implies
    1. i_1 < i_2 < ... < i_k 
    2. Each element of the subsequence must be within +/-1 of the previous element.
    '''

    def __init__(self, sequence):
        '''
        This method initialialiazed the Longest Stable Subsequence with a given sequence

        Parameters : 
            sequence : [int]
                The array of numbers for which we are finding the longest stable sub sequence
        '''

        self.sequence = sequence
        self.sequence_length = len(self.sequence)
        
    def stableSubsequenceLength(self, i, j):
        '''
        This is a recursive Method to find the length of the longest stable subsequence

        Parameters : 
            i : int
                The current index
            j : int
                The index being considered

        Returns :
            length : int
                The length of the greatest subsequence
        '''

        value_j = self.sequence[j] if 0 <= j < len(self.sequence) else None 
        value_i = self.sequence[i] if 0 <= i < len(self.sequence) else None 

        if value_j == None and i == 0:
            return 1 + self.stableSubsequenceLength( i + 1, 0 )
        elif value_i == None or value_j == None:
            return 0
        else:
            if abs( value_i - value_j ) <= 1 : 
                return max(1 + self.stableSubsequenceLength( i+1, i ), 0 + self.stableSubsequenceLength( i+1, j )) 
            else: 
                return 0 + self.stableSubsequenceLength( i+1, j )