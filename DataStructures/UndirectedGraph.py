import pandas as pd

class GraphNode():
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

    
    
class Graph():
    '''
    This class contains the undirected graph data structure
    '''

    def __init__(self, number_of_nodes, edge_list=[], breadth_first=True, directed=False, debug=False):
        '''
        This method initializes the node for the directed or undirected graph

        Parameters :
            number_of_nodes : int
                The number of nodes in the graph
            edge_list : [(int,int)]
                The edges in the graph
            breadth_first : Boolean
                Whether the traversal shall be breadth first rather than depth first (default is True)
            directed : Boolean
                Whether the graph is created as a directed or undirected graph
            debug : Boolean
                Whether the print statements should be more informative to allow debugging (default is False)
        '''

        self.number_of_nodes = number_of_nodes
        self.breadth_first = breadth_first
        self.directed = directed
        self.debug = debug
        self.counter = 0

        self.back_edges = []

        self.nodes = {}
        for i in range(0, self.number_of_nodes):
            self.nodes[i] = GraphNode(i, debug=self.debug)

        self.addEdges(edge_list=edge_list)

        if self.debug:
            print(f"Created: ", end=" ")
            self.printGraphSummary()

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
        if not self.directed:
            self.nodes[end].addConnectedNode(start)

        if(self.debug):
            directed_or_undirected = "a directed" if self.directed else "an undirected"
            print(f"Added {directed_or_undirected} connection between node {start} and node {end}")
    
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

        self.printGraphSummary()

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

        Returns :
            traversal_table : DataFrame
                A Dataframe containing the information about the graphs traversal
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
    
    def traverseGraph(self):
        '''
        This method traverses the entire graph by visiting each node which was not previously visited

        Returns :
            traversal_table : DataFrame
                A Dataframe containing the information about the graphs traversal
        '''

        self.resetTraversalInformation()
        if self.debug:
            if self.breadth_first:
                print("Traversing graph breadth first")
            else:
                print("Traversing graph depth first")

        for node_number in range(0, self.number_of_nodes):
            node = self.nodes[node_number]
            if node.discovered_time == None:
                self.node_visit(node_number)

        return self.getTraversalTable()
    
    def getIndependantSegmentCount(self):
        '''
        This method counts how many unconnected segments are in a graph which has already been traversed

        Returns :
            segments_counted : int
                The number of independant segments in the graph
        '''

        segments_counted = 0
        for node_number in range(0, self.number_of_nodes):
            node = self.nodes[node_number]
            if node.parent == None:
                segments_counted += 1
        return segments_counted
    
    def getUnvisitedNodes(self):
        '''
        This method counts how many unvisited nodes are in a graph

        Returns :
            unvisited_nodes : [int]
                The list of unvisited nodes in the graph
        '''

        unvisited_nodes = []
        for node_number in range(0, self.number_of_nodes):
            node = self.nodes[node_number]
            if node.discovered_time == None:
                unvisited_nodes.append(node_number)
        return unvisited_nodes
    
    
    def getNodeDiscoveredTime(self, node_number):
        '''
        This method gets the discovered time of a given node

        Parameters :
            node_number : int
                The number of the node

        Returns : 
            discovered_time : int
                The counter value when the node was discovered
        '''

        return self.nodes[node_number].discovered_time
    
    def getNodeParent(self, node_number):
        '''
        This method gets the parent node number of a given node

        Parameters :
            node_number : int
                The number of the node

        Returns : 
            parent : int
                The node number of the parent node
        '''

        return self.nodes[node_number].parent

    def getNodeFinishedTime(self, node_number):
        '''
        This method gets the finished time of a given node

        Parameters :
            node_number : int
                The number of the node

        Returns : 
            discovered_time : int
                The counter value when the node was finished
        '''

        return self.nodes[node_number].finished_time
        
    def printGraphSummary(self):
        '''
        This method prints out a summary of the current graph object
        '''

        if self.directed:
            print("A directed", end=" ")
        else:
            print("An undirected", end=" ")

        print(f"graph with {self.number_of_nodes} nodes that is",end=" ")
        if self.breadth_first:
            print("in breadth first traversal mode.")
        else:
            print("in depth first traversal mode.")

if __name__ == '__main__':

    edge_list = [(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(1,6),(6,3),(2,4),(2,5)]   
    undirected_graph = Graph(7,edge_list=edge_list, debug=True)
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

    extended_edge_list = [(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(1,6),(6,3),(2,4),(2,5),(7,8),(8,9),(9,7)]
    second_undirected_graph = Graph(10, edge_list=extended_edge_list, debug=True)
    second_undirected_graph.node_visit(0)
    node_visit_table = second_undirected_graph.getTraversalTable()

    traverse_graph_table = second_undirected_graph.traverseGraph()

    print("First Node Visit Table")
    print(node_visit_table)
    print("\nTraverse Graph Table")
    print(traverse_graph_table)

    print(f"The original graph has {undirected_graph.getIndependantSegmentCount()} independant segments")
    print(f"The second graph has {second_undirected_graph.getIndependantSegmentCount()} independant segments")

    directed_edge_list = [(0,1),(2,1),(2,3),(3,4),(4,5),(5,6),(1,6),(6,3),(2,4),(2,5)]   

    directed_graph = Graph(7,edge_list=directed_edge_list, directed=True, debug=True)
    undirected_graph = Graph(7,edge_list=directed_edge_list, directed=False, debug=True)

    undirected_graph_table = undirected_graph.traverseGraph()
    directed_graph_table = directed_graph.traverseGraph()

    print(undirected_graph_table)
    print(directed_graph_table)