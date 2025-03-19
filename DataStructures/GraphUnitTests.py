import unittest
from UndirectedGraph import Graph,GraphNode

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
        self.number_of_nodes = 10

    def test_undirected_first_node_travel_breadth(self):
        '''
        This method tests undirected breadth first travel from the first node
        '''

        graph = Graph(number_of_nodes=self.number_of_nodes, edge_list=self.edge_list, breadth_first=True, directed=False, debug=False)
        
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

        graph = Graph(number_of_nodes=self.number_of_nodes, edge_list=self.edge_list, breadth_first=True, directed=True, debug=False)
        
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

        graph = Graph(number_of_nodes=self.number_of_nodes, edge_list=self.edge_list, breadth_first=False, directed=False, debug=False)
        
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

        graph = Graph(number_of_nodes=self.number_of_nodes, edge_list=self.edge_list, breadth_first=False, directed=True, debug=False)
        
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

        graph = Graph(number_of_nodes=self.number_of_nodes, edge_list=self.edge_list, breadth_first=False, directed=True, debug=False)
        
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

        graph = Graph(number_of_nodes=self.number_of_nodes, edge_list=self.edge_list, breadth_first=False, directed=False, debug=False)
        
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

        graph = Graph(number_of_nodes=self.number_of_nodes, edge_list=self.edge_list, breadth_first=True, directed=False, debug=False)
        
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

        graph = Graph(number_of_nodes=self.number_of_nodes, edge_list=self.edge_list, breadth_first=True, directed=True, debug=False)
        
        self.assertEqual(len(graph.getUnvisitedNodes()),10)

        traversal_table = graph.traverseGraph()

        print("Directed breadth first traversed")
        print(traversal_table)

        unvisited_nodes = graph.getUnvisitedNodes()
        self.assertEqual(len(unvisited_nodes),0)
        self.assertEqual(graph.getNodeDiscoveredTime(6),2)
        self.assertEqual(graph.getIndependantSegmentCount(),4)


if __name__ == '__main__':
    unittest.main()