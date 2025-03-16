import time
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from HelperClasses import GenerateArrays

class QuickSort():
    '''
    This class initializes the quick sort object, runs the sorting algorithm and keeps track of related performance metrics
    '''

    def __init__(self, array):
        '''
        This method initializes the quick sort object

        It creates the metrics variables and calls the initial quick sort method

        Parameters :
            array : [int]
                The array to be sorted 
        '''

        self.unsorted_array = array
        self.sorted_array = array.copy()
        self.partition_counter = 0
        self.loop_counter = 0
        start_time = time.time()

        self.array_length = len(array)
        self.maximum_depth = 0

        if self.array_length > 1:
            self.quickSort(0, self.array_length-1,0)
        
        end_time = time.time()
        self.run_duration = end_time - start_time

    def setMaximumDepth(self, depth):
        '''
        This method sets the maximum depth of the quick sort

        Parameters: 
            depth : int 
                The depth to be set if it is larger than the current maximum depth
        '''
        if depth > self.maximum_depth:
            self.maximum_depth = depth

    def partition(self, left_index, right_index):
        '''
        This method partitions the array, placing values that are smaller or equal to the pivot value on the left side

        Parameters :
            left_index : int
                The left index of the area being partitioned
            right_index : int 
                The right index of the area being partitioned
        '''

        pivot_value = self.sorted_array[right_index]
        self.partition_counter += 1
        partition_index = left_index

        for i in range(left_index, right_index):
            self.loop_counter += 1
            if self.sorted_array[i] <= pivot_value:

                (self.sorted_array[partition_index], self.sorted_array[i]) = (self.sorted_array[i], self.sorted_array[partition_index])
                
                partition_index += 1


        (self.sorted_array[partition_index], self.sorted_array[right_index]) = (self.sorted_array[right_index], self.sorted_array[partition_index])

        return partition_index

    def quickSort(self, left_index, right_index, recursive_depth):
        '''
        This is the recursive method which runs the quick sort
        It works on divide and concur, calling itself on both sides of a partition value in order to sort the entire array

        Parameters :
            left_index : int
                The left index of the area being partitioned
            right_index : int 
                The right index of the area being partitioned
            recursive_depth : int
                The current recursive depth of this array partition
        '''

        recursive_depth += 1
        self.setMaximumDepth(recursive_depth)

        if left_index < right_index:
            partition_index = self.partition(left_index, right_index)
            self.quickSort(left_index, partition_index - 1, recursive_depth=recursive_depth)
            self.quickSort(partition_index + 1, right_index, recursive_depth=recursive_depth)

    def printArrays(self):
        print("The Unsorted Array: ")
        print(self.unsorted_array)
        print("The Sorted Array: ")
        print(self.sorted_array)

    def printDetails(self):
        print(f"The array of length {self.array_length} was sorted in {self.partition_counter} partitions, {self.loop_counter} loop iterations, {self.maximum_depth} maximum recursive depth and {self.run_duration:.2f} seconds")



if __name__ == '__main__':
    initial_array_length = 2
    array_length_multiplier = 2
    number_to_sort = 25

    array_lengths = []
    partition_counters = []
    loop_interations = []
    time_durations = []
    maximum_depths = []

    for _ in range(5):
    # sorts number_to_sort random arrays with array_length elements
        for i in range(0,number_to_sort):
            array_length = initial_array_length * array_length_multiplier ** i
            unsorted_random_array = GenerateArrays.generate_random_array(array_length,0,array_length*2)
            quicksort = QuickSort(unsorted_random_array)

            # quicksort.printArrays()
            quicksort.printDetails()

            array_lengths.append(array_length)
            partition_counters.append(quicksort.partition_counter)
            loop_interations.append(quicksort.loop_counter)
            time_durations.append(quicksort.run_duration)
            maximum_depths.append(quicksort.maximum_depth)

    dictionary = {
        "Array Length": array_lengths,
        "Recursive Depth": maximum_depths,
        "Partition Count": partition_counters,
        "Loop Iterations": loop_interations,
        "Duration in Seconds": time_durations
    }

    dataframe = pd.DataFrame.from_dict(dictionary)
    fig, axes = plt.subplots(nrows=2, ncols=2, sharey=False)
    fig.set_figwidth(10)
    bright_palette = palette=sns.hls_palette(h=.5)
    sns.set_theme(style="whitegrid", palette=bright_palette)
    sns.lineplot(data=dataframe, x="Array Length", y="Recursive Depth", ax=axes[0,0], color=bright_palette[0])
    sns.scatterplot(data=dataframe, x="Array Length", y="Recursive Depth", ax=axes[0,0], color=bright_palette[1])
    sns.lineplot(data=dataframe, x="Array Length", y="Partition Count", ax=axes[0,1], color=bright_palette[0])
    sns.scatterplot(data=dataframe, x="Array Length", y="Partition Count", ax=axes[0,1], color=bright_palette[1])
    sns.lineplot(data=dataframe, x="Array Length", y="Loop Iterations", ax=axes[1,0], color=bright_palette[0])
    sns.scatterplot(data=dataframe, x="Array Length", y="Loop Iterations", ax=axes[1,0], color=bright_palette[1])
    sns.lineplot(data=dataframe, x="Array Length", y="Duration in Seconds", ax=axes[1,1], color=bright_palette[0])
    sns.scatterplot(data=dataframe, x="Array Length", y="Duration in Seconds", ax=axes[1,1], color=bright_palette[1])

    fig.canvas.manager.set_window_title('Recursive Quick Sort By Array Length')

    plt.tight_layout()
    plt.show()