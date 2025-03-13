# import HelperClasses.GenerateArrays as genArrays
from statistics import mean
import HelperClasses.GenerateArrays as genArrays

def insertionSort(array):
    '''
    Sorts an array using the insertion sort method

    Parameters : 
        array : [int]
            The array to be sorted

    Returns :
        array_length : int
            The length of the array being sorted
        number_shifts : int
            How many times numbers were swapped in order to sort the array
        total_iterations : int 
            How many times the algorithm went through one of the loops
        maximum_iterations : int
            How many times the algorithm could have gone through one of the loops
    '''
    
    array_length = len(array)
    number_shifts = 0
    total_iterations = 0
    maximum_iterations = 0

    # any array with only one (or no) item is already sorted
    if array_length <= 1:
        return number_shifts
    
    # loop through the items in the array
    # start from the second item as the first is already "sorted" with regards to itself
    # sorted  unsorted
    # [0] i [i+1,i+2,...,n]
    for i in range(1, array_length):
        sub_iterations = 0

        # the item in position i is to be inserted into the presorted section of the array
        # the presorted section of the array is those up to index i
        #
        #  sorted            unsorted
        # [0,1,2,...,i-2,i-1] i [i+1,...,n]
        to_be_inserted = array[i]
        last_sorted_element = i-1

        # moves any item larger than the value to be inserted in the pre sorted section of the array to the right
        # creating room for the value to be insert
        #
        #
        #  sorted            unsorted
        # [0,1,2,...,i-2, BLANK,i-1] [i+1,...,n]
        # (BLANK is still technically i-1 in the array above but that isn't relevant to this process)
        while last_sorted_element >= 0 and to_be_inserted < array[last_sorted_element]:
            number_shifts = number_shifts + 1
            sub_iterations = sub_iterations + 1
            array[last_sorted_element+1] = array[last_sorted_element] 
            last_sorted_element -= 1

        # item is then inserted in its appropriate location in the pre sorted array
        # the pre sorted array is now one item longer than it was before
        #
        #  sorted            unsorted
        # [0,1,2,...,i-2,i-1,i] [i+1,...,n]
        array[last_sorted_element+1] = to_be_inserted

        if sub_iterations == 0:
            sub_iterations = 1
        total_iterations += sub_iterations
        maximum_iterations += i

    return array_length, number_shifts, total_iterations, maximum_iterations

def output_results(unsorted_random_array, sorted_random_array, number_shifts, total_iterations, maximum_iterations):
    '''
    Outputs the results of the sorting algorithm to the console

    Parameters :
        unsorted_random_array : [int]
            The array before it was sorted
        sorted_random_array : [int]
            The array after it was sorted
        number_shifts : int
            How many times numbers were swapped in order to sort the array
        total_iterations : int 
            How many times the algorithm went through one of the loops
        maximum_iterations : int
            How many times the algorithm could have gone through one of the loops
    '''
    print(f"Unsorted array : {unsorted_random_array}")
    print(f"Sorted array   : {sorted_random_array}")
    print(f"Item Swaps     : {number_shifts}")
    print(f"Iterations     : {total_iterations}")
    print(f"Max Iterations : {maximum_iterations}")

    print("\n---------------------\n")

def test_insertion_sort(array_length = 20, number_to_sort = 10):
    '''
    This function runs the insertion sort for number_to_sort random arrays of array_length

    It also runs a pre sorted array of the same length and a reverse sorted array of the same length at the end

    Parameters :
        array_length : int, optional
            The length of the random arrays to be tested
        number_to_sort : int, optional
            The quantity of the random arrays to be tested
    '''
    iteration_counts = []

# sorts number_to_sort random arrays with array_length elements
    for i in range(0,number_to_sort):
        unsorted_random_array = genArrays.generate_random_array(array_length,0,array_length*2)
        sorted_random_array = unsorted_random_array.copy()
        array_length, number_shifts, total_iterations, maximum_iterations = insertionSort(sorted_random_array)

        iteration_counts.append(total_iterations)

        output_results(unsorted_random_array, sorted_random_array, number_shifts, total_iterations,maximum_iterations)

    print("\nSorting a presorted array")
    asc_sorted = []
    desc_sorted = []
    for i in range(0,array_length):
        asc_sorted.append(i)
        desc_sorted.append(array_length-i-1)
    array_length, number_shifts, total_iterations, maximum_iterations = insertionSort(asc_sorted)
    output_results(asc_sorted, asc_sorted, number_shifts, total_iterations,maximum_iterations)
    print("Sorting a reverse sorted array")
    desc_sorted_asc = desc_sorted.copy()
    array_length, number_shifts, total_iterations, maximum_iterations = insertionSort(desc_sorted_asc)
    output_results(desc_sorted, desc_sorted_asc, number_shifts, total_iterations,maximum_iterations)
    
    print(f"Maximum possible iterations  : {maximum_iterations}")
    print(f"Maximum observed iterations  : {max(iteration_counts)}")
    print(f"Average observed iterations  : {mean(iteration_counts)}")

array_length = 20
number_to_sort = 100000
test_insertion_sort(array_length, number_to_sort)


