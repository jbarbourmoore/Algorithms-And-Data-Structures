
class HashTable():
    '''
    This class serves as a hash table data stucture
    '''

    def __init__(self, rows = 4, increase_multiplier = 2, maximum_load_factor = .5, debug = False):
        '''
        This method initializes the hashtable data structure object with a given number of rows

        Parameters : 
            rows : int
                The number of rows that will initially be in the hashtable in order to store items
            increase_multiplier : item
                The factor by which to increase the table's rows when it reaches it's maximum load factor (default is 2)
            maximum_load_factor : float
                The maximum ratio of items to rows that should be stored in the hashtable to limit collisions (default is .5)
            debug : Boolean
                Whether the HashTable should print out information regarding its internal process (default is False)
        '''

        self.row_count = rows
        self.increase_multiplier = increase_multiplier
        self.maximum_load_factor = maximum_load_factor
        self.count_items = 0
        self.debug = debug
        self.load_factor = 0
        self.array = [] 
        for _ in range(0, self.row_count):
            self.array.append([])

    def addItem(self, item):
        '''
        This method adds an item to the hashtable

        Parameters : 
            item : any (?)
                The item to add to the hashtable
        '''

        index = self.calculateItemRow(item)

        self.array[index].append(item)

        self.count_items += 1

        self.checkCurrentLoadFactor()

    def deleteItem(self, item):
        '''
        This method removes an item from the hashtable

        Parameters : 
            item : any (?)
                The item to remove from the hashtable
        '''

        index = self.calculateItemRow(item)

        if item in self.array[index]:
            self.array[index].remove(item)
            self.count_items -= 1

    def increase_capacity(self):
        '''
        This method increases the capacity of the hashtable

        The new capacity is the current rows multiplied by the increase_multiplier for the hashtable
        Each item currently in the hash table is rehashed and added to the expanded hashtable
        '''

        current_row_count = self.row_count
        self.row_count = current_row_count * self.increase_multiplier
        self.count_items = 0
        current_array = self.array
        self.array = []
        for _ in range(0, self.row_count):
            self.array.append([])

        for row_index in range(0, current_row_count):
            for item in current_array[row_index]:
                self.addItem(item)


        self.checkCurrentLoadFactor()

        if self.debug:
            print(f"The new row count is {self.row_count} and the load factor is now {self.load_factor}")


    def calculateItemRow(self, item):
        '''
        This function uses the hash of an item to determine what row it should be stored in the hash table using the modulo division with the hashtables row count

        Parameters : 
            item
                The item that the row is being calculated for
        '''

        item_hash = hash(item)

        calculated_item_row = item_hash % self.row_count

        return calculated_item_row

    def checkCurrentLoadFactor(self):
        '''
        This function calculates the current load factor for the hash function and expands the table if the load factpr is higher than the hashtable's load_factor_limit
        '''

        self.load_factor =  self.count_items / self.row_count

        if self.load_factor > self.maximum_load_factor:
            if self.debug :
                print(f"The current row count is {self.row_count} and the load factor is {self.load_factor} and the HashTable needs to expand")
            self.increase_capacity()

    def outputHashTable(self):
        '''
        This function output's the current state of the hashtable
        '''

        print(f"The HashTable currently has {self.row_count} rows, a load factor of {self.load_factor} and is storing {self.count_items} items")
        print(f"Its maximum load factor is {self.maximum_load_factor} and it's size is increased by a factor of {self.increase_multiplier} when it needs to expand")
        print(self.array)

if __name__ == "__main__":

    hashtable = HashTable(debug=True)

    hashtable.outputHashTable()

    items_to_add = [56, "Hello", "This", "Is", "A", "Hashtable", "Implementation", 1, 83, True]

    for item_to_add in items_to_add:
        hashtable.addItem(item=item_to_add)

    hashtable.outputHashTable()