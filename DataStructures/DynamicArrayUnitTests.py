import unittest
import DynamicArray

class DynamicArrayUnitTests(unittest.TestCase):
    '''
    This class contains basic unit tests for the dynamic array datastructue
    '''

    def print_results(self, index = None):
        '''
        This method ouputs the current state of the dynamic array

        Parameters :
            index : int
                A specifc location index that should be outputed
        '''

        self.dynamic_array.printHead()
        self.dynamic_array.printDimensions()
        if(index != None):
            print(f"The value at index {index} is {self.dynamic_array[index]}")

        print("\n------\n")

    def setUp(self):
        '''
        This method sets up a dynamic array to be used as the stating point for each unit test

        Starting size : 16
        Starting allocated size : 16
        Starting values : 0-15
        Debug : True
        '''

        print("SETUP")
        print("Creating an empty dynamic array with an initial allocated size of 4:")
        self.dynamic_array = DynamicArray.DynamicArray(initial_size=4, initial_content=0, debug=True)

        # check that the newly created empty dynamic array has an allocated size of 16 and a size of 0
        assert self.dynamic_array.allocated_size == 4 and self.dynamic_array.size == 0

        print("Adding 16 values to the array:")

        # add 2047 items to the end of the dynamic array
        for i in range(16):
            self.dynamic_array.append(i)

        self.initial_size = self.dynamic_array.size
        self.initial_allocated_size = self.dynamic_array.allocated_size
        self.print_results()

    def test_append(self):
        '''
        This method tests the append method for the dynamic array
        '''

        self.dynamic_array.append(10)

        self.assertEqual(self.dynamic_array[self.dynamic_array.size - 1], 10)
        self.assertEqual(self.dynamic_array.allocated_size, self.initial_allocated_size*2)
        self.assertEqual(self.dynamic_array.size, self.initial_size + 1)
        self.print_results(index=self.dynamic_array.size - 1)

    def test_insert_at_index(self):
        '''
        This method tests adding a value at a certain index to the dynamic array
        '''

        self.dynamic_array.insertAtIndex(index=5, value_to_add=10)

        self.assertEqual(self.dynamic_array[5], 10)
        self.assertEqual(self.dynamic_array[self.dynamic_array.size - 1], self.dynamic_array.size - 2)
        self.assertEqual(self.dynamic_array.allocated_size, self.initial_allocated_size*2)
        self.assertEqual(self.dynamic_array.size, self.initial_size + 1)
        self.print_results(index=5)

    def test_remove_ignore_order(self):
        '''
        This method tests removing an item from the dynamic array without preserving order
        '''

        removed_index = 5
        removed_item = self.dynamic_array.removeItemIgnoreOrder(removed_index)

        self.assertEqual(removed_item, removed_index)
        self.assertEqual(self.dynamic_array[removed_index], self.initial_size-1)
        self.assertEqual(self.dynamic_array[self.dynamic_array.size - 1], self.initial_size - 2)
        self.assertEqual(self.dynamic_array.allocated_size, self.initial_allocated_size)
        self.print_results(index=removed_index)

    def test_remove_preserve_order(self):
        '''
        This method tests removing an item from the dynamic array while preserving order
        '''

        removed_index = 5
        removed_item = self.dynamic_array.removeItemPreserveOrder(removed_index)

        self.assertEqual(removed_item, removed_index)
        self.assertEqual(self.dynamic_array[removed_index], removed_index + 1)
        self.assertEqual(self.dynamic_array[self.dynamic_array.size - 1], self.initial_size - 1)
        self.assertEqual(self.dynamic_array.allocated_size, self.initial_allocated_size)
        self.print_results(index=removed_index)

if __name__ == '__main__':
    unittest.main()