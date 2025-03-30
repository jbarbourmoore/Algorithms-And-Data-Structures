import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
from matplotlib import pyplot as plt

def applyReflectionAboutUniformState(quantum_circuit, inputs): 
    '''
    This function applies reflection about the uniform state

    Parameters :
        quantum_circuit : QuantumCircuit
            The quantum circuit
        inputs : QuantumRegister
            The quantum register with 3 qubits to be used as the input for this function
    '''
    # apply Hadamard and invert the qubits
    for i in inputs:
        quantum_circuit.h(i)
        quantum_circuit.x(i)
    number_of_registers = len(inputs)

    # apply a multi controlled Z gate 
    quantum_circuit.mcp(np.pi, inputs[0:number_of_registers-1], inputs[number_of_registers-1])
    
    # restore the qubits
    for i in inputs:
        quantum_circuit.x(i)
        quantum_circuit.h(i)

def searchFor3BitNumber(quantum_circuit, inputs, output, number_to_search):
    '''
    This function generates the simple circuit for f(b_0, b_1, b_2) = 3 bit number in binary

    Parameters :
        quantum_circuit : QuantumCircuit
            The quantum circuit
        inputs : QuantumRegister
            The quantum register with 3 qubits to be used as the input for this function
        outputs : QuantumRegister
            The quantum register with 1 qubit to hold the result of this circuit
        number_to_search: int
            A number with three bits (0-7)
    '''

    # creates the binary value for the number
    if number_to_search in [0, 2, 4, 6]:
        quantum_circuit.x(inputs[0])
    if number_to_search in [0, 1, 4, 5]:
        quantum_circuit.x(inputs[1])
    if number_to_search in [0, 1, 2, 3]:
        quantum_circuit.x(inputs[2])

    # define ciruit inputs and result
    quantum_circuit.mcx([inputs[0], inputs[1], inputs[2]], output[0])

    # restores the bits that were flipped
    if number_to_search in [0, 2, 4, 6]:
        quantum_circuit.x(inputs[0])
    if number_to_search in [0, 1, 4, 5]:
        quantum_circuit.x(inputs[1])
    if number_to_search in [0, 1, 2, 3]:
        quantum_circuit.x(inputs[2])    

def createGroverSearchFor3BitNumber(quantum_circuit, inputs, result, classical_bits, number_to_search = 0, number_of_iterations = 1):
    '''
    This function performs a grover's search for a 3 bit number over a certain number of iterations

    Parameters :
        quantum_circuit : QuantumCircuit
            The quantum circuit
        inputs : QuantumRegister
            The quantum register with 3 qubits to be used as the input for this function
        outputs : QuantumRegister
            The quantum register with 1 qubit to hold the result of this circuit
        classical_bits : ClassicalRegister
            The classical register with 3 bits
        number_to_search: int
            A number with three bits (0-7)
        number_of_iterations : int
            The number of iterations to perform the grover search
    '''

    quantum_circuit.h(inputs[0])
    quantum_circuit.h(inputs[1])
    quantum_circuit.h(inputs[2])

    quantum_circuit.x(result[0])
    quantum_circuit.h(result[0])

    for _ in range(number_of_iterations):
        quantum_circuit.barrier()
        searchFor3BitNumber(quantum_circuit, inputs, result, number_to_search)
        applyReflectionAboutUniformState(quantum_circuit, inputs)

    quantum_circuit.measure(inputs, classical_bits)

def outputSearchResultsFor3BitNumber(number_to_search):
    '''
    This function outputs the search results for a 3 bit number as histograms as well as the circuit diagrams
    
    Parameters :
        number_to_search: int
            A number with three bits (0-7)
    '''

    inputs = QuantumRegister(3, 'b')
    output = QuantumRegister(1, 'r')
    classical_bits = ClassicalRegister(3, 'z')
    quantum_circuit = QuantumCircuit(inputs, output, classical_bits)

    fig, axes = plt.subplots(2, 2, layout='constrained')
    fig.set_figwidth(10)
    fig.set_figheight(8)

    fig_circuits, axes_circuits = plt.subplots(1, 4, layout='constrained')
    fig_circuits.set_figwidth(14)

    title = f"Result Frequency For Grover Search Algorithm for f(b_0, b_1, b_2) = {number_to_search}"
    axes[0,0].set_title('1 Iteration Of Grovers Algorithm')
    axes[0,1].set_title('2 Iterations Of Grovers Algorithm')
    axes[1,0].set_title('6 Iterations Of Grovers Algorithm')
    axes[1,1].set_title('13 Iterations Of Grovers Algorithm')
    fig.suptitle(title, fontsize=16) 
    fig.canvas.manager.set_window_title(f'GroverSearchAlgorithms_SearchFor{number_to_search}_Histograms') 

    title_circuits = f"Circuit Diagrams For Grover Search Algorithm for f(b_0, b_1, b_2) = {number_to_search}"
    axes_circuits[0].set_title('1 Iteration Of Grovers Algorithm',x=0.5, y=2.1)
    axes_circuits[1].set_title('2 Iterations Of Grovers Algorithm',x=0.5, y=3)
    axes_circuits[2].set_title('6 Iterations Of Grovers Algorithm',x=0.5, y=1.35)
    axes_circuits[3].set_title('13 Iterations Of Grovers Algorithm',x=0.5, y=1)
    fig_circuits.suptitle(title_circuits, fontsize=16) 
    fig_circuits.canvas.manager.set_window_title(f'GroverSearchAlgorithms_SearchFor{number_to_search}_CircuitDiagrams') 


    createGroverSearchFor3BitNumber(quantum_circuit, inputs, output, classical_bits, number_to_search, 1)
    simulator = Aer.get_backend('aer_simulator')
    circ = transpile(quantum_circuit, simulator)
    result = simulator.run(quantum_circuit).result()
    counts = result.get_counts(circ)

    plot_histogram(counts, ax=axes[0,0], color=["skyblue"])
    quantum_circuit.draw('mpl', style="clifford", scale=.5,ax=axes_circuits[0])

    inputs = QuantumRegister(3, 'b')
    output = QuantumRegister(1, 'r')
    classical_bits = ClassicalRegister(3, 'z')
    quantum_circuit = QuantumCircuit(inputs, output, classical_bits)

    createGroverSearchFor3BitNumber(quantum_circuit, inputs, output, classical_bits, number_to_search, 2)
    simulator = Aer.get_backend('aer_simulator')
    circ = transpile(quantum_circuit, simulator)
    result = simulator.run(quantum_circuit).result()
    counts = result.get_counts(circ)
    plot_histogram(counts, ax=axes[0,1], color=["skyblue"])
    quantum_circuit.draw('mpl', style="clifford", scale=.5,ax=axes_circuits[1])

    inputs = QuantumRegister(3, 'b')
    output = QuantumRegister(1, 'r')
    classical_bits = ClassicalRegister(3, 'z')
    quantum_circuit = QuantumCircuit(inputs, output, classical_bits)

    createGroverSearchFor3BitNumber(quantum_circuit, inputs, output, classical_bits, number_to_search, 6)
    simulator = Aer.get_backend('aer_simulator')
    circ = transpile(quantum_circuit, simulator)
    result = simulator.run(quantum_circuit).result()
    counts = result.get_counts(circ)
    plot_histogram(counts, ax=axes[1,0], color=["skyblue"])
    quantum_circuit.draw('mpl', style="clifford", scale=.5,ax=axes_circuits[2])

    inputs = QuantumRegister(3, 'b')
    output = QuantumRegister(1, 'r')
    classical_bits = ClassicalRegister(3, 'z')
    quantum_circuit = QuantumCircuit(inputs, output, classical_bits)

    createGroverSearchFor3BitNumber(quantum_circuit, inputs, output, classical_bits, number_to_search,13)
    simulator = Aer.get_backend('aer_simulator')
    circ = transpile(quantum_circuit, simulator)
    result = simulator.run(quantum_circuit).result()
    counts = result.get_counts(circ)
    plot_histogram(counts, ax=axes[1,1], color=["skyblue"])
    quantum_circuit.draw('mpl', style="clifford", scale=.5,ax=axes_circuits[3])
    plt.show()


number_to_search = 3
outputSearchResultsFor3BitNumber(number_to_search)