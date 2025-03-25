class GreedyMakespan():
    '''
    This class utilizes a greedy algorithm to control assigning tasks to processors and reducing the makespan
    '''

    def __init__(self, number_of_processors, existing_tasks = None):
        '''
        This method initializes the greedy makespan object

        Parameters :
            number_of_processors : int
                The number of processors that can handle the tasks
            existing_tasks : [int], optional
                The list of the task lengths to be assigned to the processors (default is an empty list)
        '''

        self.number_of_processors = number_of_processors
        if existing_tasks == None:
            self.tasks = []
            self.assignments = []
        else:
            self.tasks = existing_tasks
            self.calculateAssignments_Greedy()

    def calculateMakespan(self):
        '''
        This method calculates the current makespan, or the amount of time it will take the processors to finish their assigned tasks

        Returns :
            maximum_duration : int
                The maximum duration for any of the processors to complete thei currently assigned tasks
        '''

        number_of_jobs = len(self.tasks)
        duration_per_processor = [0]*self.number_of_processors
        for i in range(0,number_of_jobs):
            duration_per_processor[self.assignments[i]] += self.tasks[i]
            
        return max(duration_per_processor)
    
    def calculateAssignments_Greedy(self):
        '''
        This method uses a greedy algorithm to assign the tasks to the cpus
        '''

        number_of_times = len(self.tasks)
        assignments = [None]*number_of_times
        machine_loads = [0]*self.number_of_processors
        for i in range(0,number_of_times):
            min_assigned_machine = machine_loads.index(min(machine_loads))
            assignments[i] = min_assigned_machine
            machine_loads[min_assigned_machine] += self.tasks[i]
            
        self.assignments = assignments

    def addTasks(self, tasks):
        '''
        This method adds tasks to the computer and redistributes the tasks to the processors

        Parameters :
            tasks : [int]
                The list of the task lengths to be assigned to the processors
        '''

        self.tasks += tasks
        self.calculateAssignments_Greedy()

    def printComputerDetails(self):
        '''
        This method outputs the details of the current tasking to the command line
        '''

        print(f"This computer has {self.number_of_processors} cpus and {len(self.tasks)} jobs with a makespan of {self.calculateMakespan()}")
        machine_tasks = [0]*self.number_of_processors
        machine_durations = [0]*self.number_of_processors
        machine_task_list = []
        for i in range(0,self.number_of_processors):
            machine_task_list.append([])
        for i in range(0,len(self.tasks)):
            assigned_machine = self.assignments[i]
            machine_tasks[assigned_machine] += 1
            machine_durations[assigned_machine] += self.tasks[i]
            machine_task_list[assigned_machine].append(self.tasks[i])
        for i in range(0,self.number_of_processors):
            print(f"Processor {i} has been assigned {machine_tasks[i]} tasks with a total duration {machine_durations[i]}")
            print(f"The individual task durations are {machine_task_list[i]}")

if __name__ == '__main__':
    computer = GreedyMakespan(3, [2,2,5,3,1,4,2,1,1,2,3,2])
    computer.printComputerDetails()
    print("****")
    computer.addTasks([4,7,2])
    computer.printComputerDetails()
    print("****")
    computer.addTasks([12,2,2,2,2,2,2,2,2])
    computer.printComputerDetails()
    print("****")
    print("Computer with 4 cpus")
    print("****")
    computer = GreedyMakespan(4, [2,2,5,3,1,4,2,1,1,2,3,2])
    computer.printComputerDetails()
    print("****")
    computer.addTasks([4,7,2])
    computer.printComputerDetails()
    print("****")
    computer.addTasks([12,2,2,2,2,2,2,2,2])
    computer.printComputerDetails()