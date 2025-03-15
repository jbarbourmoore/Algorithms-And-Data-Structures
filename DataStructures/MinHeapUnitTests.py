import unittest
import MinHeap

class MinHeapUnitTests(unittest.TestCase):
    '''
    This class contains basic unit tests for the min heap data structue
    '''

    def print_results(self, index = None):
        '''
        This method ouputs the current state of the min heap

        Parameters :
            index : int
                A specifc location index that should be outputed
        '''

        self.minheap.printHeap()
        self.minheap.printHeapDimensions()
        if(index != None):
            print(f"The value at index {index} is {self.minheap[index]}")

        print("\n------\n")

    def setUp(self):
        '''
        This method sets up a min heap to be used as the stating point for each unit test

        Starting size : 15
        Starting depth : 4
        Starting values : 0-14
        '''

        print("SETUP")
        print("Creating a min heap with 15 items and a depth of 4")

        starting_array = []

        for i in range (0,15):
            starting_array.append(i)

        self.minheap = MinHeap.MinHeap(starting_array)

        # check that the newly created empty dynamic array has an allocated size of 16 and a size of 0
        assert self.minheap.getHeapSize() == 15 and self.minheap.getHeapDepth() == 4

        self.print_results()
    
    def test_add_item(self):
        '''
        This method tests the addItem method for the min heap
        '''

        self.minheap.addItem(-1)
        self.print_results()
        
        self.assertEqual(self.minheap.getHeapSize(), 16)
        self.assertEqual(self.minheap.getHeapRoot(), -1)
        self.assertEqual(self.minheap.getHeapDepth(), 5)

    def test_add_item_to_front(self):
        '''
        This method tests the addItemToFront method for the min heap
        '''

        self.minheap.addItemToFront(20)
        self.print_results()
        
        self.assertEqual(self.minheap.getHeapSize(), 16)
        self.assertEqual(self.minheap.getHeapRoot(), 0)
        self.assertEqual(self.minheap.getHeapDepth(), 5)
        self.assertEqual(self.minheap[15],20)

    def test_delete_item(self):
        '''
        This method tests the deleteItem method for the min heap
        '''

        self.minheap.deleteItem(0)
        self.print_results()
        
        self.assertEqual(self.minheap.getHeapSize(), 14)
        self.assertEqual(self.minheap.getHeapRoot(), 1)
        self.assertEqual(self.minheap.getHeapDepth(), 4)
        self.assertEqual(self.minheap[7],14)


if __name__ == '__main__':
    unittest.main()