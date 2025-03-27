import pulp as lp
import seaborn as sns
import networkx as nx
from matplotlib import pyplot as plt

def calculateDistance(source_coordinate, destination_coordinate):
    '''
    This function calculates the distance between two locations

    Parameters :
        source_coordinate : (int, int)
            The x,y coordinate of the source location
        destination_coordinate : (int, int)
            The x,y coordinate of the destination location

    Returns : 
        distance : number
            The distance between the source and the destination
    '''

    (x_source, y_source) = source_coordinate
    (x_destination, y_destination) = destination_coordinate
    distance =  ( (x_source- x_destination)**2 + (y_source - y_destination)**2) ** .5
    return distance

class TransportationRequirements():

    def __init__(self,source_coordinates, source_weights, destination_coordinates, destination_weights):
        '''
        This method initializes the Transportation Requirements object

        Parameters :
            source_coordinates : [(int,int)]
                The list of source coordinates
            source_weights : [int]
                The list of source weights
            destination_coordinates : [(int,int)]
                The list of destination coordinates
            destination_weights : [int]
                The list of destination weights
        '''

        self.source_coordinates = source_coordinates
        self.source_weights = source_weights
        self.destination_coordinates = destination_coordinates
        self.destination_weights = destination_weights

        self.number_of_sources = len(self.source_coordinates)
        self.number_of_destinations = len(self.destination_coordinates)

        self.optimal_quantities_moved = None
        self.minimal_distance_moved = None

    def calculateOptimalTransport_MinimalDistance(self):
        '''
        This method calculates the optimal transport arrangement that minimizes the distance traveled
        '''

        lpModel = lp.LpProblem('OptimizedTransportPlan', lp.LpMinimize)
        transport_quantity = [ [lp.LpVariable(f'x{i}{j}', 0, None) for j in range(0, self.number_of_destinations)] for i in range(0,self.number_of_sources) ] 

        lpModel += lp.lpSum([[calculateDistance(self.source_coordinates[i],self.destination_coordinates[j])*transport_quantity[i][j] for j in range(0,self.number_of_destinations)] for i in range(0,self.number_of_sources) ])
        for i in range(0,self.number_of_sources):
            lpModel += lp.lpSum([transport_quantity[i][j]  for j in range(0,self.number_of_destinations)]) == self.source_weights[i]
        for j in range(0,self.number_of_destinations):
            lpModel += lp.lpSum([transport_quantity[i][j]  for i in range(0,self.number_of_sources)]) == self.destination_weights[j]
            
        lpModel.solve(lp.PULP_CBC_CMD(msg=False))
        
        if lpModel.status == lp.constants.LpStatusOptimal:
            print("Optimal Solution Found")
            self.optimal_quantities_moved = [[transport_quantity[i][j].varValue for j in range(0,self.number_of_destinations)] for i in range(0,self.number_of_sources)]
            self.minimal_distance_moved = lpModel.objective.value()
        elif lpModel.status == lp.constants.LpStatusUnbounded:
            print("Unbounded Solution")
        elif lpModel.status == lp.constants.LpStatusInfeasible:
            print("Infeasible Solution")
        else: 
            print("Undefined Status")
    
    def calculateWeightedDirectedEdges_MinimizedDistance(self):
        '''
        This method created a list of directed edges, where each weight is the amount transported in the optimal model
        
        Returns :
            edge_list = [(int,int,number)]
                The list of weighted directed edges
        '''
        edge_list = []
        for i in range(0,self.number_of_sources):
            for j in range(0,self.number_of_destinations):
                if self.optimal_quantities_moved[i][j]>0:
                    edge_list.append((i,self.number_of_sources+j,self.optimal_quantities_moved[i][j]))
        return edge_list

    def visualizeOptomizedTransport_MinimimizedDistance(self):
        '''
        This method creates a graphical visualization of the weights moved between locations using matplotlib and networkx
        '''

        options = {"edgecolors": "tab:gray", "node_size": 800, "alpha": 1, "font_color":"whitesmoke", "font_size":16}
        bright_palette = sns.hls_palette(h=.5)
        graph_visualization = nx.DiGraph()
        graph_visualization.add_nodes_from(range(self.number_of_sources+self.number_of_destinations))
        color_map = [bright_palette[0] if j < self.number_of_sources else bright_palette[1] for j in range(self.number_of_sources+self.number_of_destinations)]
        graph_visualization.add_weighted_edges_from(self.calculateWeightedDirectedEdges_MinimizedDistance())
        position_mapping = nx.circular_layout(graph_visualization)
        plt.figure(figsize=(10,5))
        graph_axes = plt.gca()
        title = f'Visualized Transport With A Distance of {self.minimal_distance_moved:.2f}'
        graph_axes.set_title(f'{title}')
        
        nx.draw(graph_visualization, pos=position_mapping, node_color=color_map, with_labels=True, **options)
        weight_labels = nx.get_edge_attributes(graph_visualization, 'weight')
        nx.draw_networkx_edge_labels(graph_visualization, position_mapping, edge_labels=weight_labels, font_color=bright_palette[1])
        plt.show()

source_coordinates = [ (1,1), (2,2), (3,3), (4, 4), (5,5), (6,6) ]
source_weights = [10, 10, 10, 10, 10, 10]
destination_coordinates = [ (6,1), (5, 2), (4,3), (3,2), (2,1) ]
destination_weights = [12, 12, 12, 12, 12]

plan = TransportationRequirements(source_coordinates, source_weights, destination_coordinates, destination_weights)
plan.calculateOptimalTransport_MinimalDistance()
plan.visualizeOptomizedTransport_MinimimizedDistance()