

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
        
if __name__ == '__main__':
    binary_search_tree = BinarySearchTree(debug=True)

    binary_search_tree.insertItem(3)
    binary_search_tree.insertItem(5)
    binary_search_tree.insertItem(43)
    binary_search_tree.insertItem(-2)
    binary_search_tree.insertItem(36)
