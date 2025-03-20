import unittest
from Graph import Graph, GraphNode

class GraphUnitTests(unittest.TestCase):
    '''
    This class contains basic unit tests for the graph data structue
    '''

    def setUp(self):
        '''
        This method sets up the edge list to be used with the following unit tests

        Number of nodes : 10
        Number of edges : 13
        '''

        self.edge_list = [(0,1),(2,1),(2,3),(3,4),(4,5),(5,6),(1,6),(6,3),(2,4),(2,5),(7,8),(9,8),(9,7)]   
        self.weighted_edge_list = [(0,1,2),(2,1,1),(2,3,4),(3,4,6),(4,5,3),(5,6,2),(1,6,1),(6,3,3),(2,4,4),(2,5,2),(7,8,5),(9,8,2),(9,7,1)]   

        self.number_of_nodes = 10

    def test_undirected_first_node_travel_breadth(self):
        '''
        This method tests undirected breadth first travel from the first node
        '''

        graph = Graph(number_of_nodes=self.number_of_nodes, edge_tuples=self.edge_list, is_breadth_first=True, is_directed=False, is_debug=False)
        
        self.assertEqual(len(graph.getUnvisitedNodes()),10)

        graph.node_visit(0)
        traversal_table = graph.getTraversalTable()

        print("Undirected breadth first travel from the first node")
        print(traversal_table)

        unvisited_nodes = graph.getUnvisitedNodes()
        self.assertEqual(len(unvisited_nodes),3)
        self.assertListEqual(unvisited_nodes,[7,8,9])
        self.assertEqual(graph.getNodeDiscoveredTime(6),3)


    def test_directed_first_node_travel_breadth(self):
        '''
        This method tests directed breadth first travel from the first node
        '''

        graph = Graph(number_of_nodes=self.number_of_nodes, edge_tuples=self.edge_list, is_breadth_first=True, is_directed=True, is_debug=False)
        
        self.assertEqual(len(graph.getUnvisitedNodes()),10)

        graph.node_visit(0)
        traversal_table = graph.getTraversalTable()

        print("Directed breadth first travel from the first node")
        print(traversal_table)

        unvisited_nodes = graph.getUnvisitedNodes()
        self.assertEqual(len(unvisited_nodes),4)
        self.assertListEqual(unvisited_nodes,[2,7,8,9])
        self.assertEqual(graph.getNodeDiscoveredTime(6),2)


    def test_undirected_first_node_travel_depth(self):
        '''
        This method tests directed breadth first travel from the first node
        '''

        graph = Graph(number_of_nodes=self.number_of_nodes, edge_tuples=self.edge_list, is_breadth_first=False, is_directed=False, is_debug=False)
        
        self.assertEqual(len(graph.getUnvisitedNodes()),10)

        graph.node_visit(0)
        traversal_table = graph.getTraversalTable()

        print("Undirected depth first travel from the first node")
        print(traversal_table)

        unvisited_nodes = graph.getUnvisitedNodes()
        self.assertEqual(len(unvisited_nodes),3)
        self.assertListEqual(unvisited_nodes,[7,8,9])
        self.assertEqual(graph.getNodeDiscoveredTime(6),6)

    def test_directed_first_node_travel_depth(self):
        '''
        This method tests directed depth first travel from the first node
        '''

        graph = Graph(number_of_nodes=self.number_of_nodes, edge_tuples=self.edge_list, is_breadth_first=False, is_directed=True, is_debug=False)
        
        self.assertEqual(len(graph.getUnvisitedNodes()),10)

        graph.node_visit(0)
        traversal_table = graph.getTraversalTable()

        print("Directed depth first travel from the first node")
        print(traversal_table)

        unvisited_nodes = graph.getUnvisitedNodes()
        self.assertEqual(len(unvisited_nodes),4)
        self.assertListEqual(unvisited_nodes,[2,7,8,9])
        self.assertEqual(graph.getNodeDiscoveredTime(6),2)

    def test_directed_traversed_depth(self):
        '''
        This method tests directed depth first travered
        '''

        graph = Graph(number_of_nodes=self.number_of_nodes, edge_tuples=self.edge_list, is_breadth_first=False, is_directed=True, is_debug=False)
        
        self.assertEqual(len(graph.getUnvisitedNodes()),10)

        traversal_table = graph.traverseGraph()

        print("Directed depth first traversed")
        print(traversal_table)

        unvisited_nodes = graph.getUnvisitedNodes()
        self.assertEqual(len(unvisited_nodes),0)
        self.assertEqual(graph.getNodeDiscoveredTime(6),2)
        self.assertEqual(graph.getIndependantSegmentCount(),4)

    def test_undirected_traversed_depth(self):
        '''
        This method tests undirected depth first travered
        '''

        graph = Graph(number_of_nodes=self.number_of_nodes, edge_tuples=self.edge_list, is_breadth_first=False, is_directed=False, is_debug=False)
        
        self.assertEqual(len(graph.getUnvisitedNodes()),10)

        traversal_table = graph.traverseGraph()

        print("Undirected depth first traversed")
        print(traversal_table)

        unvisited_nodes = graph.getUnvisitedNodes()
        self.assertEqual(len(unvisited_nodes),0)
        self.assertEqual(graph.getNodeDiscoveredTime(6),6)
        self.assertEqual(graph.getIndependantSegmentCount(),2)

    def test_undirected_traversed_breadth(self):
        '''
        This method tests undirected breadth first travered
        '''

        graph = Graph(number_of_nodes=self.number_of_nodes, edge_tuples=self.edge_list, is_breadth_first=True, is_directed=False, is_debug=False)
        
        self.assertEqual(len(graph.getUnvisitedNodes()),10)

        traversal_table = graph.traverseGraph()

        print("Undirected breadth first traversed")
        print(traversal_table)

        unvisited_nodes = graph.getUnvisitedNodes()
        self.assertEqual(len(unvisited_nodes),0)
        self.assertEqual(graph.getNodeDiscoveredTime(6),3)
        self.assertEqual(graph.getIndependantSegmentCount(),2)

    def test_directed_traversed_breadth(self):
        '''
        This method tests directed breadth first travered
        '''

        graph = Graph(number_of_nodes=self.number_of_nodes, edge_tuples=self.edge_list, is_breadth_first=True, is_directed=True, is_debug=False)
        
        self.assertEqual(len(graph.getUnvisitedNodes()),10)

        traversal_table = graph.traverseGraph()

        print("Directed breadth first traversed")
        print(traversal_table)

        unvisited_nodes = graph.getUnvisitedNodes()
        self.assertEqual(len(unvisited_nodes),0)
        self.assertEqual(graph.getNodeDiscoveredTime(6),2)
        self.assertEqual(graph.getIndependantSegmentCount(),4)

    def test_unweighted_directed_bellman(self):
        '''
        This method tests bellman using an unweighted, directed graph
        '''

        graph = Graph(number_of_nodes=self.number_of_nodes, edge_tuples=self.edge_list, is_breadth_first=True, is_directed=True, is_debug=False)
        
        distances, parents = graph.shortestPathUsingBellmanFord(0)

        self.assertListEqual(parents, [None, 0, None, 6, 3, 4, 1, None, None, None])
        self.assertListEqual(distances, [0, 1, None, 3, 4, 5, 2, None, None, None])

    def test_unweighted_undirected_bellman(self):
        '''
        This method tests bellman using an unweighted, undirected graph
        '''

        graph = Graph(number_of_nodes=self.number_of_nodes, edge_tuples=self.edge_list, is_breadth_first=True, is_directed=False, is_debug=False)
        
        distances, parents = graph.shortestPathUsingBellmanFord(0)

        self.assertListEqual(parents, [None, 0, 1, 2, 2, 2, 1, None, None, None])
        self.assertListEqual(distances, [0, 1, 2, 3, 3, 3, 2, None, None, None])

    def test_weighted_directed_bellman(self):
        '''
        This method tests bellman using a weighted, directed graph
        '''

        graph = Graph(number_of_nodes=self.number_of_nodes, edge_tuples=self.weighted_edge_list, is_breadth_first=True, is_directed=True, is_weighted=True, is_debug=False)
        
        distances, parents = graph.shortestPathUsingBellmanFord(0)

        self.assertListEqual(parents, [None, 0, None, 6, 3, 4, 1, None, None, None])
        self.assertListEqual(distances, [0, 2, None, 6, 12, 15, 3, None, None, None])

    def test_weighted_undirected_bellman(self):
        '''
        This method tests bellman using a weighted, undirected graph
        '''

        graph = Graph(number_of_nodes=self.number_of_nodes, edge_tuples=self.weighted_edge_list, is_breadth_first=True, is_directed=False, is_weighted=True, is_debug=False)
        
        distances, parents = graph.shortestPathUsingBellmanFord(0)

        self.assertListEqual(parents, [None, 0, 1, 6, 2, 2, 1, None, None, None])
        self.assertListEqual(distances, [0, 2, 3, 6, 7, 5, 3, None, None, None])

    def test_weighted_undirected_bellman_negative_edge(self):
        '''
        This method tests bellman using a weighted, undirected graph with a negative loop
        '''
        negative_edge_loop_edges = [(0,1,1),(1,2,-1),(0,2,1)]
        graph = Graph(number_of_nodes=3, edge_tuples=negative_edge_loop_edges, is_breadth_first=True, is_directed=False, is_weighted=True, is_debug=False)
        
        distances, parents = graph.shortestPathUsingBellmanFord(0)

        self.assertEqual(parents, None)
        self.assertEqual(distances, None)

if __name__ == '__main__':
    unittest.main()