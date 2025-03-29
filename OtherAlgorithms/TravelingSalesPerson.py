from pulp import *
import seaborn as sns
import networkx as nx
from matplotlib import pyplot as plt

class TravelingSalesPerson():
    '''
    This class solves variations on the Traveling Sales Person problem
    '''

    def __init__(self, number_of_nodes, cost_matrix):
        '''
        This method initializes the traveling sales person problem

        Parameters : 
            number_of_nodes : int
                The number of nodes in the TSP
            cost_matrix : int
                The cost matrix for all routes in the TSP
        '''

        self.number_of_nodes = number_of_nodes
        self.cost_matrix = cost_matrix
        self.all_unweighted_undirected_edges = []
        for i in range(0, self.number_of_nodes):
            for j in range(i+1,self.number_of_nodes):
                if i != j and self.cost_matrix[i][j] != None:
                    self.all_unweighted_undirected_edges.append((i, j))
        print(self.all_unweighted_undirected_edges)

    def calculateTSP_DefiniteNumberOfSalespeople(self, number_of_salespeople):
        '''
        This method uses linear programming with binary variables to solve traveling sales person with exactly the specified number of sales people

        Parameters :
            number_of_salespeople : int
                The number of salespeople who are taking on routes in the TSP
        '''
        
        lp_problem = LpProblem('TSP_DefiniteNumberOfSalespeople', LpMinimize)
        
        binary_variables = [[ LpVariable(f'binary_{i}_{j}', cat='Binary') if i != j else None for j in range(0, self.number_of_nodes)] for i in range(0,self.number_of_nodes) ]
        time_stamps = [LpVariable(f'time_{j}', lowBound=0, upBound=self.number_of_nodes, cat='Continuous') for j in range(1, self.number_of_nodes)]

        objective = lpSum( [ lpSum([binary_i_j*cost_j if binary_i_j != None else 0 for (binary_i_j, cost_j) in zip(binary_row, cost_row) ])
                            for (binary_row, cost_row) in zip(binary_variables, cost_matrix)] )
        
        lp_problem += objective 

        # The first node has all the salespeople coming and going, while the others are visited by exactly one sales person
        lp_problem += lpSum([binary_j for binary_j in binary_variables[0] if binary_j != None]) == number_of_salespeople
        lp_problem += lpSum([binary_variables[j][0] for j in range(0,self.number_of_nodes) if j != 0]) == number_of_salespeople
        for i in range(1,self.number_of_nodes):
            lp_problem += lpSum([binary_j for binary_j in binary_variables[i] if binary_j != None]) == 1
            lp_problem += lpSum([binary_variables[j][i] for j in range(nodes) if j != i]) == 1
        
        # time based constraints (array starts at node 1 not 0, still indexed at 0)
        for i in range(1,self.number_of_nodes):
            for j in range(1, self.number_of_nodes):
                if i == j: 
                    continue
                binary_i_j = binary_variables[i][j]
                time_i = time_stamps[i - 1]
                time_j = time_stamps[j - 1]
                lp_problem += time_j >= time_i + binary_i_j - (1-binary_i_j)*(self.number_of_nodes+1) # add the constraint

        lp_problem.solve(PULP_CBC_CMD(msg=False))

        # Begin a dictionary of each salesperson's tour and their first stop after 0
        tours={}
        solutions = [j for (j, xij) in enumerate(binary_variables[0]) if xij != None and xij.varValue >= 0.999]
        for salesperson_tour in range(0, number_of_salespeople):
            tours[salesperson_tour] = [0, solutions[salesperson_tour]]

        # trace each salesperson's route back to 0
        for salesperson_tour in range(0,number_of_salespeople):
            latest_stop = tours[salesperson_tour][-1]
            while latest_stop != 0:
                solutions = [j for (j, xij) in enumerate(binary_variables[latest_stop]) if xij != None and xij.varValue >= 0.999]
                tours[salesperson_tour].append(solutions[0])
                latest_stop = solutions[0]
    
        # calculate the total cost for all salespeople's tours
        tour_cost = 0
        for index,tour in tours.items():
            print(f"Salesperson {index+1}: {tour}")
            i=0
            for j in tour[1:]:
                tour_cost += cost_matrix[i][j]
                i = j
        print(f"Total Cost: {tour_cost}")

        return tours, tour_cost
    
    def calculateTSP_MaximumNumberOfSalespeople(self, number_of_salespeople):
        '''
        This method uses linear programming with binary variables to solve traveling sales person with between one and the specified number of salespeople

        Parameters :
            number_of_salespeople : int
                The number of salespeople who are taking on routes in the TSP
        '''
        
        lp_problem = LpProblem('TSP_DefiniteNumberOfSalespeople', LpMinimize)
        
        binary_variables = [[ LpVariable(f'binary_{i}_{j}', cat='Binary') if i != j else None for j in range(0, self.number_of_nodes)] for i in range(0,self.number_of_nodes) ]
        time_stamps = [LpVariable(f'time_{j}', lowBound=0, upBound=self.number_of_nodes, cat='Continuous') for j in range(1, self.number_of_nodes)]

        objective = lpSum( [ lpSum([binary_i_j*cost_j if binary_i_j != None else 0 for (binary_i_j, cost_j) in zip(binary_row, cost_row) ])
                            for (binary_row, cost_row) in zip(binary_variables, cost_matrix)] )
        
        lp_problem += objective 

        # The first node has between one and the maximum number of salespeople coming and going, while the others are visited by exactly one sales person
        lp_problem += lpSum([binary_j for binary_j in binary_variables[0] if binary_j != None]) <= number_of_salespeople
        lp_problem += lpSum([binary_variables[j][0] for j in range(0,self.number_of_nodes) if j != 0]) <= number_of_salespeople
        lp_problem += lpSum([binary_j for binary_j in binary_variables[0] if binary_j != None]) >= 1
        lp_problem += lpSum([binary_variables[j][0] for j in range(0,self.number_of_nodes) if j != 0]) >= 1
        for i in range(1,self.number_of_nodes):
            lp_problem += lpSum([binary_j for binary_j in binary_variables[i] if binary_j != None]) == 1
            lp_problem += lpSum([binary_variables[j][i] for j in range(nodes) if j != i]) == 1
        
        # time based constraints (array starts at node 1 not 0, still indexed at 0)
        for i in range(1,self.number_of_nodes):
            for j in range(1, self.number_of_nodes):
                if i == j: 
                    continue
                binary_i_j = binary_variables[i][j]
                time_i = time_stamps[i - 1]
                time_j = time_stamps[j - 1]
                lp_problem += time_j >= time_i + binary_i_j - (1-binary_i_j)*(self.number_of_nodes+1) # add the constraint

        lp_problem.solve(PULP_CBC_CMD(msg=False))

        # Begin a dictionary of each salesperson's tour and their first stop after 0
        tours={}
        solutions = [j for (j, xij) in enumerate(binary_variables[0]) if xij != None and xij.varValue >= 0.999]
        calculated_number_salespeople = len(solutions)
        for salesperson_tour in range(0, calculated_number_salespeople):
            tours[salesperson_tour] = [0, solutions[salesperson_tour]]

        # trace each salesperson's route back to 0
        for salesperson_tour in range(0,calculated_number_salespeople):
            latest_stop = tours[salesperson_tour][-1]
            while latest_stop != 0:
                solutions = [j for (j, xij) in enumerate(binary_variables[latest_stop]) if xij != None and xij.varValue >= 0.999]
                tours[salesperson_tour].append(solutions[0])
                latest_stop = solutions[0]
    
        # calculate the total cost for all salespeople's tours
        tour_cost = 0
        for index,tour in tours.items():
            print(f"Salesperson {index+1}: {tour}")
            i=0
            for j in tour[1:]:
                tour_cost += cost_matrix[i][j]
                i = j
        print(f"Total Cost: {tour_cost}")

        return tours, tour_cost
    
    def visualize_MaxAndExactNumberSalespeople(self, number_of_salespeople):
        '''
        This method creates a graphical visualization of the TSP with varying number of salespeople constraints
        '''

        options = {"edgecolors": "tab:gray", "node_size": 800, "alpha": 1, "font_color":"whitesmoke", "font_size":16}
        bright_palette = sns.hls_palette(h=.5)
        graph_visualization = nx.Graph()
        graph_visualization.add_nodes_from(range(self.number_of_nodes))
        graph_visualization.add_edges_from(self.all_unweighted_undirected_edges)
        position_mapping = nx.spring_layout(graph_visualization)
        title = f'Visualized {number_of_salespeople} Salespeople With {self.number_of_nodes} Nodes'
        # rendering

        fig, axes = plt.subplots(2, 2, layout='constrained')

        fig.suptitle(title, fontsize=16)        
        plt.subplot(221)
        plt.axis('off')
        axes[0,0].set_title('Graph Layout')

        color_map = [bright_palette[0] for _ in range(self.number_of_nodes)]
        nx.draw(graph_visualization, pos=position_mapping, node_color=color_map, with_labels=True, **options)

        plt.subplot(222)
        plt.axis('off')
        graph_visualization.remove_edges_from(self.all_unweighted_undirected_edges)

        graph_visualization = graph_visualization.to_directed()
        color_map = [bright_palette[0] for _ in range(self.number_of_nodes)]
        exact_routes, prices = self.calculateTSP_DefiniteNumberOfSalespeople(1)
        directed_weighted_edges = []
        for index,route in exact_routes.items():
            previous_stop = 0
            if index < 5:
                color = bright_palette[index+1]
            else:
                color = index
            for stop in route:
                if stop != previous_stop:
                    directed_weighted_edges.append((previous_stop,stop,self.cost_matrix[previous_stop][stop]))
                if stop != 0:
                    color_map[stop] = color
                previous_stop = stop
        graph_visualization.add_weighted_edges_from(directed_weighted_edges)
        nx.draw(graph_visualization, pos=position_mapping, node_color=color_map, with_labels=True, **options)
        weight_labels = nx.get_edge_attributes(graph_visualization, 'weight')
        nx.draw_networkx_edge_labels(graph_visualization, position_mapping, edge_labels=weight_labels, font_color=bright_palette[1])
        axes[0,1].set_title(f'Exactly 1 Salesperson With Cost {prices}')

        plt.subplot(223)
        plt.axis('off')
        graph_visualization.remove_edges_from(directed_weighted_edges)

        color_map = [bright_palette[0] for _ in range(self.number_of_nodes)]
        exact_routes, prices = self.calculateTSP_DefiniteNumberOfSalespeople(number_of_salespeople)
        directed_weighted_edges = []
        for index,route in exact_routes.items():
            previous_stop = 0
            if index < 5:
                color = bright_palette[index+1]
            else:
                color = index
            for stop in route:
                if stop != previous_stop:
                    directed_weighted_edges.append((previous_stop,stop,self.cost_matrix[previous_stop][stop]))
                if stop != 0:
                    color_map[stop] = color
                previous_stop = stop
        graph_visualization.add_weighted_edges_from(directed_weighted_edges)
        nx.draw(graph_visualization, pos=position_mapping, node_color=color_map, with_labels=True, **options)
        weight_labels = nx.get_edge_attributes(graph_visualization, 'weight')
        nx.draw_networkx_edge_labels(graph_visualization, position_mapping, edge_labels=weight_labels, font_color=bright_palette[1])
        axes[1,0].set_title(f'Exactly {number_of_salespeople} Salespeople With Cost {prices}')

        plt.subplot(224); plt.axis('off')
        color_map = [bright_palette[0] for _ in range(self.number_of_nodes)]
        max_routes, prices = self.calculateTSP_MaximumNumberOfSalespeople(number_of_salespeople)
        graph_visualization.remove_edges_from(directed_weighted_edges)
        directed_weighted_edges = []
        for index,route in max_routes.items():
            previous_stop = 0
            if index < 5:
                color = bright_palette[index+1]
            else:
                color = index
            for stop in route:
                if stop != previous_stop:
                    directed_weighted_edges.append((previous_stop,stop,self.cost_matrix[previous_stop][stop]))
                if stop != 0:
                    color_map[stop] = color
                previous_stop = stop

        graph_visualization.add_weighted_edges_from(directed_weighted_edges)
        nx.draw(graph_visualization, pos=position_mapping, node_color=color_map, with_labels=True, **options)
        weight_labels = nx.get_edge_attributes(graph_visualization, 'weight')
        nx.draw_networkx_edge_labels(graph_visualization, position_mapping, edge_labels=weight_labels, font_color=bright_palette[1])
        axes[1,1].set_title(f'Maximum Of {number_of_salespeople} Salespeople With Cost {prices}')

        fig.tight_layout()
        plt.show()

if __name__ == '__main__':
    cost_matrix=[[None, 3, 4, 3, 5],
                 [1, None, 2, 4, 1],
                 [2, 1, None, 5, 4],
                 [1, 1, 5, None, 4],
                 [2, 1, 3, 5, None] ]

    nodes = 5
    salespeople = 2
    two_traveling_salespeople = TravelingSalesPerson(nodes, cost_matrix)
    two_tours, tour_cost = two_traveling_salespeople.calculateTSP_DefiniteNumberOfSalespeople(salespeople)

    assert len(two_tours) == salespeople
    assert abs(tour_cost - 12) <= 0.001
    for i in range(1, nodes):
        sum([ 1 if i in tour else 0 for _,tour in two_tours.items()]) == 1

    max_two_tours, max_two_tour_cost = two_traveling_salespeople.calculateTSP_MaximumNumberOfSalespeople(salespeople)
    assert len(max_two_tours) <= salespeople
    assert len(max_two_tours) >= 1
    assert abs(max_two_tour_cost - 10) <= 0.001
    for i in range(1, nodes):
        sum([ 1 if i in tour else 0 for _,tour in max_two_tours.items()]) == 1

    two_traveling_salespeople.visualize_MaxAndExactNumberSalespeople(salespeople)