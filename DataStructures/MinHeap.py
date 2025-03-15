import math

class MinHeap:
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

        self.array = array

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
    
    def printHeapDimensions(self):
        '''
        This method outputs the current heap dimensions
        '''

        print(f"The heap containing {self.getHeapSize()} elements has a depth of {self.getHeapDepth()} and a root of {self.getHeapRoot()}")
    
if __name__ == '__main__':

    starting_array = []

    for i in range (0,14):
        starting_array.append(i)

    minheap = MinHeap(starting_array)

    minheap.printHeapDimensions()