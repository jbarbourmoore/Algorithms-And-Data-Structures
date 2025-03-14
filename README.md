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

### Searching

#### Binary Search

Implemented two basic binary search algorithms. One uses recursion and the other relies on loops. Both have counters for how many times the loop is run / the recursive method is called. They are both run against the same 1000 random arrays with 10000 elements. It outputs for graphs comparing the counters for both implementation which do seem to match.

![plots comparing the distribution of both binary search implementations showing that they match](https://github.com/jbarbourmoore/Foundations_AlgosAndDataStructs/blob/fef0f1b8370cafb916fe3a5037ac62060ced7838/OutputImages/Binary_Search_Counter_Distributions_By_Algorithm_Type.png "Binary Search Algorithms Comparison")

