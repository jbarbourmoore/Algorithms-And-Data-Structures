import networkx as nx
from matplotlib import pyplot as plt 
import seaborn as sns

class MaxCutProblem():
    '''
    This class finds the best way to "cut" a set into two, such that each node has adjacent nodes that are in the other set.
    '''

    def __init__( self, number_of_nodes, edge_list ):
        '''
        This method initializes the MaxCutProblem

        Parameters : 
            number_of_nodes : int
                The number of nodes in the set
            edge_list : [int]
                The edges between the nodes
        '''
        self.number_of_nodes = number_of_nodes
        self.edge_list = edge_list
        self.set_list = [True] * self.number_of_nodes

    def findBalancedCut(self): 
        '''
        This method utilizes a greedy algorithm to split the list into two such that each node
        has at least one adjacent node which is in the opposite set
        '''
        
        self.set_list = [True if i < self.number_of_nodes/2 else False for i in range(number_of_nodes)]
        imbalanced_vertices = self.findUnbalancedNodes()
        while len(imbalanced_vertices) != 0:
            self.set_list[imbalanced_vertices[0]] = not self.set_list[imbalanced_vertices[0]]
            imbalanced_vertices = self.findUnbalancedNodes()
        
    def findUnbalancedNodes(self):
        '''
        This method returns a list of all nodes which do not have an adjacent node in the other set
        '''

        unbalanced_nodes = [i for i in range(0,self.number_of_nodes)]

        for edge in self.edge_list:
            i, j = edge
            if self.set_list[i] != self.set_list[j]:
                if i in unbalanced_nodes:
                    unbalanced_nodes.remove(i)
                if j in unbalanced_nodes:
                    unbalanced_nodes.remove(j)
        return unbalanced_nodes

    def drawCutSets(self):
        '''
        This method creates the graphical representation of the cut set
        '''

        options = {"edgecolors": "tab:gray", "node_size": 800, "alpha": 1, "font_color":"whitesmoke", "font_size":16}
        bright_palette = sns.hls_palette(h=.5)
        edge_list_cut = [(i,j) for (i,j) in self.edge_list if self.set_list[i] != self.set_list[j] ]
        graph_visualization = nx.Graph()
        graph_visualization.add_nodes_from(range(self.number_of_nodes))
        color_map = [bright_palette[1] if self.set_list[j] == True else bright_palette[0] for j in range(self.number_of_nodes)]
        graph_visualization.add_edges_from(self.edge_list)
        position_mapping = nx.spring_layout(graph_visualization, seed=1234)
        plt.figure()
        nx.draw(graph_visualization, pos=position_mapping, node_color=color_map, with_labels=True, **options)
        nx.draw_networkx_edges(graph_visualization, position_mapping, width=2, edgelist=edge_list_cut, edge_color=bright_palette[2])
        plt.show()


number_of_nodes = 5
edge_list = [(0,1), (0,2), (0,3), (0,4), (1,2), (1,3), (2,4), (3,4)]
max_cut_problem = MaxCutProblem(number_of_nodes, edge_list)
max_cut_problem.findBalancedCut()
max_cut_problem.drawCutSets()
