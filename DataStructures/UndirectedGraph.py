class UndirectedGraphNode():
    '''
    This class is a node for the undirected graph data structure
    '''
    def __init__(self, number, parent = None, discovered_time = None, finished_time = None, debug=False):
        '''
        This method initializes the node for the undirected graph

        Parameters :
            number : int
                The node's number
            parent : UndirectedGraphNode
                The parent node (default is None)
            discovered_time : int
                The counter time when the node was discovered (default is None)
            finished_time : int
                The counter time when the node was finished (default is None)
            debug : Boolean
                Whether the print statements should be more informative to allow debugging (default is False)
        '''

        self.number = number
        self.parent = parent
        self.discovered_time = discovered_time
        self.finished_time = finished_time
        self.debug = debug

    def resetTraversalInformation(self):
        '''
        This method resets all the information for the node generated during the traversal
        '''

        self.parent = None
        self.discovered_time = None
        self.finished_time = None

    
class UndirectedGraph():
    '''
    This class contains the undirected graph data structure
    '''

    def __init__(self, number_of_nodes, breadth_first=True, debug=False):
        '''
        This method initializes the node for the undirected graph

        Parameters :
            number : int
                The node's number
            parent : int
                The number of the parent node
            breadth_first : None
                Whether the traversal shall be breadth first rather than depth first (default is True)
            debug : Boolean
                Whether the print statements should be more informative to allow debugging (default is False)
        '''

        self.number_of_nodes = number_of_nodes
        self.breadth_first = breadth_first
        self.debug = debug
        self.counter = 0

        self.nodes = []
        for i in range(0,self.number_of_nodes):
            self.nodes.append(UndirectedGraphNode(i, debug=self.debug))

        if self.debug:
            print(f"Created a graph with {number_of_nodes} nodes that is",end=" ")
            if self.breadth_first:
                print("in breadth first traversal mode.")
            else:
                print("in depth first traversal mode.")
    
    def resetTraversalInformation(self):
        '''
        This method resets the traversal information for all of the nodes
        '''

        for node in self.nodes:
            node.resetTraversalInformation()

        self.resetCounter()

    def getCounter(self):
        '''
        This method returns the current counter value for the graph

        Returns : 
            counter : int 
                The current value of the counter for this graph
        '''

        return self.counter
    
    def incrementCounter(self):
        '''
        This method increments the graph's counter by one
        '''

        self.counter += 1

    def resetCounter(self):
        '''
        This method resets the graph's counter to 0
        '''

        self.counter = 0

if __name__ == '__main__':
    undirected_graph = UndirectedGraph(6, debug=True)