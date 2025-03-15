# Does seem a bit redundant in Python but I want to try it anyways
# This is clearly not a real data structure for use, mearly a simulation of how one could work

class DynamicArray: 
    '''
    This class creates a simulated Dynamic Array data structure

    The allocated size for the array stats at 16 (default value) and doubles every time it is needed to expand
    '''
    
    def __init__(self, initial_size=16, initial_content=0, debug=False):
        '''
        This method is the constructor for the dynamic array data structure

        Parameters :
            initial_size : int
                The initial size for the dynamic array (defaul is 16)
            initial_content : int
                The initial content to fill the dynamic array (defult is 0 -> [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
            debug : boolean
                Whether the dynamic array is being debugged and should generate more detailed output messages (default is false)
        '''

        self.allocated_size = initial_size 
        self.size = 0
        self.array = [initial_content] * initial_size
        self.debug = debug
    
    
    def allocateMemory(self, memory_size_to_allocate=1): 
        '''
        This method allowcates memory for the dynamic array

        Parameters : 
            memory_size_to_allocate : int
                The amount of memory to allocate (default is 1)
        '''

        assert memory_size_to_allocate >= 1
        return [0] * memory_size_to_allocate

    def copyToNewArray(self, new_array):
        '''
        This method copies the array from the old location to the new when its size needs to be increased

        Parameters : 
            new_array : [int]
                The new array which is being copied into
        '''

        old_array_length = len(self.array)
        new_array_length = len(new_array)

        assert old_array_length <= new_array_length, 'New array is smaller than the old array'


        for i in range(0, old_array_length):
            new_array[i] = self.array[i]

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
        assert index >= 0 and index < self.size 

        return self.array[index]
    
    def __setitem__(self, index, value):
        '''
        This method allows direct write access to the array at a given index

        Parameters :
            index: int
                The dynamic array index that is being written to
            value: int
                The value that is being written to the array at the given index
        '''

        # ensure the index is not outside the bounds of the array
        assert index >= 0 and index < self.size 

        self.array[index] = value
    
    def append(self, value_to_add):
        '''
        This method adds a value to the end of the dynamic array.

        If the array does not have enough allocated space, it copies the values to a new array with double the space

        Parameters :
            value_to_add : int
                The value being added to the end of the dynamic array
        '''

        # doubles the allocated size of the array if more space is required
        if self.size >= self.allocated_size:
            self.increase_allocated_size()

        self.array[self.size] = value_to_add
        self.size = self.size + 1

    def increase_allocated_size(self):
        '''
        This method doubles the allocated size for the dynamic array
        '''

        new_array_allocated_size = 2*self.allocated_size

        if self.debug: 
            print(f'Array is full: copying content to new array with a size of {new_array_allocated_size}')

        self.allocated_size = new_array_allocated_size
        new_array = self.allocateMemory(self.allocated_size)

        self.copyToNewArray(new_array)

        self.array = new_array

    def removeItemIgnoreOrder(self, index_to_remove):
        '''
        This method removes an item from the dynamic array without preserving element order

        The operation can be done in constant time as it simplymoves the value from the end of the array into the index being removed and decreases the size by one.
        
        Parameters : 
            index_to_remove : int
                The index of the value to be removed from the array

        Returns :
            item_to_remove : int
                The value of the item removed from the array
        '''
        # ensure the index is not outside the bounds of the array
        assert index_to_remove >= 0 and index_to_remove < self.size 

        item_to_remove = self.array[index_to_remove]

        starting_size = self.size
        self.array[index_to_remove] = self.array[starting_size-1]
        self.size = starting_size - 1

        return item_to_remove

    def removeItemPreserveOrder(self, index_to_remove):
        '''
        This method removes an item from the dynamic array while preserving element order

        This operation is maybe worst case O(n) as removing the first item in an array would require you to move every item
        
        Parameters : 
            index_to_remove : int
                The index of the value to be removed from the array
        
        Returns :
            item_to_remove : int
                The value of the item removed from the array
        '''
        # ensure the index is not outside the bounds of the array
        assert index_to_remove >= 0 and index_to_remove < self.size 

        item_to_remove = self.array[index_to_remove]

        starting_size = self.size

        # move every item to the right of the index one position to the left
        for i in range(index_to_remove, starting_size):
            self.array[i] = self.array[i + 1]

        self.size = starting_size - 1

        return item_to_remove

    def insertAtIndex(self, index, value_to_add):
        '''
        This method adds a value at a specific index of the dynamic array.

        If the array does not have enough allocated space, it copies the values to a new array with double the space

        Parameters :
            index : int
                The index at which the value is being added
            value_to_add : int
                The value being added to the end of the dynamic array
        '''

        # doubles the allocated size of the array if more space is required
        if self.size >= self.allocated_size:
            self.increase_allocated_size()

        # ensure the index is not outside the bounds of the array
        assert index >= 0 and index < self.size 

        # increases the array size
        self.size += 1

        # moves every item to he right of the index one position over
        for i in range(0,self.size-index):
            self.array[self.size-i] = self.array[self.size-i-1]

        #inserts the value
        self.array[index] = value_to_add
    
    def printHead(self, length = 10):
        '''
        This method prints the begining of the array

        Parameters :
            length : int
                The number of values to print (default is 10)
        '''

        if length > self.size :
            print(f"The current values in the array are {self.array[0:self.size]}")
        else :
            print(f"The first {length} values are {self.array[0:length]}")
    
    def printDimensions(self):
        '''
        This method prints the current size and allocated size of the array
        '''

        print(f"Current dynamic array size is {self.size} and allocated size is {self.allocated_size}")

if __name__ == '__main__':
    print("\n-------\n")
    print("Creating an empty dynamic array with an initial allocated size of 16:")
    dynamic_array = DynamicArray(initial_size=16, initial_content=0, debug=True)

    # check that the newly created empty dynamic array has an allocated size of 16 and a size of 0
    assert dynamic_array.allocated_size == 16 and dynamic_array.size == 0

    dynamic_array.printHead()
    dynamic_array.printDimensions()

    print("\n-------\n")
    print("Adding 2048 values to the array:")

    # add 2047 items to the end of the dynamic array
    for i in range(2048):
        dynamic_array.append(i)

    dynamic_array.printHead()
    dynamic_array.printDimensions()

    # check that both the size and allocated size are 2048
    assert dynamic_array.allocated_size == 2048 and dynamic_array.size == 2048
    # chack that the elements at 4, 5 and 2047 match their index
    assert dynamic_array[4] == 4 and dynamic_array[5] == 5 and dynamic_array[2047] == 2047

    print("\n-------\n")
    print("Adding value 10 to the array at index 4:")
    print("(This should cause the array to overflow and double its allocated size while increasing its size by one)")
    dynamic_array.insertAtIndex(index=4,value_to_add=10)

    dynamic_array.printHead()
    dynamic_array.printDimensions()

    # check that allocated size has doubled as the array should have reached its limit and the size has incremented by one
    assert dynamic_array.allocated_size == 4096 and dynamic_array.size == 2049
    # check that the element at 4 is now the inserted value and the other values have moved one position to the right
    assert dynamic_array[4] == 10 and dynamic_array[5] == 4 and dynamic_array[6] == 5 and dynamic_array[2048] == 2047

    # check the valus at 0, 2048 and 2047 are as expected
    assert dynamic_array[0] == 0 and dynamic_array[1] == 1 and dynamic_array[2048] == 2047 and dynamic_array[2047] == 2046


    print("\n-------\n")
    print("Removing the value at index 0 without preserving order:")
    item_removed = dynamic_array.removeItemIgnoreOrder(0)

    print(f"The value removed was {item_removed}")
    dynamic_array.printHead()
    dynamic_array.printDimensions()

    # check that the item removed was correct and the size decreased
    assert item_removed == 0 and dynamic_array.size == 2048
    # check that the last value of the array was moved to replace it while the other values did not move
    assert dynamic_array[1] == 1 and dynamic_array[0] == 2047 and dynamic_array[2047] == 2046

    # check that the values at 2, 3 and 2047 are as expected
    assert dynamic_array[2] == 2 and dynamic_array[3] == 3 and dynamic_array[4] == 10 and dynamic_array[2047] == 2046

    print("\n-------\n")
    print("Removing the value at index 2 and preserving order:")

    item_removed = dynamic_array.removeItemPreserveOrder(2)

    print(f"The value removed was {item_removed}")
    dynamic_array.printHead()
    dynamic_array.printDimensions()

    # check that the item removed was correct and the size decreased
    assert item_removed == 2 and dynamic_array.size == 2047
    # check that the values past index 2 all shifted one position to the left preserving order
    assert dynamic_array[2] == 3 and dynamic_array[3] == 10 and dynamic_array[2046] == 2046