import random

def generate_random_length_array():
    '''
    Helper function which generates a random length array
     
    The array is of random integers between 0 and 50 and the length is between 10 and 30
    
     Returns :
        array : [int]
            An array of random length filled with random values between 0 and 50
    '''

    array_length = random.randint(10,30)

    array = []
    for _ in range(0,array_length):
        array.append(random.randint(0,50))
    return array


def generate_random_array(array_length=10,min_value=0,max_value=30):
    '''
    Helper function which generates a random array 
    
    The array is of array_length where each value is between min_value and max_value

    Parameters :
        array_length : int, optional
            The length of the array (default is 10)
        min_value : int, optional
            The minimum possible value of any array element (default is 0)
        max_value : int, optional
            The maximum possible value of any array element (default is 30)

    Returns :
        array : [int]
            An array of array_length filled with random values between min_value and max_value
    '''

    array = []
    for _ in range(0,array_length):
        array.append(random.randint(min_value,max_value))
    return array