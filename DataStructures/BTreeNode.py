from matplotlib import pyplot as plt
import networkx as nx
import seaborn as sns

class BTreeNode(object):
    '''
    This class creates the node object for the BTree data structure

    - Each node can have multiple keys
    - Ensure each node has a minimum number of keys
    - All leaves are the same level

    Time complexity for operations on a BTree should be O(log(n))
    '''

    def __init__(self, keys = None, children = None, is_root_node = False, parent_information = None, minimum_key_count = 3, debug = False):
        '''
        This method initializes the BTreeNode object

        Parameters :
            keys : [int], optional
                The list of keys in the BTreeNode when it is created (default is None)
            children : [BTreeNode], optional
                The list of children for the BTreeNode when it is created (default is None)
            is_root_node : Boolean, optional
                Whether the BTreeNode is the root node when it is created (default is False)
            parent_information : (BTreeNode, int)
                The parent information for the BTreeNode when it is created (default is None)
            minimum_key_count : int, optional
                The minimum key count for any node in a tree which is not root (default is 3)
                (maximum key count is double the minimum key count)
            debug : Boolean
                Whether the BTreeNode should be generation more output to help with debugging
        '''

        if keys == None:
            self.keys = []
        else:
            self.keys = keys
        if children == None:
            self.children = []
        else:
            self.children = children
        self.is_root_node = is_root_node
        self.parent_information = parent_information
        self.minimum_key_count = minimum_key_count
        self.debug = debug

        
    def is_leaf_node(self):
        '''
        This method returns whether the node is a leaf node or not

        Returns :
            is_leaf_node : Boolean
                Whether or not this BTreeNode is currently a leaf node
        '''

        return len(self.children) == 0
    
    def setParentInformation(self, parent_node, index_self_as_child):
        '''
        This method sets the parent information for the BTree Node
        '''
        
        self.parent_information = (parent_node, index_self_as_child)
    
    def searchForKey_Internal(self, key_to_search):
        '''
        This method uses recursion to search through internal nodes for a given key 

        Parameters :
            key_to_search : int
                The key value that is being searched for within the BTree
        '''

        number_of_keys = len(self.keys)
        if number_of_keys == 0:
            return None

        # Search this node's keys for the key_to search
        i = 0
        while i < number_of_keys and self.keys[i] < key_to_search:
            i = i + 1

        # do find the key in this BTreeNode's keys
        if i < number_of_keys and self.keys[i] == key_to_search:
            return (self, i)
        
        # don't find the key in this BTreeNode's keys
        else: 
            if self.is_leaf_node():
                return None
            else:
                return self.children[i].searchForKey_Internal(key_to_search)
            
    def searchForKey(self, key_to_search):
        '''
        This method starts a recursive search for key at the root node

        Parameters :
            key_to_search : int
                The key value that is being searched for within the BTree
        '''

        search_result = self.searchForKey_Internal(key_to_search)

        return search_result
    
    def findSuccessorNodeToKey(self, key_index):
        '''
        This method searches for the successor for the BTreeNode's given key index

        The successor is found by going to the node to the right of the key index once and then going to the nodes the left

        Parameters :
            key_index : int
                The index of the key to which we are finding the successor node

        Returns :
            child_information : (int, BTreeNode)
                The BTreeNode of the successor and it's first key value
        '''

        if self.is_leaf_node() or key_index >= len(self.keys) - 1:
            return None
        
        child = self.children[key_index + 1]

        while not child.is_leaf_node():
            child = child.children[0]

        return (child.keys[0], child)
    
    def addNewKey(self, new_key):
        '''
        This method adds a new key to the root node of the BTree

        Parameters :
            new_key : int
                The new key to be added to the BTree

        Returns :
            root_node : BTreeNode
                The root node of the BTree
        '''

        result = self.addNewKey_Internal(new_key)

        if result != None: 
            (middle_key, first_new_node, second_new_node) = result
            self.is_root = False
            if self.debug:
                print(f"Creating new root with keys={middle_key}")
            new_root = BTreeNode( keys=[middle_key], children=[first_new_node, second_new_node], is_root_node=True, minimum_key_count=self.minimum_key_count, debug=True)
            first_new_node.setParentInformation(new_root, 0)
            second_new_node.setParentInformation(new_root, 1)
            return new_root
        else:
            return self
        
    def addNewKey_Internal(self, new_key):
        '''
        This is a recursive method for adding a new key to the BTree

        If it finds a place for the node it returns None, but if it does not and the parent node needs to be
        split it returns the information for the necessary split

        Parameters :
            new_key : int
                The new key to be added to the BTree
            
        Returns : 
            split_information : (int, BTreeNode, BTreeNode)
                The middle key and the two new nodes if a split is required
        '''

        if self.is_leaf_node(): 
            self.insertKey_LeafNode(new_key)
            number_of_keys = len(self.keys)
            if self.debug:
                    print(f"Added key {new_key} to {self.keys}")
            if number_of_keys <= 2 * self.minimum_key_count:
                # The new key has been successfully inserted into the BTree
                
                return None
            
            else:
                # The node needs to be split in order to create room for the key as the keys are full
                (middle_key, first_new_node, second_new_node) = self.splitNode()
                return (middle_key, first_new_node,  second_new_node)
        else:
            i = 0
            number_of_keys = len(self.keys)
            while i < number_of_keys and self.keys[i] < new_key:
                i = i + 1
            if  i < number_of_keys and self.keys[i] == new_key:
                if self.debug:
                    print(f"{new_key} is already in the BTree")
                return None           
            else:
                result = self.children[i].addNewKey_Internal(new_key)

                if result != None:

                    (middle_key, first_new_node, second_new_node) = result
                    self.insertKeyAndChildren(middle_key, first_new_node, second_new_node, i)

                    if len(self.keys) == 2 * self.minimum_key_count + 1:
                        # The node needs to be split in order to create room for the key as the keys are full
                        (middle_key, first_new_node, second_new_node) = self.splitNode()
                        return (middle_key, first_new_node, second_new_node)
    
    def insertKey_LeafNode(self, new_key):
        '''
        This method inserts the new key into this leaf node's list of keys

        Parameters :
            new_key : int
                The new key to be added to the BTree
        '''

        number_of_keys = len(self.keys)
        self.keys.append(new_key)
        i = number_of_keys - 1
        while i >= 1 and self.keys[i] < self.keys[i-1]:
            (self.keys[i-1], self.keys[i]) = (self.keys[i], self.keys[i-1])
            i -= 1
            
    def insertKeyAndChildren(self, new_key, left_node, right_node, index):
        '''
        This method inserts a key to this node's keys at a specific index

        Parameters :
            new_key : int
                The new key to be added to the BTree
            left_node : BTreeNode
                The node to the left of the split
            right_node : BTreeNode
                The node to the right of the split
            index : int
                The index of the insertion
        '''

        if self.debug:
            print(f"Inserting key {new_key} and children at {self.keys}")
        number_of_keys = len(self.keys)
        left_node.setParentInformation(self, index)
        new_child = right_node
        # swap all the keys and children making room for the added key and child
        for i in range(index, number_of_keys):
            (self.keys[i], new_key) = (new_key, self.keys[i])
            (self.children[i+1], new_child) = (new_child, self.children[i+1])
            self.children[i+1].setParentInformation(self, i+1) 
        self.keys.append(new_key)
        self.children.append(new_child)

        new_child.setParentInformation(self, number_of_keys+1)
        
    def correctParentInformationForChildren(self):
        '''
        This method ensures that all of this node's children correctly identify it as the parent node
        '''

        for (i, child_node) in enumerate(self.children):
            child_node.setParentInformation(self, i)
        
    def splitNode(self):
        '''
        This method splits a full node when adding a new key

        Returns :
            middle_key : int
                The key in the middle of the node
            self : BTreeNode
                The node itself
            new_node : BTreeNode
                The new node that was created with half of this node's keys
        '''
        middle_key = self.keys[self.minimum_key_count]
        new_keys = list(self.keys[self.minimum_key_count+1:])
        self.keys = list(self.keys[:self.minimum_key_count])
        if self.is_leaf_node():
            new_children_nodes = []
        else:
            new_children_nodes = list(self.children[self.minimum_key_count+1:])
            self.children = list(self.children[:self.minimum_key_count+1])
        new_node = BTreeNode(keys=new_keys, children=new_children_nodes, is_root_node=False, minimum_key_count=self.minimum_key_count, debug=self.debug)
        new_node.correctParentInformationForChildren()
        if self.debug:
            print(f"splitting node {self.keys} returning self {self} as first_new_node and {new_node} as second_new_node")
        return (middle_key, self, new_node)

    def __str__(self):
        '''
        This method implements the defult to string method for the BTreeNode

        Returns 
            list_of_keys : str
                The BTreeNode's key list as a string
        '''

        return str(self.keys)
    
    def createNetworkGraphForVisualization(self, graph, node_id, parent_id, node_labels):
        '''
        This is a recursive method that adds the information for each node to a networkx graph for visualization 

        Parameters :
            graph : Graph
                The networkx graph
            node_id : int 
                The id of the node
            parent_id : int 
                The id of the parent node
            node_labels : {int:str}
                The dictionary containing the label strings for each node
        Returns :
            next_node_id : int
                The id available for the next node to be drawn
        '''

        node_label = str(self.keys)
        
        graph.add_node(node_id, label=node_label)

        node_labels[node_id] = node_label
        if parent_id >= 0: graph.add_edge(parent_id, node_id)
        number_of_children = len(self.children)
        new_id = node_id + 1
        for i in range(number_of_children):
            new_id = self.children[i].createNetworkGraphForVisualization(graph, new_id, node_id, node_labels)
        return new_id + 1
    
    def generateBTreeVisualisation(self):
        '''
        This method generates a visualization for the graph starting at this root node
        '''

        options = {"node_size": 800, "alpha": 1, "font_color":"whitesmoke", "font_size":12}
        bright_palette = sns.hls_palette(h=.5)
        directional_graph = nx.DiGraph()
        node_labels = {}
        fig, axes = plt.subplots(1, 1, layout='constrained')
        fig.set_figwidth(8)
        fig.set_figheight(6)
        fig.canvas.manager.set_window_title(f'BTree_Visualization') 
        self.createNetworkGraphForVisualization(directional_graph, 0, -1, node_labels)
        positions = nx.nx_agraph.graphviz_layout(directional_graph, prog="dot")
        nx.draw(directional_graph, pos=positions, with_labels=True, labels=node_labels, node_color="none",  bbox=dict(facecolor=bright_palette[1], edgecolor='black'), **options)
        axes.margins(0.1)
        plt.axis("off")
        plt.show()

if __name__ == '__main__':
    key_list = [1, 5, 2, 4, 3, 9, 15, -5, 12, 18, 80, -25, 22, 31, -15]
    btree_root_node = BTreeNode(minimum_key_count=2, is_root_node=True, debug=True)
    for key in key_list:
        btree_root_node = btree_root_node.addNewKey(key)
    btree_root_node.generateBTreeVisualisation()
    btree_root_node = btree_root_node.addNewKey(-2)
    btree_root_node = btree_root_node.addNewKey(71)
    btree_root_node.generateBTreeVisualisation()
    btree_root_node = btree_root_node.addNewKey(29)
    btree_root_node = btree_root_node.addNewKey(16)
    btree_root_node.generateBTreeVisualisation()