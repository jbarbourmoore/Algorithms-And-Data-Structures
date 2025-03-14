import HelperClasses.GenerateArrays as genArrays
from statistics import mean

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
        
        # if the item_searched is larger than the item at the middle index
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
    
def output_search_results(item_searched, item_found_index, counter):
    print(f"The item, {item_searched}, was found at index {item_found_index}")
    print(f"The counter value was {counter}")
    print("------------------------------\n")

if __name__ == '__main__':
    # Searches for a known existing item in multiple arrays
    array_length = 1000000
    number_to_search = 100
    counter_results = []

    for _ in range(0,number_to_search):
        random_array = genArrays.generate_random_array(array_length,0,array_length*2)

        # guarantees the item is in the arrau with an unknown index when the search is ran as the array is not yet sorted
        item_searched = random_array[0]

        random_array.sort()
        
        item_found_index, counter = recursiveBinarySearch(random_array,item_searched)

        counter_results.append(counter)
        output_search_results(item_searched, item_found_index, counter)

    asc_sorted = []
    for i in range(0,array_length):
        asc_sorted.append(i)
    asc_sorted.sort()

    print("Searching for middle item")
    item_searched = (0 + array_length-1)//2
    item_found_index, counter = recursiveBinarySearch(asc_sorted,item_searched)
    output_search_results(item_searched, item_found_index, counter)
    print("Searching for item outside array range")
    item_searched = -1
    item_found_index, counter = recursiveBinarySearch(asc_sorted,item_searched)
    output_search_results(item_searched, item_found_index, counter)
    print("Searching for item not in array")
    item_searched = 15
    asc_sorted.remove(item_searched)
    item_found_index, counter = recursiveBinarySearch(asc_sorted,item_searched)
    output_search_results(item_searched, item_found_index, counter)



    print(f"Maximum Observed Counter  : {max(counter_results)}")
    print(f"Minimum Observed Counter  : {min(counter_results)}")
    print(f"Average Observed Counter  : {mean(counter_results):.1f}")