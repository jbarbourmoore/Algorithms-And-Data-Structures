# Foundations of Algorithms and Data Structures
My code repository for following along with Foundations of Algorithms and Data Structures  

## Course Information
|          |            |
| -------- | ----------- |   
| School | University of Colorado Boulder  |   
| Location | Coursera  |   
| Professor | Sriram Sankaranarayanan  |   
| Textbook | Introduction To Algorithms by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein  |   

## Algorithms

### Sorting

#### Insertion Sort

Implemented a basic insertion sort in Python. It runs 1000 times with randomly 20 item array and produces a box plot with the distribution of how many times the Insertion sort iterated.  

![box plot of the distribution for the insertion sort algorithm](https://github.com/jbarbourmoore/Foundations_AlgosAndDataStructs/blob/fef0f1b8370cafb916fe3a5037ac62060ced7838/OutputImages/Insertion_Sort_Boxplot.png "Insertion Sort Box Plot")

#### Merge Sort

Implemented a basic merge sort using recursion. It runs 20 times with different length arrays. The array length starts at 4 items and increases by a multiple of 2 each time. It generates two plots. One compares the number of times the recursive method is called with the number of elements in the array. The other compares the maximum recursion depth with the number of items in the array.

![plots comparing the maximum recursion depth and the recursive method call count with the number of items. The maximum recursion depth may be logarithmic or similar and the recursive method calls appear linear.](https://github.com/jbarbourmoore/Foundations_AlgosAndDataStructs/blob/fef0f1b8370cafb916fe3a5037ac62060ced7838/OutputImages/Recursive_Merge_Sort_By_Array_Length.png "Recursive Merge Sort Plots")

#### Heap Sort   

Implemented a heap sort using the min heap data structure. It run 5 times each for 20 different array lengths. Each run it calculates the amount of time that the sort took in seconds and the number of swap opperations that were used. It generates two plots comparing the number of elements with the swap operation count and the run time.   

![plots comparing the number of elements in the arrays being sorted with the number of swap times and the amount of time the sort took. Both appear to be resonably linear.](https://github.com/jbarbourmoore/Algorithms-And-Data-Structures/blob/455a213ce432ab83d1c4301ff848851bd379490f/OutputImages/Heap_Sort_By_Array_Length.png "Heap Sort")

#### Quick Sort   

Implemented a quick sort algorithm that relies on recursion. It run 5 times each for 205 different array lengths. Each run it calculates the amount of time that the sort took in seconds and the number of calls to the recursive method, the max recursive depth and the quantity of loop iterations. It generates 4 plots comparing each statistic with the array length.

![plots comparing the number of elements in the arrays being sorted with the maximum array depth, the recursive calls, the quantity of loop iterations. Other than the max recursive depth which looks along the lines of logarithmic, the others appear near linear.](https://github.com/jbarbourmoore/Algorithms-And-Data-Structures/blob/c8489f2ec63e4eb019621d54eb827794f9cb0d5e/OutputImages/Recursive_Quick_Sort_By_Array_Length.png "Quick Sort")

### Searching

#### Binary Search

Implemented two basic binary search algorithms. One uses recursion and the other relies on loops. Both have counters for how many times the loop is run / the recursive method is called. They are both run against the same 1000 random arrays with 10000 elements. It outputs for graphs comparing the counters for both implementation which do seem to match.

![plots comparing the distribution of both binary search implementations showing that they match](https://github.com/jbarbourmoore/Foundations_AlgosAndDataStructs/blob/fef0f1b8370cafb916fe3a5037ac62060ced7838/OutputImages/Binary_Search_Counter_Distributions_By_Algorithm_Type.png "Binary Search Algorithms Comparison")

## Data Structures   

### Dynamic Array

This is an approximation of a dynamic array implementation. It has methods to add items both to the front and the back of the dynamic array, showing their difference in complexity. It also has two methods to delete an item from the dynamic array. One ignores the array's order and run in constant time while the other preserves the array's order and will run in a worst case O(n).   

### Min Heap   

The min heap is a heap data structure where each item must be smaller than it's child items. The heap root is the minimum item in the min heap. When the min heap is instantiated on an array, the heapify method uses bubble down on each of the items in the array in order to construct the appropriate order for a min heap. There are also methods for adding and deleting items from the min heap which preserve this structure.   

#### Example Min Heap 

Given an array : [48, 16, 49, 20, 51, 37, 33, 31, 44, 15, 52, 27, 42, 38, 31]

This min heap could be created:  
|    |    |   |   |   |    |    |   |   |    |   |    |   |   |   |   
|  ---  |  ---  |  --- | --- | ---  |   --- |   --- |  --- |  --- |   ---- |  --- | --- | ---  | ---  |  ---- |   
|    |    |   |   |   |    |    | 15 |   |    |   |    |   |   |   |   
|    |    |   |16 |   |    |    |   |   |    |   | 27 |   |   |   |      
|    | 20 |   |   |    | 48 |   |   |   | 37 |   |   |   | 31 |   |  
| 31 |   | 44 |   | 51 |   | 52 |   | 49 |   | 42 |   | 38 |   | 33 |   


The heap containing 15 elements has a depth of 4 and a root of 15.   
Each item's childrean are larger than the item itself and the smallest item is always at the root.   
