import math

from Graph import GraphNode

class MinHeapForObjects:
    '''
    This class shall function as a minheap data structure
    '''

    array = []

    def __init__(self, array=[]):
        '''
        This method initializes the minheap data structure based on a giveb starting array 

        Parameters :
            array : [int], optional
                The array that the minheap shall be created around (default is the empty array [])
        '''
        self.swap_count = 0
        self.array = array
        self.heapify()
        

    def swap(self, index_a, index_b):
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
        self.swap_count += 1
        # assumes both index values are positive and not out of bound of the array
        # arr(a) = arr[b] and arr(b) = arr[a]
        (self.array[index_a], self.array[index_b]) = (self.array[index_b], self.array[index_a])

    def addItem(self, item_to_add):
        '''
        This method adds an item to the end of the min heap and then calls bubble up to position the item appropriately

        Paramters :
            item_to_add : Object
                The item to be added to the min heap and then positioned appropriately
        '''
        item_to_add.is_in_queue = True

        self.array.append(item_to_add)
        index_added = len(self.array) - 1
        self.bubbleUp(index_added)

    def bubbleUp(self, starting_index):
        '''
        This method completes the bubble up algorithm to appropriately position an item at a given index in the min heap

        Parameters : 
            starting_index : int
                The index of the item to be positioned within the min heap
        '''

        parent_index = self.getParentIndex(starting_index)

        if starting_index < 1 :
            return
        else :
            if self[starting_index].getPriority() < self[parent_index].getPriority():
                self.swap(starting_index, parent_index)
                self.bubbleUp(parent_index)

        return

    def addItemToFront(self, item_to_add):
        '''
        This method adds an item to the front of the min heap and calls bubble down in order to position it 

        Parameters :
            item_to_add : int
                The item to be added to the front of the min heap
        '''

        self.array.insert(0,item_to_add)
        index_added = 0
        self.bubbleDown(index_added)

    def getParentIndex(self, index):
        '''
        This method gets the index value that would be the parent item for a given index if it exists

        Parameters :
            index : int
                The index of the item for which one is finding the parent index

        Returns : 
            parent_index : int
                The index the parent have if it exists
        '''

        return index // 2
    
    def getChildIndexes(self, index):
        '''
        This method gets the index values that would be the child items for a given index if they are in the heap

        Parameters :
            index : int
                The index of the item for which one is finding the child indexes

        Returns : 
            left_child_index : int
                The index the left child would have if it exists
            right_child_index : int
                The index the right child would have if it exists
        '''

        left_child_index = 2 * (index) + 1
        right_child_index = left_child_index + 1
        return left_child_index, right_child_index

    def bubbleDown(self, starting_index):
        '''
        This method completes the bubble down algorithm to apropriately position an item which is too high in the min heap

        Parameters :
            starting_index : int
                The index of the item to be repositioned using bubble down
        '''

        heap_size = self.getHeapSize()

        left_child_index, right_child_index = self.getChildIndexes(starting_index)

        # the item has no children
        if left_child_index > heap_size -1:
            return
        
        # the item has 1 left child
        elif right_child_index > heap_size - 1:
            if self[starting_index].getPriority() > self[left_child_index].getPriority():
                self.swap(starting_index, left_child_index)
                self.bubbleDown(left_child_index)

        # the item has 2 children
        else :
            # if the left child is the smaller one
            if self[left_child_index].getPriority() < self[right_child_index].getPriority():
                if self[starting_index].getPriority() > self[left_child_index].getPriority():
                    self.swap(starting_index, left_child_index)
                    self.bubbleDown(left_child_index)
                elif self[starting_index].getPriority() > self[right_child_index].getPriority():
                    self.swap(starting_index, right_child_index)
                    self.bubbleDown(right_child_index)
                
            else:
                if self[starting_index].getPriority() > self[right_child_index].getPriority():
                    self.swap(starting_index, right_child_index)
                    self.bubbleDown(right_child_index)
                elif self[starting_index].getPriority() > self[left_child_index].getPriority():
                    self.swap(starting_index, left_child_index)
                    self.bubbleDown(left_child_index)

        return
    
    def deleteItem(self, index):
        '''
        This method removes an item from the array by swapping it with the last item and then deleting the last item

        It then uses bubble up if the item is smaller than its parent or bubble down if the item is bigger than its child

        Parameters :
            index : int
                The index of the item to be removed
        '''

        starting_length = len(self.array)

        if starting_length > 1:
            self.swap(index, starting_length-1)

            item_deleted = self.array.pop(starting_length-1)

            parent_index = self.getParentIndex(index)
            left_child_index, right_child_index = self.getChildIndexes(index)

            if self[index].getPriority() < self[parent_index].getPriority() :
                self.bubbleUp(index)
            elif left_child_index < len(self.array) and right_child_index < len(self.array):
                if self[index].getPriority() > self[left_child_index].getPriority() or self[index].getPriority() > self[right_child_index].getPriority():
                    self.bubbleDown(index)
            elif left_child_index < len(self.array):
                if self[index].getPriority() > self[left_child_index].getPriority():
                    self.bubbleDown(index)
            item_deleted.is_in_queue = False
            return item_deleted
        elif starting_length == 1:
            item_deleted = self.array.pop(starting_length-1)
            item_deleted.is_in_queue = False
            return item_deleted 

    def heapify(self):
        '''
        This method turns the array into a min heap using bubble down
        '''

        heap_size = self.getHeapSize()

        for i in range(heap_size-1, -1, -1):
            self.bubbleDown(i)
    
    def __getitem__(self, index):
        '''
        This method allows direct access to the array value at a given index

        Parameters : 
            index : int
                The index of the array value which is being accessed

        Returns :
            array[index] : int
                The value of the array at the given index
        '''

        # ensure the index is not outside the bounds of the array
        assert index >= 0 and index < self.getHeapSize()

        return self.array[index]

    def getHeapRoot(self):
        '''
        This method gets the current value of the heap root

        Returns :
            heap_root : int
                The heap root or the smallest number in the minheap, located at index 0
        '''

        return self.array[0]
    
    def getHeapSize(self):
        '''
        This method gets the current size (number of elements) of the heap

        Returns :
            element_count : int
                The size of the heap, determined by the length of the array
        '''

        return len(self.array)
    
    def getHeapDepth(self):
        '''
        This method calculates the current depth of the heap

        Returns :
            heap_depth : int
                The current depth of the array, determined based on the log2(heap_size)
        '''

        heap_size = self.getHeapSize()

        heap_depth = math.floor(math.log2(heap_size)) +1

        return heap_depth
    
    def updateItemPriority(self, item):
        '''
        This method updates the position of an item in the min heap if it's priority has changed

        Parameters :
            item : Object
                The item that may need to be moved
        '''

        starting_position = self.array.index(item)

        self.bubbleDown(starting_index=starting_position)
        self.bubbleUp(starting_index=starting_position)

    def isEmpty(self):
        '''
        This method returns whether the minheap is currently empty
        '''

        return len(self.array) == 0
    
    def printHeap(self):
        '''
        This method outputs each level of the min heap on its own line
        '''
        previous_index = 0
        for i in range(0,self.getHeapDepth()):
            next_index = previous_index+2**i
            if next_index > len(self.array) :
                next_index = len(self.array)
            for j in range(previous_index, next_index):
                self.array[j].printAbbreviated()
            previous_index = next_index
            print()
        print()
    
    def printHeapDimensions(self):
        '''
        This method outputs the current heap dimensions
        '''

        print(f"The heap containing {self.getHeapSize()} elements has a depth of {self.getHeapDepth()} and a root of {self.getHeapRoot().getDescription()}")
    
if __name__ == '__main__':

    starting_array = []

    for i in range (0,14):
        starting_array.append(GraphNode(number=i,parent=i-1, distance=i))

    minheap = MinHeapForObjects(starting_array)
    minheap.printHeap()
    minheap.printHeapDimensions()

    i=i+1
    newNode = GraphNode(number=i,parent=i-1, distance=i)
    minheap.addItem(newNode)
    minheap.printHeap()
    minheap.printHeapDimensions()
    i=i+1
    newNode_2 = GraphNode(number=i,parent=i-1, distance=1)
    minheap.addItem(newNode_2)
    minheap.printHeap()
    minheap.printHeapDimensions()
    i=i+1
    newNode_3 = GraphNode(number=i,parent=i-1, distance=-2)
    minheap.addItem(newNode_3)
    minheap.printHeap()
    minheap.printHeapDimensions()
    i=i+1
    newNode_4 = GraphNode(number=i,parent=i-1, distance=1)
    minheap.addItemToFront(newNode_4)
    minheap.printHeap()
    minheap.printHeapDimensions()

    newNode_4.distance = 20
    minheap.updateItemPriority(newNode_4)
    minheap.printHeap()