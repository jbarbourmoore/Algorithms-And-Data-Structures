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

### Hash Table   

A basic implementation of a hash table data structure. It manages collisions by increasing the hash table's number of rows by a certain factor (default is two) whenever the hash table's load factor is larger than a given value (default is .5) and rehashing and inserting the items in the new hash table.

#### Hash Table Expansion Example   

##### Starting Hash Table with a load factor of .5 (the default maximum)   

| Row | Items |
|--------| ---- |
| 1 |   |
| 2 |  1 , "Item 3"  |
| 3 |    |
| 4 | "two" |

##### Adding an extra item which pushes the load factor over the default maximum   

| Row | Items |
|--------| ---- |
| 1 |   |
| 2 |  1 , "Item 3"  |
| 3 |    |
| 4 | "two" |

##### Resulting table expanded by a factor of 2 (the default value)     

| Row | Items |
|--------| ---- |
| 1 |  "Item 3 |
| 2 |    |
| 3 |    |
| 4 |    |
| 5 | 1 |
| 6 |    |
| 7 | "two" |
| 8 |     |   

### Binary Search Tree    

The binary search tree itself does not store much information. It holds one binary search tree node, or the "root". Each Binary Search Node contains the information for its own value as well as it's right and left children. All left children must be smaller than their parent and all right node children must be larger than their parent. This allows an item to be located in the binary search tree by comparing it to a node and then choosing whether to continue to the left child or the right child for further comparions.   

### Graph   

The graph data structure is defined using nodes and edges with multiple Boolean parameters to allow each graph object to be constructed for a specific purpose or algorithm. (Definitely not an efficient implementation of a graph, simply interesting to play with in this case)   

#### Directed or Undirected Edges    

The is_directed Boolean determines whether the edges in a graph strictly travel from the start node to the end node or if they are reversable.   

#### Breadth or Depth First Traversal   

The is_breadth Boolean determines whether the traversal methods will run breadth first (visiting each descendant of a node before visiting the descendants' descendants) or depth first (visiting the first descendant of the node and each first descendant of that node until there are no further descendants before visiting the other descendants of the node and repeating)    

![Tables comparing the traversal results with directed or undirected edges and using breadth first traversal or depth first traversal. Directed edges cause the graph to not be a single connected entity and breadth first increases the number of nodes who have 0-2 as their parent.](https://github.com/jbarbourmoore/Algorithms-And-Data-Structures/blob/48fe4e511fcf3d83faa1bc48ddd7ff56d7dbc8ce/OutputImages/Graph_TraversalComparisons.png "Graph Traversal Comparisons")

#### Weighted or Unweighted Edges    

The is_weighted Boolean determines whether the edges in a graph are weighted. This weight data is used when calculating the shortest distance to each node and similar algorithms. Unweighted graphs default to each edge weighted 1 for the sake of the calculations.  

#### Dijkstra's Algorithm for Shortest Paths

The graph can use Dijkstra's Algorithm to find the shortest path between each of it's nodes depending on whether the graph is directed or un directed and whether the graph is weighted or unweighted. Unweighted graphs assume each edge has the same cost (default to one: so if a path takes 4 edges that would be a distance of four).   

Below are some graphics showing the shortest distances and shortest paths between each node in a given graph with that are weighted or unweighted and directed or undirected. Each column is labeled with the starting node index for a path and each row labeled with the ending node index for a path. Every location where the row and column are the same the distance should be 0 and the path should simply be that node. If there is no path between two nodes the distance should be indicated by NaN and the path by None.  

![Tables comparing the shortest distances between each node in the graph when it is weighted or unweighted and directed or undirected. Weighted causes many of the distances to increase and as does directed. Directed also decreases the number of nodes are accessible from which other nodes](https://github.com/jbarbourmoore/Algorithms-And-Data-Structures/blob/48fe4e511fcf3d83faa1bc48ddd7ff56d7dbc8ce/OutputImages/Graph_ShortestDistancesComparisons.png "Shortest Distances Comparisons")

![Tables comparing the shortest paths between each node in the graph when it is weighted or unweighted and directed or undirected. Weighted causes some of the paths to reroute to avoid particularly heavy or expensive routes. Directed  decreases the number of nodes are accessible from which other nodes, thereby changing the routing options.](https://github.com/jbarbourmoore/Algorithms-And-Data-Structures/blob/48fe4e511fcf3d83faa1bc48ddd7ff56d7dbc8ce/OutputImages/Graph_ShortestPathsComparisons.png "Shortest Paths Comparisons")

