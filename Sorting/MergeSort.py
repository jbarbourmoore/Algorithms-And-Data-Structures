# helper function to swap the elements at two positions in the list
from HelperClasses import GenerateArrays
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class MergeSort():
    def __init__(self, array):
        '''
        This is the contructor for the MergeSort object

        It stores the unsorted array, and a counter value for how many times the recursive method is called

        It also calls the merge sort algorithm and stored the sorted array

        Parameters :
            array : [int]
                The array to be sorted
        '''
        self.maximum_depth = 0
        self.counter = 0
        self.unsorted_array = array.copy()
        self.sorted_array = array.copy()
        self.recursive_merge_sort(self.sorted_array)

    def setMaximumDepth(self, depth):
        '''
        This method sets the maximum depth of the merge sort

        Parameters: 
            depth : int 
                The depth to be set if it is larger than the current maximum depth
        '''
        if depth > self.maximum_depth:
            self.maximum_depth = depth

    def getMaximumDepth(self): 
        return self.maximum_depth
    
    def getCounter(self):
        return self.counter
    
    def getUnsortedArray(self):
        return self.unsorted_array

    def getSortedArray(self):
        return self.sorted_array
    
    def swap(self,array, index_a, index_b):
        '''
        This method swaps two items in the list

        Parameters :
            array : [int]
                The array that the items are in
            index_a : int 
                The index of one of the items to be swapped
            index_b : int
                The index of the other item to be swapped
        '''

        # assumes both index values are positive and not out of bound of the array
        # arr(a) = arr[b] and arr(b) = arr[a]
        (array[index_a], array[index_b]) = (array[index_b], array[index_a])

    def update_original_list(self, merge_result, original_array, left_index, right_index):
        '''
        This method puts the result of merging back into the original list

        Parameters :
            merge_results : [int]
                The result of the merge operation
            original_array : [int]
                The original array
            left_index : int
                The left index of the merge operations location in the original array
            right_index : int
                The right index of the merge operations location in the original array
        '''

        # Given a 10 item original array
        # [n, n+1, n+2, n+3, n+4, n+5, n+6, n+7, n+8, n+9]
        # And a 5 item merge_result
        #                         [a, a+1, a+2, a+3, a+4]
        # with a left index 5 and right index 9
        #
        # copy each it over such that
        # [n, n+1, n+2, n+3, n+4, a, a+1, a+2, a+3, a+4]
        for i in range(left_index, right_index+1):
            original_array[i] = merge_result[i - left_index]
        
    def mergeHelper(self, array, left_index, middle_index, right_index):
        '''
        This method merges two sorted sub arrays into a single sorted array 

        Parameters:
            array : [int]
                The entire array that is being sorted
            left_index : int
                The index of the left most position in the sub array
            middle_index : int
                The index of the last positionn in the left sub array and one before the first position of the right sub array
            right_index : int 
                The index of the right most position in the sub array
        '''

        # Perform a merge on sublists lst[left:mid+1] and lst[mid+1:right+1]
        # This is the same algorithm as merge above but we will need to copy
        # things back to the original list.

        # if either sublist is empty it leaves the method
        if left_index > middle_index or middle_index > right_index:
            return
        
        # The indexes for the start of both sub arrays being merged
        first_start = left_index
        second_start = middle_index + 1

        merged_sorted_array = []

        # The loop runs while there are items in either of the sublists being merged
        while (first_start <= middle_index or second_start <= right_index):

            # Adds the smallest item in either sub array to the merged sorted array
            # moves where the sub array starts
            #
            # 9 , 8 , 6 , 5 , [ 3 , 4 ] [ 1 , 2 ] -> []
            # 9 , 8 , 6 , 5 , [ 3 , 4 ] , 1 [ 2 ] -> [ 1 ]
            # 9 , 8 , 6 , 5 , [ 3 , 4 ] , 1 , 2   -> [ 1 , 2 ]
            # 9 , 8 , 6 , 5 ,   3 [ 4 ] , 1 , 2   -> [ 1 , 2 , 3 ]
            # 9 , 8 , 6 , 5 ,   3 , 4   , 1 , 2   -> [ 1 , 2 , 3 , 4]
            if (first_start <= middle_index and second_start <= right_index):
                if array[first_start] <= array[second_start]:
                    merged_sorted_array.append(array[first_start])
                    first_start = first_start + 1
                else:
                    merged_sorted_array.append(array[second_start])
                    second_start = second_start + 1
            elif first_start <= middle_index:
                merged_sorted_array.append(array[first_start])
                first_start = first_start + 1
            else:
                merged_sorted_array.append(array[second_start])
                second_start = second_start + 1

        # Add the sorted merged sub array back into its original position in the array
        # 9 , 8 , 6 , 5 , 3 , 4 , 1 , 2   -> [ 1 , 2 , 3 , 4]
        # 9 , 8 , 6 , 5 , 1 , 2 , 3 , 4
        self.update_original_list(merged_sorted_array, array, left_index, right_index)
        return

    def recursive_merge_sort_helper(self,array, left_index, right_index, local_depth):
        '''
        This method is the recursive component of the merge sort implementation

        Parameters: 
            array : [int]
                The array that the merge sort algorithm is sorting
            left_index : int
                The index of the left side ofthe current area being sorted
            right_index : int 
                The index of the right side of the current area being sorted
        '''
        local_depth +=1
        self.setMaximumDepth(local_depth)
        self.counter += 1

        # This would mean the area being sorted only has one item and therefore must already be sorted
        # This would end the recursion
        if (left_index == right_index):
            return
        
        # This would mean the area being sorted only has two item
        # It can therefore be sorted by simply comparing the items and swapping if necessary
        # This would end the recursion
        elif (left_index + 1 == right_index):
            if (array[left_index] > array[right_index]):
                self.swap(array, left_index, right_index)

        # This splits the area to sort into half
        # and then calls the recursive method for merge sort on each side 
        # before recombining the smaller areas once they are sorted
        #
        # [4 , 3 , 2 , 1]
        # [4 , 3] [2 , 1]
        # [3 , 4] [1 , 2]
        # [1 , 2 , 3 , 4]
        else:
            mid = (left_index + right_index ) // 2 

            self.recursive_merge_sort_helper(array, left_index, mid, local_depth)
            self.recursive_merge_sort_helper(array, mid + 1 , right_index, local_depth) 
            self.mergeHelper(array, left_index, mid, right_index)

    def recursive_merge_sort(self,array):
        '''
        This method begins the mergesort of the array. It has no return value
        '''

        local_depth = 0
        self.counter = 0

        if len(array) <= 1:
            return
        else:
            self.recursive_merge_sort_helper(array, 0, len(array)-1, local_depth)

if __name__ == '__main__':
    initial_array_length = 2
    array_length_multiplier = 2
    number_to_sort = 20

    array_lengths = []
    recursive_calls = []
    maximum_depths = []

    # sorts number_to_sort random arrays with array_length elements
    for i in range(0,number_to_sort):
        array_length = initial_array_length * array_length_multiplier ** i
        unsorted_random_array = GenerateArrays.generate_random_array(array_length,0,array_length*2)
        mergesort = MergeSort(unsorted_random_array)

        print(f"The array with length {array_length} was sorted at a maximum recursive depth of {mergesort.getMaximumDepth()} with {mergesort.getCounter()} calls to the recursive method")
        array_lengths.append(array_length)
        recursive_calls.append(mergesort.getCounter())
        maximum_depths.append(mergesort.getMaximumDepth())

    dictionary = {
        "Array Length": array_lengths,
        "Recursive Depth": maximum_depths,
        "Recursive Calls": recursive_calls
    }

    dataframe = pd.DataFrame.from_dict(dictionary)
    fig, axes = plt.subplots(ncols=2, sharey=False)
    fig.set_figwidth(10)
    bright_palette = palette=sns.hls_palette(h=.5)
    sns.set_theme(style="whitegrid", palette=bright_palette)
    sns.lineplot(data=dataframe, x="Array Length", y="Recursive Depth", ax=axes[0], color=bright_palette[0])
    sns.scatterplot(data=dataframe, x="Array Length", y="Recursive Depth", ax=axes[0], color=bright_palette[1])
    sns.lineplot(data=dataframe, x="Array Length", y="Recursive Calls", ax=axes[1], color=bright_palette[0])
    sns.scatterplot(data=dataframe, x="Array Length", y="Recursive Calls", ax=axes[1], color=bright_palette[1])

    fig.canvas.manager.set_window_title('Recursive Merge Sort By Array Length')

    plt.tight_layout()
    plt.show()
    