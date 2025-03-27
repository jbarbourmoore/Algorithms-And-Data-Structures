import pulp as lp
import seaborn as sns
import networkx as nx
from matplotlib import pyplot as plt
import pandas as pd

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
            print("Optimal Solution To Minimize Distance Found")
            self.optimal_quantities_moved = [[transport_quantity[i][j].varValue for j in range(0,self.number_of_destinations)] for i in range(0,self.number_of_sources)]
            self.minimal_distance_moved = lpModel.objective.value()
        elif lpModel.status == lp.constants.LpStatusUnbounded:
            print("Unbounded Solution")
        elif lpModel.status == lp.constants.LpStatusInfeasible:
            print("Infeasible Solution")
        else: 
            print("Undefined Status")

    def calculateOptimalTransport_MaximizedPrices(self):
        '''
        This method calculates the source and destination prices in order to maximize profits, within specific criteria
        '''
        
        lpModel = lp.LpProblem('TransportationPricing', lp.LpMaximize)
        source_prices = [lp.LpVariable(f's{i}', 0, None)for i in range(0,self.number_of_sources) ] 
        destination_prices = [lp.LpVariable(f'd{j}', 0, None)for j in range(0,self.number_of_destinations) ] 

        lpModel += lp.lpSum([destination_prices[j] * self.destination_weights[j] for j in range(0,self.number_of_destinations)]) - lp.lpSum([source_prices[i] * self.source_weights[i] for i in range(0,self.number_of_sources)])    
        for i in range(0,self.number_of_sources):
            for j in range(0,self.number_of_destinations):
                lpModel += destination_prices[j] - source_prices[i] <= calculateDistance(self.source_coordinates[i],self.destination_coordinates[j])
            
        lpModel.solve(lp.PULP_CBC_CMD(msg=False))
        if lpModel.status == lp.constants.LpStatusOptimal:
            print("Optimal Solution To Maximize Profits Found")
            self.source_prices = [v.varValue for v in source_prices]
            self.destination_prices = [v.varValue for v in destination_prices]
            self.maximized_profit = lpModel.objective.value()
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

    def outputResults(self):
        '''
        This function outputs the calculated data to the console
        '''

        optomized_transport_source = []
        optomized_transport_destination = []
        for i in range(0,self.number_of_sources):
            optomized_transport_source.append([f"{self.destination_coordinates[j]}: {self.destination_weights[j]:.2f}" for j in range(0,self.number_of_destinations) if self.optimal_quantities_moved[i][j]>0])
        for j in range(0,self.number_of_destinations):
            optomized_transport_destination.append([f"{self.source_coordinates[i]}: {self.optimal_quantities_moved[i][j]:.2f}" for i in range(0,self.number_of_sources) if self.optimal_quantities_moved[i][j]>0 ])

        source_dictionary = {
            "Coordinates" : self.source_coordinates,
            "Weights" : self.source_weights,
            "Prices" : self.source_prices,
            "Optomized Transport" : optomized_transport_source
        }
        destination_dictionary = {
            "Coordinates" : self.destination_coordinates,
            "Weights" : self.destination_weights,
            "Prices" : self.destination_prices,
            "Optomized Transport" : optomized_transport_destination
        }

        pd.options.display.float_format = '{:,.2f}'.format
        source_dataframe = pd.DataFrame.from_dict(source_dictionary)
        destination_dataframe = pd.DataFrame.from_dict(destination_dictionary)

        print(" - - - - - - - - - - - - - - - ")
        print("The final results for the transportaion optomization:")
        print(f"The minimal distance was {self.minimal_distance_moved} and the maximum profit was {self.maximized_profit}")
        print(" - - - - - - - - - - - - - - - ")
        print("The Source Locations")
        print(source_dataframe)
        print(" - - - - - - - - - - - - - - - ")
        print("The Destination Locations")
        print(destination_dataframe)
        print(" - - - - - - - - - - - - - - - ")

if __name__ == '__main__':
    source_coordinates = [ (1,1), (2,2), (3,3), (4, 4), (5,5), (6,6) ]
    source_weights = [10, 10, 10, 10, 10, 10]
    destination_coordinates = [ (6,1), (5, 2), (4,3), (3,2), (2,1) ]
    destination_weights = [12, 12, 12, 12, 12]

    plan = TransportationRequirements(source_coordinates, source_weights, destination_coordinates, destination_weights)
    plan.calculateOptimalTransport_MinimalDistance()
    plan.visualizeOptomizedTransport_MinimimizedDistance()
    plan.calculateOptimalTransport_MaximizedPrices()
    plan.outputResults()