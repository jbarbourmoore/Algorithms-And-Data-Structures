import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from random import randint
import time

def factorialByRecursion(number):
    '''
    This function calculates the factorial of a given number by using recursion

    Parameters :
        number : int 
            The number that the factorial is being calculated for

    Returns : 
        factorial : int 
            The resulting factorial of number
    '''
    
    if number == 0:
        return 1

    return number * factorialByRecursion(number - 1)

def factorialByLoop(number):
    '''
    This function calculates the factorial of a given number by using a loop

    Parameters :
        number : int 
            The number that the factorial is being calculated for

    Returns : 
        factorial : int 
            The resulting factorial of number
    '''

    factorial = 1

    for i in range(2, number + 1):
        factorial = factorial * i

    return factorial

def calculatePrimeFactors(number):
    '''
    This function calculates the prime factors of a given number by using nested loops

    Parameters :
        number : int 
            The number that the prime factors are being calculated for

    Returns : 
        prime_factors : {int:int}
            The resulting prime factors as a dictionary where each prime factor is a key and the value is the count for that factor
    '''
    prime_factors = {}
    potential_factor = 2

    # Calculating prime factors of : 84
    # number:  84 -> 42   factor :2
    # number:  42 -> 21   factor :2
    # number:  21 ->  7   factor :3
    # Prime Factors : {2: 2, 3: 1}
    while potential_factor**2 <= number:
        while number % potential_factor == 0:

            if potential_factor in prime_factors:
                prime_factors[potential_factor] += 1
            else:
                prime_factors[potential_factor] = 1

            number = number // potential_factor

        potential_factor += 1

    # remaining number: 7 leaving us the factor :7
    # Prime Factors : {2: 2, 3: 1, 7: 1}
    if number > 1:
        if potential_factor in prime_factors:
            prime_factors[number] += 1
        else:
            prime_factors[number] = 1

    return prime_factors

def factorialByPrimeFactors(number):
    '''
    This function calculates the factorial of a given number by using it's prime factors.

    It should be the most efficient of the thre factorial algorithms

    Parameters :
        number : int 
            The number that the factorial is being calculated for

    Returns : 
        factorial : int 
            The resulting factorial of number
    '''

    factorial = 1

    # example using 6! which is 720
    # 2 ->   prime factors: {2: 1}          -> 2
    # 3 ->   prime factors: {3: 1}          -> 6
    # 4 ->   prime factors: {2: 2}          -> 12 -> 24
    # 5 ->   prime factors: {5: 1}          -> 120
    # 6 ->   prime factors: {2: 1, 3: 1}    -> 240 -> 720
    for i in range(2, number+1):
        prime_factors = calculatePrimeFactors(i)
        for prime_factor in prime_factors:
            factorial *= prime_factor ** prime_factors[prime_factor]

    return factorial

def compareFactorialDurations():
    

    durations = []
    types = []
    numbers = []
    recursive_durations = []
    recursive_numbers = []
    recursive_method = []

    for number in range(0, 30000,25):

            start_time = time.time()
            try:
                recursive_factorial = factorialByRecursion(number=number)
                duration = time.time() - start_time
                durations.append(duration)
                types.append("Recursive")
                numbers.append(number)
                recursive_durations.append(duration)
                recursive_numbers.append(number)
                recursive_method.append("Recursive")
            except:
                recursive_factorial = None
                

            start_time = time.time()
            loop_factorial = factorialByLoop(number=number)
            duration = time.time() - start_time
            durations.append(duration)
            types.append("Loop")
            numbers.append(number)

            start_time = time.time()
            prime_factors_factorial = factorialByPrimeFactors(number=number)
            duration = time.time() - start_time
            durations.append(duration)
            types.append("Prime Factors")
            numbers.append(number)
            print(number)
            #print(f"{number}! is loop:{loop_factorial}, recursion:{recursive_factorial}, and prime_factors:{prime_factors_factorial} which are hopefully the same")


    dictionary ={
        "Duration": durations,
        "Method": types,
        "Number": numbers
    }
    dataframe = pd.DataFrame.from_dict(dictionary)

    recursive_dictionary = {
        "Duration": recursive_durations,
        "Method": recursive_method,
        "Number": recursive_numbers
    }
    recursive_datafrom = pd.DataFrame.from_dict(recursive_dictionary)

    dataframe.dropna()

    dataframe.to_csv("Factorial_Durations.csv")

    fig, axes = plt.subplots(nrows=1, ncols=2, sharey=False)
    fig.set_figwidth(10)
    fig.set_figheight(6)

    bright_palette = sns.hls_palette(h=.5)

    sns.set_theme(style="whitegrid", palette=bright_palette)
    sns.scatterplot(data=dataframe, x="Number", y="Duration", ax=axes[0], hue="Method", palette=bright_palette[0:3])
    sns.scatterplot(data=recursive_datafrom, x="Number", y="Duration", ax=axes[1], hue="Method", palette=bright_palette[0:1])


    fig.canvas.manager.set_window_title('FFT amd Brute Force Durations By Array Length')

    plt.tight_layout()
    plt.show()

def probabilityOfASingleEvent(successful_outcomes, total_outcomes):
    '''
    This function calculates the probability that a single event occurs given the number of successful outcomes and the total number of outcomes

    Parameters :
        successful_outcomes : int
            The number of successful outcomes
        total_outcomes : int
            The total number of potential outcomes

    Returns :
        probability : float
            The probability that the event occurs (should be between 0 and 1, where 1 is that the event will definitely occuring)
    '''

    return successful_outcomes / total_outcomes

def probabilityTwoIndependantEventsOccur(a_successful_outcomes, b_successful_outcomes, total_outcomes, b_total_outcomes=None):
    '''
    This function calculates the probability of two independent events occuring

    The probability of events a and b is the probability of event a multiplies by the probability of event b

    Parameters :
        a_successful_outcomes : int
            The number of successful outcomes for event a
        b_successful_outcomes : int
            The number of successful outcomes for event b
        total_outcomes : int
            The total number of potential outcomes for event a (or both event a and b)
        b_total_outcomes : int
            The total number of potential outcomes for event b (default is the same as a)

    Returns :
        probability : float
            The probability that the event occurs (should be between 0 and 1, where 1 is that the event will definitely occuring)
    '''

    if b_total_outcomes == None:
        b_total_outcomes = total_outcomes
    
    a_probability = probabilityOfASingleEvent(a_successful_outcomes, total_outcomes)
    b_probability = probabilityOfASingleEvent(b_successful_outcomes, b_total_outcomes)

    return a_probability * b_probability

def permutationsWithRepetition(number_of_options, count_choices_made):
    '''
    This function calculates the number of possibilities for a ordered selection that allows repetition

    total_possibilities = number_of_options ** count_choices_made

    An example would be calculating the total number of possible 4 digit [0-9] pins 

    Parameters :
        number_of_options : int
            The number of options that each selection is choosing between (such as 10 digit options [0-9] for a pin)
        count_choices_made : int 
            The number of times a choice is made (such as selecting 4 digits for a pin)

    Returns : 
        total_possibilities : int
            The total number of possibilities for an ordered selection that allows repetition
    '''

    return number_of_options ** count_choices_made

def permutationWithoutRepetition(number_of_options, count_choices_made):
    '''
    This function calculates the number of possibilities for an ordered selection that does not allow repetition

    total_possibilities = number_of_options! / (number_of_options - count_choices_made)!

    An example would be finding th number of orders 3 out of 16 billiards balls may go into the nets -> 16!/(16-3)! -> 16!/13! -> 3360

    Parameters :
        number_of_options : int
            The number of options that each selection is choosing between (such as 16 billiards balls)
        count_choices_made : int 
            The number of times a choice is made (such as 3 of them going into the net)

    Returns : 
        total_possibilities : int
            The total number of possibilities for an ordered selection that does not allow repetition
    '''

    total_possibilities = factorialByPrimeFactors(number_of_options) / factorialByPrimeFactors(number_of_options - count_choices_made)
    return total_possibilities

def combinationsWithoutRepetition(number_of_options, count_choices_made):
    '''
    This function calculates the number of possibilities for an unordered selection that does not allow repetition

    total_possibilities = number_of_options! / (count_choices_made! * (number_of_options - count_choices_made)!)

    An example would be finding the number of combos that can be made with 3 out of 16 billiards balls-> 16!/(3!(16-3)!) -> 16!/(3!*13!) -> 560

    Parameters :
        number_of_options : int
            The number of options that each selection is choosing between (such as 16 billiards balls)
        count_choices_made : int 
            The number of times a choice is made (such as 3 of them going into the net)

    Returns : 
        total_possibilities : int
            The total number of possibilities for an unordered selection that does not allow repetition
    '''
    total_possibilities = factorialByPrimeFactors(number_of_options) / (factorialByPrimeFactors(count_choices_made)*factorialByPrimeFactors(number_of_options - count_choices_made))
    return total_possibilities

def combinationsWithRepetition(number_of_options, count_choices_made):
    '''
    This function calculates the number of possibilities for an unordered selection that does allow repetition

    total_possibilities = (number_of_options + count_choices_made -1)! / (count_choices_made! * (number_of_options - 1)!)

    An example would be finding the total number of possible combinations of 4 candy with 6 types
    -> (6+4-1)! / 4!(6-1)! -> 9! / (4!5!) -> 126

    Parameters :
        number_of_options : int
            The number of options that each selection is choosing between (such as 6 types of candy)
        count_choices_made : int 
            The number of times a choice is made (such as 4 pieces of candy)

    Returns : 
        total_possibilities : int
            The total number of possibilities for an unorder selection that does allow repetition
    '''

    numerator = factorialByPrimeFactors(number_of_options + count_choices_made - 1)
    denominator = factorialByPrimeFactors(count_choices_made) * factorialByPrimeFactors(number_of_options - 1)
    return numerator / denominator

if __name__ == '__main__':

    number = 12
    print(f"{number}! is loop:{factorialByLoop(number)}, recursion:{factorialByRecursion(number)}, and prime_factors:{factorialByPrimeFactors(number)} which are hopefully the same")

    print(f"The probability of rolling a 3  on a six sided dice is {probabilityOfASingleEvent(1,total_outcomes=6):.3f}")
    print(f"The probability of rolling a 3 and then a 5 on a six sided dice is {probabilityTwoIndependantEventsOccur(1,1,total_outcomes=6):.3f}")
    print(f"The total number of possible 4 digit [0-9] pins is {permutationsWithRepetition(10,4)}")
    print(f"The total number of possible orders that 4 of 16 billiards balls may go into a basket is {permutationWithoutRepetition(16,4)}")
    print(f"The total number of possible combinations that can be made with 4 of 16 billiards balls is {combinationsWithoutRepetition(16,4)}")
    print(f"The total number of possible combinations that can be made with 4 candies with 6 types is {combinationsWithRepetition(6,4)}")

    compareFactorialDurations()