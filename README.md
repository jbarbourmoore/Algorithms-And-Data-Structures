# Foundations of Algorithms and Data Structures
My code repository for following along with Foundations of Algorithms and Data Structures  

## Course Information
|          |            |
| -------- | ----------- |   
| School | University of Colorado Boulder  |   
| Location | Coursera  |   
| Professor | Sriram Sankaranarayanan  |   
| Textbook | Introduction To Algorithms by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein  |   

### Specialization Certificate

![The pdf certificate for the Foundations of Algorithms and Data Structures Specialization for University of Colorado Boulder on Coursera. It was a five course series consisting of "Algorithms for Searching, Sorting and Indexing", "Graphs and Trees: Basics", "Dynamic Programming, Greedy Algorithms", "Approximation Algorithms, and Linear Programming" and "Advanced Data Structures, RSA and Quantum Algorithms"](https://github.com/jbarbourmoore/Algorithms-And-Data-Structures/blob/0ce320cf8e3a047ec7c134c89b62f4a1d45ce905/OutputImages/CourseraCertificationPDFs/Specialization_DataStructuresAndAlgorithmsCert_ImageForReadMe.png "Coursera Certificate for Foundations of Algorithms and Data Structures Specializtion")

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

### Other Algorithms

#### Karatsuba Multiplication

I implemented a verson of Karatsuba's multiplication algorithm for binary numbers. It is a divide and conquer method meant for multiplying large numbers.

#### Using Polynomial Multiplication Based on Fast Fourier Transforms

Using the Numpy implementation of fft and ifft I implemented a function for polynomial multiplication. I then used the polynomial multiplication to implement a more efficient way to determine if a list, c, includes a number that is the sum of any number in a second list, a, and any number in a third list, b. I also implemented a brute force function with this same capability. I was then able to run both functions on random arrays with increasing complexity where the result was both true and false. I used seaborn and matplot lib to generate graphs demonstrating the time it took for both functions to run on my computer. Despite knowing that the fft polynomial multiplication based method should be more efficient I am still quite surprised by how evident that efficiency seems in the data I collected.

![plots showing the difference in duration between the fft polynomial implementation and the brute force implementation on arrays between length 50 and 1000. Although both implementations increase the fft appears more linear in comparison to the brute force which appears to be increasing exponentially. The brute force method also shows a large discrepency between best times and worse case times, as the arrays that did not include the sum are more consistent higher durations.](https://github.com/jbarbourmoore/Algorithms-And-Data-Structures/blob/b7853877e6471272faa2dbca257cb7a8039c073e/OutputImages/FFT_amd_Brute_Force_Durations_By_Array_Length.png "FFT Polynomial Multiplication vs. Brute Force Durations")

#### Factorial Algorithms (For Calculating Combinations and Permutations)   

I implemented a function to calculate the factorial of a number in 3 different ways. The first two are obvious, with a recursive algorithm and one based on loops. The third variant used the prime factors in order to find the factorial. While I believe that this one should be more efficient in the worst case scenario I have yet to see this characteristic in my experimentations. Of course, the recursive algorithm cannot actually be compared past calculating the factorial of about 1000 as it hits the maximum resursion depth on my computer. So the comparison graphs below are both interesting and not as complete as I was hoping.

![plots showing the duration of the factorial calculations for numbers up to 12000 both recursively and using prime factors. They both seem to shing a tendency towards exponential growth though the recursive durations seem to be consistently lower. The recursive durations are also shown up to 1000, which appears mostly linear, but as it is so restricted the appearance is unlikely to be much help.](https://github.com/jbarbourmoore/Algorithms-And-Data-Structures/blob/f430c4c5a1ba2ecdd2435ec41b08c8918b62ebed/OutputImages/Factorization_Durations_0_To_12000.png "Factorization Durations by Number")   

#### Finding the Longest Stable Subsequence Using Dynamic Programming    

I used dynamic programming algorithm in order to find the longest stable subsequence of a list. The longest stable subsequence was one where the values continued increasing and the values with no more than one apart from each other.

#### Transportation Optomization With Linear Programming

I used linear programming in order to find the best way to move items from starting locations to the destinations, assuming the best way was minimizing the distance the stuff was transported. This can be displayed using NetworkX simply to show how much weight was moved between each source node and each destination node.    

![Visualization of how much of the weight was moved from each starting point to each ending point](https://github.com/jbarbourmoore/Algorithms-And-Data-Structures/blob/708ede1d9ab4231a2e2469c1420da9fe5f81538c/OutputImages/TransportOptomization_VizualizedNodesAndWeight.png "Transportation Visualization by Weight")   

I also used linear programming to maximize the potential profits by setting the prices within specific parameters.

![This simply shows the starting locations, the destinations, how much to move and what to set the prices.](https://github.com/jbarbourmoore/Algorithms-And-Data-Structures/blob/708ede1d9ab4231a2e2469c1420da9fe5f81538c/OutputImages/TransportationOptomization_OutputData.png "Transportation Optomization Output")

#### Investment Optomization With Linear Programming    

I utilized linear programming in order to select the best stocks (from those passed into the class) to buy in order to acheive a balanced portfolio.   

![The break down of the stock data and how much would be optomal to buy within a certain budget](https://github.com/jbarbourmoore/Algorithms-And-Data-Structures/blob/708ede1d9ab4231a2e2469c1420da9fe5f81538c/OutputImages/InvestmentExample_ConsoleOutput.png "Investment Optomization")

#### Coloring Nodes With Binary Linear Programming

I used binary variable in linear programming in order to find the best way to color nodes so that each node is a different color from all of those touching it. The class works with an inputted number of number, list of edges and number of colors.

![This shows a small graph of four nodes. It uses 3 colors and none of the nodes are connected to a node of the same color.](https://github.com/jbarbourmoore/Algorithms-And-Data-Structures/blob/708ede1d9ab4231a2e2469c1420da9fe5f81538c/OutputImages/ColoringNode_3Colors4Nodes.png "Coloring 4 nodes with 3 colors")   

![This shows a larger graph of 10 nodes. It uses 4 colors and none of the nodes are connected to a node of the same color.](https://github.com/jbarbourmoore/Algorithms-And-Data-Structures/blob/708ede1d9ab4231a2e2469c1420da9fe5f81538c/OutputImages/ColoringNode_4Colors10Nodes.png "Coloring 10 Nodes with 4 Colors")

#### Max Cut Problem   

The idea here is to split a list of nodes into two sets such that each node has a connecting edges to a node in the opposite set. In order to do this I used a greedy algorithm to approximate the optimal solution. For this algorithm, the approximate solution should be between 1/2 of the optimal solution and the optimal solution.

![This shows 5 nodes that are connected to each other. 3 of the nodes are in set 1, and 2 are in set 2 so each node connects to at least one in the other set.](https://github.com/jbarbourmoore/Algorithms-And-Data-Structures/blob/c4f5b06be61f22a808243fdf2e5d405389175f60/OutputImages/MaxCutProblem_5Nodes.png "Max Cut Problem With 5 Nodes")

![This shows 20 nodes that are connected to each other. 9 of the nodes are in set 1, and 11 are in set 2, so each node connects to at least one in the other set.](https://github.com/jbarbourmoore/Algorithms-And-Data-Structures/blob/c4f5b06be61f22a808243fdf2e5d405389175f60/OutputImages/MaxCutProblem_20Nodes.png "Max Cut Problem With 20 Nodes")

#### Traveling Sales Person

I implemented a version of the traveling sales person problem using Linear Programming with multiple salespeople. The traveling sales person can be constrained by either a maximum number of salespeople or an exact number of salespeople

![This shows the traveling Salesperson with 5 nodes and 2 salespeople. When given the option of 1 or 2 salespeople the algorithm finds that a single salesperson is most efficient.](https://github.com/jbarbourmoore/Algorithms-And-Data-Structures/blob/9cb2661fefc269dfb15d973686b2cfc32f7102af/OutputImages/TSP_5Node2Salespeople.png "Traveling Sales Person with 5 Nodes")

![This shows the traveling salesperson problem with 8 nodes and 4 salespeople. When given the option of up to four salespeople the algorithm finds that 2 Salespeople is most efficient.](https://github.com/jbarbourmoore/Algorithms-And-Data-Structures/blob/9cb2661fefc269dfb15d973686b2cfc32f7102af/OutputImages/TSP_8Node4Salespeople.png "Traveling Sales Person with 8 Nodes")

#### RSA Encryption Scheme 

Utilized the extended form of Euclid's Algorithm in order to create an implementation along the lines of the RSA Encryption Scheme. It takes in two large prime numbers and generates both private and public encyption keys. Messages encrypted with the public key must be decrypted using the private key.    

![This shows the console output of the RSA Encryption scheme. It is ran on two different pairs of prime numbers, each generating their own sets of public and private key. When the input is encrypted using the public key of one of the pairs it can only be decrypted by the same pair's private key, or it outputs nonsense.](https://github.com/jbarbourmoore/Algorithms-And-Data-Structures/blob/f4f8ed6377a6dd1fc609e62824aab6e51fd3fba2/OutputImages/RSAEcryptionScheme_ConsoleOutput.png "Console Output of RSA Ecryption Scheme Results")

#### Grover's Quantum Search Algorithm   

Utilized Qiskit in order to implement Grover's Search Algorithm in Python. The implementation takes three qubits for the input, which can form 0-7, or not x_0 and not x_1 and not x_2 through x_0 and x_1 and x_2. Grover's algorithm can be executed a set number of times before reading the result, with the number of iterations affecting the accuracy. It runs extremely quickly and generates a batch of 1000 results which can be displayed as a histogram to show it's accuracy.   

![This shows four circuit diagrams for Grover's search for three, or more precisely, x_0 and x_1 and not x_2. The first diagram is with one iteration, the second shows two iterations, the third shows three iterations and the fouth shows ten iterations.](https://github.com/jbarbourmoore/Algorithms-And-Data-Structures/blob/main/OutputImages/GroverSearchAlgorithms_SearchFor3_CircuitDiagrams.png "Circuit Diagrams for Grover's Search Algorithm")

![This shows four circuit diagrams for Grover's search for three. The first histogram is with one iteration, and has roughly 80% accuracy, the second shows two iterations with roughly 97% accuracy, the third shows three iterations with roughly 35% accuracy, and the fouth shows ten iterations with roughly 96% accuracy.](https://github.com/jbarbourmoore/Algorithms-And-Data-Structures/blob/798666cde0566903f7ed1410d5a0032b1cab591e/OutputImages/GroverSearchAlgorithms_SearchFor3_Histograms.png "Histograms for Grover's Search Algorithm")

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

#### Visualizations of the Graphs

Shows one graph with unweighted and undirected edges as well as one graph with weighted and directed edges. Generated programmatically using NetworkX and MatPlotLib.    

![An unweighted and undirected graph with 10 nodes](https://github.com/jbarbourmoore/Algorithms-And-Data-Structures/blob/708ede1d9ab4231a2e2469c1420da9fe5f81538c/OutputImages/Graph_Visualized_UnweightedUndirected.png "Unweighted, Undirected Graph")

![A weighted and directed graph with 10 nodes](https://github.com/jbarbourmoore/Algorithms-And-Data-Structures/blob/main/OutputImages/Graph_Visualized_WeightedDirected.png "Weighted and Directed Graph")

#### Dijkstra's Algorithm for Shortest Paths

The graph can use Dijkstra's Algorithm to find the shortest path between each of it's nodes depending on whether the graph is directed or un directed and whether the graph is weighted or unweighted. Unweighted graphs assume each edge has the same cost (default to one: so if a path takes 4 edges that would be a distance of four).   

Below are some graphics showing the shortest distances and shortest paths between each node in a given graph with that are weighted or unweighted and directed or undirected. Each column is labeled with the starting node index for a path and each row labeled with the ending node index for a path. Every location where the row and column are the same the distance should be 0 and the path should simply be that node. If there is no path between two nodes the distance should be indicated by NaN and the path by None.  

![Tables comparing the shortest distances between each node in the graph when it is weighted or unweighted and directed or undirected. Weighted causes many of the distances to increase and as does directed. Directed also decreases the number of nodes are accessible from which other nodes](https://github.com/jbarbourmoore/Algorithms-And-Data-Structures/blob/48fe4e511fcf3d83faa1bc48ddd7ff56d7dbc8ce/OutputImages/Graph_ShortestDistancesComparisons.png "Shortest Distances Comparisons")

![Tables comparing the shortest paths between each node in the graph when it is weighted or unweighted and directed or undirected. Weighted causes some of the paths to reroute to avoid particularly heavy or expensive routes. Directed  decreases the number of nodes are accessible from which other nodes, thereby changing the routing options.](https://github.com/jbarbourmoore/Algorithms-And-Data-Structures/blob/48fe4e511fcf3d83faa1bc48ddd7ff56d7dbc8ce/OutputImages/Graph_ShortestPathsComparisons.png "Shortest Paths Comparisons")


