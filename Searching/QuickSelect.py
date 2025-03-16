class QuickSelect():
    '''
    This class selects the kth smallest or kth largest element in an array
    '''

    def __init__(self, array, k=1, smallest=True):
        '''
        This method initializes the QuickSelect object with an array, a k value and whether it is searching for smallest

        Parameters :
            array : [int]
                The array that the kth largest / smallest value is being selected from
            k : int 
                The value for how many from the smallest or largest (default is 1)
            smallest : Boolean
                Whether the select is for the kth smallest (default is True)
        '''

        self.array = array
        self.k = k
        self.smallest=smallest

        self.array_length = len(array)

        self.result = self.quickselect(0,self.array_length-1,self.k)

    def quickselect(self, left_index, right_index, local_k):
        '''
        This method is the recursive method that searches for the kth smallest / largest value

        Parameters :
            left_index : int
                The left index of the current search area
            right_index : int 
                The right index of the current search area
            local_k : int
                The value of k with respect to the current search area
        '''

        if (local_k > 0 and self.k <= right_index - left_index + 1):

            partition_index = self.partition(left_index, right_index)

            if (partition_index - left_index == local_k - 1):
                return self.array[partition_index]
            elif (partition_index - left_index > local_k - 1 and self.smallest):
                return self.quickselect( left_index, partition_index - 1, local_k)
            else:
                return self.quickselect(partition_index + 1, right_index, local_k - partition_index + left_index - 1)
    
    def partition(self, left_index, right_index):
        '''
        This method partitions the current search area of the array around the value of the right index

        The partition will be based on elements smaller than the pivot value if the search is for kth smallest
        The partition will be based on elements larger than the pivot value if the search is for kth largest

        Parameters :
            left_index : int
                The left index of the current search area
            right_index : int 
                The right index of the current search area

        Returns : 
            partition_index : int
                The last index of the partition
        '''

        pivot_value = self.array[right_index]
        partition_index = left_index

        for i in range(left_index, right_index):
            if (self.array[i] <= pivot_value and self.smallest) or (self.array[i] >= pivot_value and not self.smallest):

                (self.array[partition_index], self.array[i]) = (self.array[i], self.array[partition_index])
                
                partition_index += 1


        (self.array[partition_index], self.array[right_index]) = (self.array[right_index], self.array[partition_index])

        return partition_index
