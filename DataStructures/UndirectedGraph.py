import pandas as pd

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
            parent : int
                The parent node's number (default is None)
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
        self.connected_nodes = []

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

    def printNode(self):
        '''
        This method prints out the current information for this node
        '''

        print(f"Node {self.number} is connected to nodes {self.connected_nodes}")
        if self.parent != None or self.discovered_time != None or self.finished_time != None:
            print(f"Parent: {self.parent} Discovered Time: {self.discovered_time} Finished Time: {self.finished_time}")

    
    
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

        self.back_edges = []

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

    def setAsBreadthFirst(self):
        '''
        This method resets the traversal information and sets the graph to be traversed breadth first
        '''

        self.resetTraversalInformation()
        self.breadth_first = True

    def setAsDepthFirst(self):
        '''
        This method resets the traversal information and sets the graph to be traversed depth first
        '''

        self.resetTraversalInformation()
        self.breadth_first = False

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

        for node_number in range(0,self.number_of_nodes):
            self.nodes[node_number].resetTraversalInformation()

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

    def printGraph(self):
        '''
        This method prints the grapf at this time
        '''

        if self.breadth_first:
            print(f"The graph is being traversed breadth first and has {self.number_of_nodes} nodes")
        else:
            print(f"The graph is being traversed depth first and has {self.number_of_nodes} nodes")

        for node_number in range(0,self.number_of_nodes):
            node = self.nodes[node_number]
            node.printNode()
        
    def node_visit(self, node_number):
        '''
        This method is a recursive method to visit all nodes after this point based on whether the current traversal style is breadth first or depth first
        
        Parameters :
            node_number : int
                The number of the node the traversal is starting at
        '''

        node = self.nodes[node_number]
        
        if node.discovered_time == None:
            node.discovered_time = self.getCounter()
            self.incrementCounter()

        connected_node_numbers = node.connected_nodes

        if self.breadth_first:
            visit_list = []
            for neighbor_number in connected_node_numbers:
                neighbor = self.nodes[neighbor_number]
                if neighbor.discovered_time == None:
                    visit_list.append(neighbor_number)
                    neighbor.discovered_time = self.getCounter()
                    neighbor.parent = node.number
                    self.incrementCounter()
                elif neighbor.finished_time == None:
                    self.back_edges.append((node.number,neighbor.number))
            for neighbor_number in visit_list:
                self.node_visit(neighbor_number)

        else:
            for neighbor_number in connected_node_numbers:    
                neighbor = self.nodes[neighbor_number]
                if neighbor.discovered_time == None:
                    neighbor.parent = node.number
                    self.node_visit(neighbor_number)

                elif neighbor.finished_time == None:
                    self.back_edges.append((node.number,neighbor.number))

        node.finished_time = self.getCounter()
        self.incrementCounter()

    def printTraversalDataTable(self):
        '''
        This method outputs the traversal data in a table
        '''

        table = self.getTraversalTable()

        print(table)

    def getTraversalTable(self):
        '''
        This method creates a table of the current traveral information
        '''

        node_numbers = []
        node_parents = []
        node_discovered_times = []
        node_finished_times = []

        for node_number in range(0,self.number_of_nodes):
            node = self.nodes[node_number]

            node_numbers.append(node_number)
            node_parents.append(node.parent)
            node_discovered_times.append(node.discovered_time)
            node_finished_times.append(node.finished_time)
        
        data_dictionary ={
            "Node":node_numbers,
            "Parent":node_parents,
            "Discovered":node_discovered_times,
            "Finished":node_finished_times
        }
        table = pd.DataFrame.from_dict(data_dictionary)
        return table

if __name__ == '__main__':

    edge_list = [(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(1,6),(6,3),(2,4),(2,5)]   
    undirected_graph = UndirectedGraph(7,edge_list=edge_list, debug=True)
    undirected_graph.printGraph()
    undirected_graph.node_visit(0)
    undirected_graph.printGraph()
    
    breadth_table = undirected_graph.getTraversalTable()
    
    undirected_graph.setAsDepthFirst()
    undirected_graph.node_visit(0)
    undirected_graph.printGraph()

    depth_table = undirected_graph.getTraversalTable()

    print("Breadth First Traversal Table")
    print(breadth_table)
    print("\nDepth First Traveral Table")
    print(depth_table)
