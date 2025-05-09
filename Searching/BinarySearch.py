import HelperClasses.GenerateArrays as genArrays
from statistics import mean
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Important Note :
# Binary Search REQUIRES a SORTED list

def recursiveBinarySearchHelper(array, item_searched, left_index, right_index,counter):
    '''
    This is a recursive function that seaches for an item in an array using binary search

    When it is called we know:
    - the array is already sorted 
    - the item_searched is not smaller than the smallest item in the search area
    - the item_searched in not bigger than the largest item in the search area

    Parameters :
        array : [int]
            The array of items we are searching in
        item_searched : int 
            The item we are searching for
        left_index : int 
            The index of the smallest item in the search zone
        right_index : int
            The index of the largest item in the search zone

    Returns
        search result : None or int
            This returns the index of the item being searched if it is in the array or None if the item is not found
    '''

    # if the left and right indexes have crossed over we can say the item is not in the array
    # returns None and ends the recursion
    if (left_index > right_index):
        return None, counter
    
    else:
        # uses integer division to find the index of the center element of the current search area
        #
        # [n-10, n-9, n-8, n-7, n-6, n-5, n-4, n-3, n-2, n-1, !n!, n+1, n+2, n+3, n+4, n+5, n+6, n+7, n+8, n+9, n+10]  
        # [n-10, n-9, n-8, n-7, !n-6! n-5, n-4, n-3, n-2, n-1] !n!, n+1, n+2, n+3, n+4, n+5, n+6, n+7, n+8, n+9, n+10
        # n-10, n-9, n-8, n-7, !n-6! [n-5, n-4, !n-3! n-2, n-1] !n!, n+1, n+2, n+3, n+4, n+5, n+6, n+7, n+8, n+9, n+10
        middle_index = (left_index + right_index)//2 

        # checks if the center point of the current search area is the item_searched
        # returns the index number and end the recursion
        if array[middle_index] == item_searched:
            return middle_index, counter
        
        # checks in the item_searched is larger than the item at the middle index
        # calls recursiveBinarySearchHelper on a smaller search area 
        # this area contains the half the items of the current search area to the right of the middle index
        #
        # [n-10, n-9, n-8, n-7, !n-6! n-5, n-4, n-3, n-2, n-1]
        # n-10, n-9, n-8, n-7, !n-6! [n-5, n-4, n-3, n-2, n-1]
        elif array[middle_index] < item_searched:
            return recursiveBinarySearchHelper(array, item_searched, middle_index+1, right_index,counter+1)
        
        # if the item_searched is smaller than the item at the middle index
        # calls recursiveBinarySearchHelper on a smaller search area 
        # this area contains the half the items of the current search area to the left of the middle index
        #
        # [n-10, n-9, n-8, n-7, !n-6! n-5, n-4, n-3, n-2, n-1]
        # [n-10, n-9, n-8, n-7] !n-6! n-5, n-4, n-3, n-2, n-1
        else: 
            return recursiveBinarySearchHelper(array, item_searched, left_index, middle_index-1,counter+1)
        
def recursiveBinarySearch(array, item_searched):
    '''
    This function seaches for an item in an array using a recursive binary search algorithm

    It calls recursiveBinarySearchHelper which actually implements the recursive element to the algorithm

    Parameters :
        array : [int]
            The array of items we are searching in
        item_searched : int 
            The item we are searching for

    Returns
        search result : None or int
            This returns the index of the item being searched if it is in the array or None if the item is not found
        counter : int
            This returns the number of times the recursive method was called
    '''

    array_length = len(array)

    # As the array needs to be sorted prior to using binary search:
    #
    # If the item is less than the smallest array element we know it is not in the array
    # If the item is bigger than the largest array element we know it is not in the array
    #
    # !n-3! [n-2, n-1, n, n+1, n+2] !n+3!   
    if (item_searched < array[0] or item_searched > array[array_length-1]):
        return None,0
    else:
        return recursiveBinarySearchHelper(array, item_searched, 0, array_length-1,1)
    
def loop_based_binary_search(array, item_searched):
    '''
    This function seaches for an item in an array using a loop based binary search algorithm

    Parameters :
        array : [int]
            The array of items we are searching in
        item_searched : int 
            The item we are searching for

    Returns
        search result : None or int
            This returns the index of the item being searched if it is in the array or None if the item is not found
        counter : int
            This returns the number of times the loop was ran
    '''

    counter = 0

    array_length = len(array)

    # As the array needs to be sorted prior to using binary search:
    #
    # If the item is less than the smallest array element we know it is not in the array
    # If the item is bigger than the largest array element we know it is not in the array
    #
    # !n-3! [n-2, n-1, n, n+1, n+2] !n+3!   
    if (item_searched < array[0] or item_searched > array[array_length-1]):
        return None, counter
    
    else:
        left_index = 0
        right_index = array_length - 1

        # if the left and right indexes have crossed over or met without finding the item
        # we can say the item is not in the array
        while (left_index <= right_index):
            counter += 1

            # uses integer division to find the index of the center element of the current search area
            #
            # [n-10, n-9, n-8, n-7, n-6, n-5, n-4, n-3, n-2, n-1, !n!, n+1, n+2, n+3, n+4, n+5, n+6, n+7, n+8, n+9, n+10]  
            # [n-10, n-9, n-8, n-7, !n-6! n-5, n-4, n-3, n-2, n-1] !n!, n+1, n+2, n+3, n+4, n+5, n+6, n+7, n+8, n+9, n+10
            # n-10, n-9, n-8, n-7, !n-6! [n-5, n-4, !n-3! n-2, n-1] !n!, n+1, n+2, n+3, n+4, n+5, n+6, n+7, n+8, n+9, n+10
            middle_index = (left_index + right_index)//2

            # checks if the center point of the current search area is the item_searched
            # returns the index number and ends the loop
            if array[middle_index] == item_searched:
                return middle_index, counter
            
            # checks in the item_searched is larger than the item at the middle index
            # moves the left index so the next loop iteration runs on a smaller search area 
            # this area contains the half the items of the current search area to the right of the middle index
            #
            # [n-10, n-9, n-8, n-7, !n-6! n-5, n-4, n-3, n-2, n-1]
            # n-10, n-9, n-8, n-7, !n-6! [n-5, n-4, n-3, n-2, n-1]
            elif array[middle_index] < item_searched:
                left_index = middle_index + 1

            # if the item_searched is smaller than the item at the middle index
            # moved the right index so the next loop iteration run on a smaller search area 
            # this area contains the half the items of the current search area to the left of the middle index
            #
            # [n-10, n-9, n-8, n-7, !n-6! n-5, n-4, n-3, n-2, n-1]
            # [n-10, n-9, n-8, n-7] !n-6! n-5, n-4, n-3, n-2, n-1
            else: 
                right_index = middle_index - 1
        
        # the item was not found in the loop before there were no more items left to search
        return None, counter

def output_search_results(item_searched, item_found_index, counter):
    print(f"The item, {item_searched}, was found at index {item_found_index}")
    print(f"The counter value was {counter}")
    print("------------------------------\n")

def test_binary_search_method(binarySearchFunction, output_search_results, array_length, number_to_search):
    counter_results = []

    for _ in range(0,number_to_search):
        random_array = genArrays.generate_random_array(array_length,0,array_length*2)

        # guarantees the item is in the arrau with an unknown index when the search is ran as the array is not yet sorted
        item_searched = random_array[0]

        random_array.sort()
        
        item_found_index, counter = binarySearchFunction(random_array,item_searched)

        counter_results.append(counter)
        # output_search_results(item_searched, item_found_index, counter)

    asc_sorted = []
    for i in range(0,array_length):
        asc_sorted.append(i)
    asc_sorted.sort()

    # print("Searching for middle item")
    item_searched = (0 + array_length-1)//2
    item_found_index, counter = binarySearchFunction(asc_sorted,item_searched)
    # output_search_results(item_searched, item_found_index, counter)
    center_item_counter = counter
    # print("Searching for item outside array range")
    item_searched = -1
    item_found_index, counter = binarySearchFunction(asc_sorted,item_searched)
    # output_search_results(item_searched, item_found_index, counter)
    not_in_range_counter = counter
    # print("Searching for item not in array")
    item_searched = 15
    asc_sorted.remove(item_searched)
    asc_sorted.append(array_length)
    item_found_index, counter = binarySearchFunction(asc_sorted,item_searched)
    # output_search_results(item_searched, item_found_index, counter)
    not_in_array_counter = counter

    print("Results")
    print(f"Array Length              : {array_length}")
    print(f"Number of Searches        : {number_to_search}")

    print("------------------------------\n")

    print(f"Middle Item Counter       : {center_item_counter}")
    print(f"Not in range Counter      : {not_in_range_counter}")
    print(f"Not in array Counter      : {not_in_array_counter}")

    print("------------------------------\n")

    print(f"Maximum Observed Counter  : {max(counter_results)}")
    print(f"Minimum Observed Counter  : {min(counter_results)}")
    print(f"Average Observed Counter  : {mean(counter_results):.1f}")

    return counter_results

def test_binary_search_consistent_arrays(binarySearchFunction, search_dictionary, array_length, number_to_search):
    '''
    This function runs the selected binary search function against a pre defined selection of random arrays

    Parameters :
        binarySearchFunction : function()
            The implementation of binary search to use
        search_dictionary : {int : ([int],int)}
            The dictionary containing touples with the array to search and the value to search for
        array_length : int
            The length of the arrays that are being searched
        number_to_search : int 
            The quantity of arrays being searched

    Returns :
        counter_results : [int]
            A list containing how many iterations each search took
    '''
    
    counter_results = []

    for index, value in search_dictionary.items():
        array, item_searched = value 
        _, counter = binarySearchFunction(array,item_searched)
        _, counter = binarySearchFunction(array,item_searched)

        counter_results.append(counter)
        # output_search_results(item_searched, item_found_index, counter)

    print("Results")
    print(f"Array Length              : {array_length}")
    print(f"Number of Searches        : {number_to_search}")

    print("------------------------------\n")

    print(f"Maximum Observed Counter  : {max(counter_results)}")
    print(f"Minimum Observed Counter  : {min(counter_results)}")
    print(f"Average Observed Counter  : {mean(counter_results):.1f}")

    return counter_results

if __name__ == '__main__':
    # Searches for a known existing item in multiple arrays
    array_length = 10000
    number_to_search = 1000

    # creates a dictionary of random arrays for both binary search implementations to use
    search_dictionary = genArrays.generateRandomSortedSearchArrays(array_length, number_to_search)

    print("Testing recursive binary search:\n")
    recursive_binary_search_counters = test_binary_search_consistent_arrays(recursiveBinarySearch, search_dictionary, array_length, number_to_search)
    print("\n-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n")
    print("Testing loop based binary search:\n")
    loop_binary_search_counters = test_binary_search_consistent_arrays(loop_based_binary_search, search_dictionary, array_length, number_to_search)

    dictionary = {
        "Recursive": recursive_binary_search_counters,
        "Loop Based":loop_binary_search_counters
    }

    dataframe = pd.DataFrame.from_dict(dictionary)
    fig, axes = plt.subplots(nrows=2, ncols=2, sharey=False)

    bright_palette = palette=sns.hls_palette(h=.5)[0:2]
    sns.set_theme(style="whitegrid", palette=bright_palette)
    sns.boxplot(dataframe, ax=axes[0,0], palette=bright_palette)
    sns.stripplot(data=dataframe, ax=axes[0,1], palette=bright_palette)
    sns.histplot(dataframe["Recursive"],ax=axes[1,0], color=bright_palette[0])
    sns.histplot(dataframe["Loop Based"], ax=axes[1,1], color=bright_palette[1])

    axes[0,0].set_xlabel("Implementation")
    axes[0,0].set_ylabel("Counter Value")
    fig.canvas.manager.set_window_title('Binary Search Counter Distributions By Algorithm Type')

    plt.tight_layout()
    plt.show()