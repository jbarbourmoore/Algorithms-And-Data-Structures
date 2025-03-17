

class BinarySearchTreeNode():
    '''
    This class holds a single node for the binary search tree and points to its left and right child nodes
    '''

    def __init__(self, value, left_child = None, right_child = None):
        '''
        This method initializes the node object 

        Parameters : 
            value : int
                The node's value
            left_child : BinarySearchTreeNode (optional)
                The node's left child node (default is None)
            right_child : BinarySearchTreeNode (optional)
                The node's right child node (default is None)
        '''

        self.value = value

        self.left_child = left_child
        self.right_child = right_child

    def getValue(self):
         return self.value
    
    def getRightChild(self):
         return self.right_child
    
    def getLeftChild(self):
         return self.left_child

    def setRightChild(self, node):
         self.right_child = node

    def setLeftChild(self, node):
         self.left_child = node
    
    def hasLeftChild(self):
         return self.left_child != None
    
    def hasRightChild(self):
         return self.right_child != None

class BinarySearchTree():
    '''
    This class holds  the binary search tree, primarily storing the root node and holding the various methods for interacting with it
    
    Each node can have a left child and a right child node
    Each left child node must be smaller than the parent node and each right child node must be larger than the parent node
    '''

    def __init__(self, debug = False):
        '''
        This method initializes the binary search tree object

        Parameters :
            debug : Boolen (optional)
                Whether the binary search tree should produce more detailed outputs to help with debugging
        '''

        self.root = None
        self.debug = debug

    def insertItem(self, value):
        '''
        This method inserts an item into the binary search tree

        Parameters :
            value : int
                The value being inserted into the binary search tree
        '''

        if self.root == None:
            node = BinarySearchTreeNode(value)
            self.root = node
            if self.debug:
                print(f"New node for {value} added as root")
        else:
            self.insertItemHelper(current_node=self.root, value_to_insert=value)
        
    def insertItemHelper(self, current_node:BinarySearchTreeNode, value_to_insert):
        '''
        This is a recursive method which helps with adding an item into the binary search tree

        Parameters :
            current_node : BinarySearchTreeNode
                The node that the value will be added beneath
            value_to_insert :
                The value that is being inserted into the binary search tree

        Returns : 
            current_node : BinarySearchTreeNode
                The node that the value will be added beneath
        '''

        if current_node.getValue() == value_to_insert:
                if self.debug:
                    print(f"Value {value_to_insert} is already in the binary search tree")
                return current_node
        if current_node.getValue() > value_to_insert:
                if current_node.getLeftChild() == None:
                    if self.debug:
                        print(f"New node for {value_to_insert} added as left child node for {current_node.getValue()}")
                    left_child_node = BinarySearchTreeNode(value=value_to_insert)
                    current_node.setLeftChild(left_child_node)
                else:
                    left_child_node = self.insertItemHelper(current_node=current_node.getLeftChild(), value_to_insert=value_to_insert)
                    current_node.setLeftChild(left_child_node)
        elif current_node.getValue() < value_to_insert:
                if current_node.getRightChild() == None:
                    if self.debug:
                        print(f"New node for {value_to_insert} added as right child node for {current_node.getValue()}")
                    right_child_node = BinarySearchTreeNode(value=value_to_insert)
                    current_node.setRightChild(right_child_node)
                else:
                    right_child_node = self.insertItemHelper(current_node=current_node.getRightChild(), value_to_insert=value_to_insert)
                    current_node.setRightChild(right_child_node)
        return current_node
    
    def printNodesInAscendingOrder(self):
        '''
        This method prints out the current nodes of the binary search tree in ascending order
        '''

        if self.root == None:
             print("This Binary Search Tree does not hava a root node")
        else:
            print("The current nodes in order: ", end=" ")
            self.printNodesInAscendingOrderHelper(self.root) 
            print()

    def printNodesInAscendingOrderHelper(self, current_node: BinarySearchTreeNode):
        '''
        This is a recursive method which helps print the binary search tree nodes in ascending order

        Parameters :
            current_node : BinarySearchTreeNode
                The node that is currently being examined for printing
        '''

        if current_node.hasLeftChild():
                self.printNodesInAscendingOrderHelper(current_node.getLeftChild())
        print(current_node.getValue(), end=" ")
        if current_node.hasRightChild():
                self.printNodesInAscendingOrderHelper(current_node.getRightChild())

    def searchForNode(self, value_to_search):
        '''
        This method searches for a value in the binary search tree and returns that node or None if it can't be found

        Parameters :
            value : int
                The value that is being searched for in the binary search tree

        Returns :
            node_with_value : BinarySearchTreeNode or None
                The node that contains the value being searched for or none if it doesn't exist
        '''
  
        if self.root is None or self.root.getValue() == value_to_search:
            return self.root
        elif self.root.getValue() < value_to_search and self.root.hasRightChild():
            return self.searchForNodeHelper(self.root.getRightChild(), value_to_search=value_to_search)
        elif self.root.getValue() > value_to_search and self.root.hasLeftChild():
            return self.searchForNodeHelper(self.root.getLeftChild(), value_to_search=value_to_search)
            
    def searchForNodeHelper(self, current_node: BinarySearchTreeNode, value_to_search):
        '''
        This method is a recursive helper method for searching for a value in the binary search tree and returns that node or None if it can't be found

        Parameters :
            current_node : BinarySearchTreeNode
                The current node that is being searched under for the value
            value : int
                The value that is being searched for in the binary search tree

        Returns :
            node_with_value : BinarySearchTreeNode or None
                The node that contains the value being searched for or none if it doesn't exist
        '''

        if current_node.getValue() == value_to_search:
             return current_node
        elif current_node.getValue() < value_to_search and current_node.hasRightChild():
            return self.searchForNodeHelper(current_node.getRightChild(), value_to_search=value_to_search)
        elif current_node.getValue() > value_to_search and current_node.hasLeftChild():
            return self.searchForNodeHelper(current_node.getLeftChild(), value_to_search=value_to_search)
        else:
             return None
        
    def hasValue(self, value_to_search):
        '''
        This method searches for a value in the binary search tree and returns True if it exists

        Parameters :
            value : int
                The value that is being searched for in the binary search tree
        
        Returns :
            does_exist : Boolean
                Whether the value exists in the binary search tree
        '''

        potential_node = self.searchForNode(value_to_search=value_to_search)
        if potential_node == None:
             return False
        return True
        
if __name__ == '__main__':
    binary_search_tree = BinarySearchTree(debug=True)
    binary_search_tree.printNodesInAscendingOrder()

    binary_search_tree.insertItem(3)
    binary_search_tree.insertItem(5)
    binary_search_tree.insertItem(43)
    binary_search_tree.printNodesInAscendingOrder()
    binary_search_tree.insertItem(-2)
    binary_search_tree.insertItem(36)
    binary_search_tree.printNodesInAscendingOrder()

    print(f"Searching for root value 3: {binary_search_tree.searchForNode(3).getValue()}")
    print(f"Searching for existing value 36: {binary_search_tree.searchForNode(36).getValue()}")
    print(f"Searching for existing value -2: {binary_search_tree.searchForNode(-2).getValue()}")
    print(f"Searching for non existant value -7: {binary_search_tree.hasValue(-7)}")
    print(f"Searching for non existant value 70: {binary_search_tree.hasValue(70)}")
    print(f"Searching for non existant value 8: {binary_search_tree.hasValue(8)}")


