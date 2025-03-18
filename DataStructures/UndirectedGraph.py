class UndirectedGraphNode():
    '''
    This class is a node for the undirected graph data structure
    '''
    def __init__(self, number, parent = None, connected_nodes=[], discovered_time = None, finished_time = None, debug=False):
        '''
        This method initializes the node for the undirected graph

        Parameters :
            number : int
                The node's number
            parent : int
                The parent node's number (default is None)
            connected_nodes : [int]
                The numbers of any connected nodes
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
        self.connected_nodes = connected_nodes

    def addConnectedNode(self, connected_node):
        '''
        This method adds a connected node to this node, creating an edge
        '''
        if connected_node not in self.connected_nodes:
            self.connected_nodes.append(connected_node)

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

    def __init__(self, number_of_nodes, edge_list=[], breadth_first=True, debug=False):
        '''
        This method initializes the node for the undirected graph

        Parameters :
            number_of_nodes : int
                The number of nodes in the graph
            edge_list : [(int,int)]
                The edges in the graph
            breadth_first : Boolean
                Whether the traversal shall be breadth first rather than depth first (default is True)
            debug : Boolean
                Whether the print statements should be more informative to allow debugging (default is False)
        '''

        self.number_of_nodes = number_of_nodes
        self.breadth_first = breadth_first
        self.debug = debug
        self.counter = 0

        self.nodes = {}
        for i in range(0, self.number_of_nodes):
            self.nodes[i] = UndirectedGraphNode(i, debug=self.debug)

        self.addEdges(edge_list=edge_list)

        if self.debug:
            print(f"Created a graph with {number_of_nodes} nodes that is",end=" ")
            if self.breadth_first:
                print("in breadth first traversal mode.")
            else:
                print("in depth first traversal mode.")

    def addEdges(self, edge_list):
        '''
        This method adds edges to the graph

        Parameters : 
            edge_list : []
                The list of edges to be added to the graph as tuples
        '''

        for edge in edge_list:
            start, end = edge
            self.addAnEdge(start=start,end=end)

    def addAnEdge(self, start, end):
        '''
        This method adds a connection between two nodes to the graph

        Parameters :
            start : int 
                The first node in the connection
            end : int
                The second node in the connection
        '''

        self.nodes[start].addConnectedNode(end)
        self.nodes[end].addConnectedNode(start)
        if(self.debug):
            print(f"Added a connection between node {start} and node {end}")
    
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

    edge_list = [(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(1,6),(6,3),(2,4),(2,5)]   
    undirected_graph = UndirectedGraph(7,edge_list=edge_list, debug=True)