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

class GraphEdgeWithWeight():
    '''
    This class contains the details for each edge in a weighted graph
    '''

    def __init__(self, start_node, end_node, weight, edge_id, directed=False):
        '''
        This method initializes the Graph Edge object

        Parameters :
            start_node : int
                The number of the node the edge starts at
            end_node : int 
                The number of the node the edge ends at
            weight : int
                The weight for the edge
            edge_id : int
                The edge id
            directed : Boolean 
                Whether this edge has a direction
        '''
        self.start_node = start_node
        self.end_node = end_node
        self.weight = weight
        self.directed = directed
        self.edge_id = edge_id

    def getStartNode(self):
        '''
        This method returns the start of the edge

        Returns : 
            start_node : int 
                The node that the edge begins at
        '''

        return self.start_node
    
    def getEndNode(self):
        '''
        This method returns the end of the edge

        Returns :
            end_node : int
                The node that the edge ends at
        '''

        return self.end_node
    
    def getWeight(self):
        '''
        This method returns the edge's weight

        Returns : 
            weight : int
                The weight of this edge
        '''

        return self.weight
    
    def printEdge(self):
        '''
        This method prints the description for this edge
        '''

        print(f"The edge from {self.start_node} to {self.end_node} with {self.weight} weight")

    def printEdgeAbbreviated(self):
        '''
        This method prints the abbreviated edge summary
        '''

        print(f"{self.edge_id}: (s={self.start_node}, e={self.end_node}, w={self.weight})", end= " ")

    def getStartEndWeight(self):
        '''
        This method returns a tuple of the start_node, end_node and weight

        Returns:
            edge_dimensions : (int, int, int)
                The start node, end node and weight for the route
        '''

        return self.start_node, self.end_node, self.weight
    
class Graph():
    '''
    This class contains the undirected graph data structure
    '''

    def __init__(self, number_of_nodes, edge_list=[], is_breadth_first=True, is_directed=False, is_weighted=False, is_debug=False):
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
        self.is_breadth_first = is_breadth_first
        self.is_directed = is_directed
        self.is_weighted = is_weighted

        self.is_debug = is_debug

        self.counter = 0

        self.back_edges = []

        self.nodes = {}
        for i in range(0, self.number_of_nodes):
            self.nodes[i] = GraphNode(i, debug=self.is_debug)

        self.weighted_edges = []
        self.addEdges(edge_list=edge_list)

        if self.is_debug:
            print(f"Created: ", end=" ")
            self.printGraphSummary()

    def setAsBreadthFirst(self):
        '''
        This method resets the traversal information and sets the graph to be traversed breadth first
        '''

        self.resetTraversalInformation()
        self.is_breadth_first = True

    def setAsDepthFirst(self):
        '''
        This method resets the traversal information and sets the graph to be traversed depth first
        '''

        self.resetTraversalInformation()
        self.is_breadth_first = False

    def addEdges(self, edge_list):
        '''
        This method adds edges to the graph

        Parameters : 
            edge_list : []
                The list of edges to be added to the graph as tuples
        '''

        for edge in edge_list:
            if self.is_weighted :
                start, end, weight = edge
                self.addWeightedEdge(start=start, end=end, weight=weight)
            else :
                start, end = edge
                self.addUnweightedEdge(start=start,end=end)

    def addWeightedEdge(self,start,end,weight):
        '''
        This method adds a weighted connection between two nodes to the graph

        Parameters :
            start : int 
                The first node in the connection
            end : int
                The second node in the connection
            weight : int
                The weight of the edge
        '''
        edge_id = len(self.weighted_edges)
        self.weighted_edges.append(GraphEdgeWithWeight(start_node=start, end_node=end, weight=weight, edge_id=edge_id))
        self.addUnweightedEdge(start=start,end=end)

    def addUnweightedEdge(self, start, end):
        '''
        This method adds a connection between two nodes to the graph

        Parameters :
            start : int 
                The first node in the connection
            end : int
                The second node in the connection
        '''

        self.nodes[start].addConnectedNode(end)
        if not self.is_directed:
            self.nodes[end].addConnectedNode(start)

        if(self.is_debug):
            directed_or_undirected = "a directed" if self.is_directed else "an undirected"
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

        if self.is_breadth_first:
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
        if self.is_debug:
            if self.is_breadth_first:
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

        if self.is_directed:
            print("A directed", end=" ")
        else:
            print("An undirected", end=" ")

        print(f"graph with {self.number_of_nodes} nodes that is",end=" ")
        if self.is_breadth_first:
            print("in breadth first traversal mode.")
        else:
            print("in depth first traversal mode.")

    def printWeightedEdges(self):
        '''
        This method prints the weighted edges

        It relies on the edges being weighted
        '''

        assert self.is_weighted
        for weighted_edge in self.weighted_edges:
            weighted_edge.printEdge()
        
    def printWeightEdgesAbbreviated(self):
        '''
        This method prints the weighted edges in an abbreviated form

        It relies on the edges being weighted
        '''

        assert self.is_weighted
        for weighted_edge in self.weighted_edges:
            weighted_edge.printEdgeAbbreviated()
        print()

    def sortWeightedEdges(self):
        '''
        This method sorts the weighted edges in ascending order by weight

        It relies on the edges being weighted
        '''

        assert self.is_weighted
        self.weighted_edges = sorted(self.weighted_edges, key=lambda edg_data: edg_data.weight)

    def shortestPathUsingBellmanFord(self, start_node):
        '''
        This method calculates the shortest distance from a starting node to every other node using the bellman ford algorithm

        It relies on the graph being weighted

        Parameters :
            start_node : int
                The node that each node's distance is being calculated from
        
        Returns :
            distances_to_nodes : [int]
                The list of the distance from the starting node to every other node
        '''

        assert self.is_weighted

        distances_to_nodes = []
        for _ in range(0,self.number_of_nodes):
            distances_to_nodes.append(None)

        distances_to_nodes[start_node] = 0

        for i in range(0,self.number_of_nodes):
            for edge in self.weighted_edges:
                start_node, end_node, weight = edge.getStartEndWeight()
                if distances_to_nodes[start_node] != None and ( (distances_to_nodes[end_node]!= None and distances_to_nodes[start_node] + weight < distances_to_nodes[end_node]) or distances_to_nodes[end_node] == None) :
                    distances_to_nodes[end_node] = distances_to_nodes[start_node] + weight
                if not self.is_directed :
                    if distances_to_nodes[end_node] != None and ( (distances_to_nodes[start_node]!= None and distances_to_nodes[end_node] + weight < distances_to_nodes[start_node]) or distances_to_nodes[start_node] == None) :
                        distances_to_nodes[start_node] = distances_to_nodes[end_node] + weight
    
        return distances_to_nodes

if __name__ == '__main__':

    edge_list = [(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(1,6),(6,3),(2,4),(2,5)]   
    undirected_graph = Graph(7,edge_list=edge_list, is_debug=True)
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
    second_undirected_graph = Graph(10, edge_list=extended_edge_list, is_debug=True)
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

    directed_graph = Graph(7,edge_list=directed_edge_list, is_directed=True, is_debug=True)
    undirected_graph = Graph(7,edge_list=directed_edge_list, is_directed=False, is_debug=True)

    undirected_graph_table = undirected_graph.traverseGraph()
    directed_graph_table = directed_graph.traverseGraph()

    print("The table of the undirected graph traversal data:")
    print(undirected_graph_table)
    print("The table of the directed graph traversal data:")

    print(directed_graph_table)

    weighted_edge_list = [(0,1,1),(2,1,2),(2,3,1),(3,4,1),(4,5,2),(5,6,1),(1,6,4),(6,3,1),(2,4,1),(2,5,3)]

    weighted_graph = Graph(7,edge_list=weighted_edge_list,is_directed=False,is_weighted=True)
    weighted_graph_table = weighted_graph.traverseGraph()

    print("\nThe table of the undirected weighted graph traversal data:")
    print(weighted_graph_table)

    weighted_directed_graph = Graph(7,edge_list=weighted_edge_list,is_directed=True,is_weighted=True)

    print("\nThe shortest distance to each node using bellman ford from node 0:")

    bellman_ford_distances = weighted_graph.shortestPathUsingBellmanFord(0)
    bellman_ford_directed_distances = weighted_directed_graph.shortestPathUsingBellmanFord(0)

    bellman_ford_dictionary = {
        "Destination Node": [0,1,2,3,4,5,6],
        "Undirected Distance":bellman_ford_distances,
        "Directed Distance": bellman_ford_directed_distances
    }
    bellman_ford_dataframe = pd.DataFrame.from_dict(bellman_ford_dictionary)
    print(bellman_ford_dataframe)

    print("\nThe shortest distance to each node using bellman ford from node 3:")

    bellman_ford_distances = weighted_graph.shortestPathUsingBellmanFord(3)
    bellman_ford_directed_distances = weighted_directed_graph.shortestPathUsingBellmanFord(3)

    bellman_ford_dictionary = {
        "Destination Node": [0,1,2,3,4,5,6],
        "Undirected Distance":bellman_ford_distances,
        "Directed Distance": bellman_ford_directed_distances
    }
    bellman_ford_dataframe = pd.DataFrame.from_dict(bellman_ford_dictionary)
    print(bellman_ford_dataframe)