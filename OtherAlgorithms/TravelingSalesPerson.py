from pulp import *

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
                time_i = time_stamps[i-1]
                time_j = time_stamps[j -1]
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

        return tours,tour_cost

if __name__ == '__main__':
    cost_matrix=[ [None,3,4,3,5],
                [1, None, 2,4, 1],
                [2, 1, None, 5, 4],
                [1, 1, 5, None, 4],
                [2, 1, 3, 5, None] ]

    nodes=5
    salespeople=2
    two_traveling_salespeople = TravelingSalesPerson(nodes, cost_matrix)
    two_tours, tour_cost = two_traveling_salespeople.calculateTSP_DefiniteNumberOfSalespeople(salespeople)

    assert len(two_tours) == salespeople
    assert abs(tour_cost - 12) <= 0.001
    for i in range(1, nodes):
        sum([ 1 if i in tour else 0 for _,tour in two_tours.items()]) == 1