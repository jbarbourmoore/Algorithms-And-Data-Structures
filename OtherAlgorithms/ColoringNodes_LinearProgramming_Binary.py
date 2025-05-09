from pulp import *
import seaborn as sns
import networkx as nx
from matplotlib import pyplot as plt

def verifyColorAssignments( number_of_nodes, edge_list, number_of_colors, color_assignments ):
    '''
    This function verifies the generated color assignments fit the constraints

    Parameters : 
        number_of_nodes : int
            The number of nodes
        edge_list : [(int,int)]
            The list of edges
        number_of_colors = int
            The number of colors
        color_assignments = [int]
            The list of colors assigned to each node
    
    Returns 
        is_verified : Boolean
            True if the color assignments fit the constraints
    '''

    if len(color_assignments) != number_of_nodes:
        print(f"There are the wrong number of color assignments: {len(color_assignments)}")
        return False
    for color_number in color_assignments:
        if not color_number <= number_of_colors:
            print(f"One of the color_assignments has an improper value: {color_number}")
            return False
    for edge in edge_list: 
        start_node, end_node = edge
        start_node_color = color_assignments[start_node]
        end_node_color = color_assignments[end_node]
        if start_node_color == end_node_color :
            print(f"Two connected nodes have the same color : {start_node}={start_node_color} {end_node}={end_node_color}")
            return False
    print("The color assignments are valid")
    return True

class ColoringNodes():
    '''
    This class uses linear programming with binary variables to determine the color of nodes

    There are a certain number of nodes, a certain number of colors, and no two connected nodes can be the same color
    '''

    def __init__(self, number_of_nodes, edge_list, number_of_colors = 3):
        '''
        This method initializes the ColoringNodes object

        Parameters : 
        number_of_nodes : int
            The number of nodes
        edge_list : [(int,int)]
            The list of edges
        number_of_colors = int, optional
            The number of colors (default is 3)
        '''

        self.number_of_nodes = number_of_nodes
        self.edge_list = edge_list
        self.number_of_colors = number_of_colors
        self.color_list = []

    def determineColors(self):
        '''
        This method utilizes linear programming to determine the colors for each node

        Returns:
            color_list : [int]
                The list of colors assigned to each node
        '''
        
        lp_problem = LpProblem('MultipleColorAssignments', LpMinimize)

        x_colors = {}
        for c in range(0, self.number_of_colors):
            x_colors[c] = [LpVariable(f'x_color{c}_{i}', cat='Binary') for i in range(0, self.number_of_nodes)]

        lp_problem += lpSum([x_colors[c][i] for c in range(0,self.number_of_colors) for i in range(0, self.number_of_nodes)])
        for i in range(0, self.number_of_nodes):
            lp_problem+=lpSum([x_colors[c][i] for c in range(0,self.number_of_colors)]) == 1

        for edge in self.edge_list:
            i, j = edge
            for c in range(0, self.number_of_colors):
                lp_problem+= x_colors[c][i] + x_colors[c][j] <= 1
            
        status = lp_problem.solve(apis.PULP_CBC_CMD(msg=False))
        
        if status == constants.LpSolutionOptimal:
            color_list = []
            for i in range(0, self.number_of_nodes):
                color_list += [c for c in range(self.number_of_colors) if x_colors[c][i].varValue == 1]
            self.color_list = color_list
            return color_list
        else:
            print(f"Unable to assign {self.number_of_colors} colors to the graph with {self.number_of_nodes} nodes and the edges {self.edge_list}")
            return None
    
    def visualizNodeColorations(self):
        '''
        This method creates a graphical visualization of the colored nodes using matplotlib and networkx
        '''

        options = {"edgecolors": "tab:gray", "node_size": 800, "alpha": 1, "font_color":"whitesmoke", "font_size":16}
        bright_palette = sns.hls_palette(h=.5)
        graph_visualization = nx.DiGraph()
        graph_visualization.add_nodes_from(range(self.number_of_nodes))
        if self.number_of_colors < 5:
            color_map = [bright_palette[self.color_list[j]] for j in range(self.number_of_nodes)]
        else:
            color_map = self.color_list
        graph_visualization.add_edges_from(self.edge_list)
        graph_visualization = graph_visualization.to_undirected()
        position_mapping = nx.circular_layout(graph_visualization)

        plt.figure(figsize=(10,5))
        graph_axes = plt.gca()
        title = f'Colored Graph With {number_of_nodes} Nodes and {number_of_colors} Colors'
        graph_axes.set_title(f'{title}')
        nx.draw(graph_visualization, pos=position_mapping, node_color=color_map, with_labels=True, **options)

        plt.show()

if __name__ == '__main__':
    number_of_nodes = 4
    edge_list = [(0,1), (0, 2), (0,3), (1,2), (1, 3), (2,3)]
    number_of_colors = 3
    color_determination = ColoringNodes(number_of_nodes, edge_list=edge_list,number_of_colors=number_of_colors)
    color_assignments = color_determination.determineColors()
    assert color_assignments == None
    number_of_nodes = 4
    edge_list = [(0,1), (0, 2), (0,3), (1,2), (1, 3), (2,3)]
    number_of_colors = 4
    color_determination = ColoringNodes(number_of_nodes, edge_list=edge_list,number_of_colors=number_of_colors)
    color_assignments = color_determination.determineColors()
    assert color_assignments != None
    print(f'Color assignment: {color_assignments}')
    verifyColorAssignments(number_of_nodes, edge_list, number_of_colors, color_assignments)
    color_determination.visualizNodeColorations()
    number_of_nodes = 4
    number_of_colors = 3
    edge_list = [(0,1), (0, 2), (0,3), (1, 3), (2,3)]
    color_determination = ColoringNodes(number_of_nodes, edge_list=edge_list,number_of_colors=number_of_colors)
    color_assignments = color_determination.determineColors()
    assert color_assignments != None
    print(f'Color assignment: {color_assignments}')
    verifyColorAssignments(number_of_nodes, edge_list, number_of_colors, color_assignments)
    color_determination.visualizNodeColorations()
    number_of_nodes = 10
    number_of_colors = 3
    edge_list = [(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(1,6),(6,3),(2,4),(2,5),(7,8),(8,9),(9,7)]
    color_determination = ColoringNodes(number_of_nodes, edge_list=edge_list,number_of_colors=number_of_colors)
    color_assignments = color_determination.determineColors()
    assert color_assignments != None
    print(f'Color assignment: {color_assignments}')
    verifyColorAssignments(number_of_nodes, edge_list, number_of_colors, color_assignments)
    color_determination.visualizNodeColorations()
    number_of_nodes = 10
    number_of_colors = 4
    edge_list = [(0,1),(1,2),(2,3),(3,4),(4,5),(5,6),(1,6),(6,3),(2,4),(2,5),(7,8),(8,9),(9,7)]
    color_determination = ColoringNodes(number_of_nodes, edge_list=edge_list,number_of_colors=number_of_colors)
    color_assignments = color_determination.determineColors()
    assert color_assignments != None
    print(f'Color assignment: {color_assignments}')
    verifyColorAssignments(number_of_nodes, edge_list, number_of_colors, color_assignments)
    color_determination.visualizNodeColorations()