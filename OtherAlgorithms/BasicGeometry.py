import math

def rightTriangle_calculateHypotenuse_GivenTwoSides(a_side, b_side):
    '''
    This function calculate the hypotenuse of a right triangle given two sides

    Parameter :
        a_side : number
            One side of the triangle
        b_side : number
            One side of the triangle

    Returns : 
        hypotenuse : number
            The length of the hypotenuse
    '''

    a_squared = a_side ** 2
    b_squared = b_side ** 2
    sqrt_sum = (a_squared + b_squared) ** .5

    return sqrt_sum

def rightTriangle_calculateSide_GivenSideHypotenuse(given_side, hypotenuse):
    '''
    This function calculate one side of a right triangle given one sides and the hypotenuse

    Parameter :
        given_side : number
            One side of the triangle
        hypotenuse : number
            The hypotenuse of the triangle

    Returns : 
        other_side : number
            The length of the other side
    '''

    side_squared = given_side ** 2
    hypotenuse_squared = hypotenuse ** 2
    sqrt_diff = (hypotenuse_squared -side_squared) ** .5

    return sqrt_diff

def polynomial_calculateInteriorAngleSum(number_of_sides):
    '''
    This function calculates the sum of the interior angles of a polynomial given the number of sides

    Paramters :
        number_of_sides : int
            The number of sides of the polynomial

    Returns :
        sum_of_interior_angles : int
            The sum of the interior angles of the polynomial
    '''

    return (number_of_sides - 2) * 180

def square_calculateArea(side):
    '''
    This function calculates the area of a square given the length of one side

    Parameters :
        side : number
            The length of one side
    
    Returns :
        area : number
            The area of the square
    '''

    return side ** 2

def square_calculatePerimeter(side):
    '''
    This function calculates the perimeter of a square given the length of one side

    Parameters :
        side : number
            The length of one side
    
    Returns :
        perimeter : number
            The perimeter of the square
    '''
    
    return side * 4

def rectangle_calculateArea(length, width):
    '''
    This function calculates the area of a rectangle given the length and the width

    Parameters :
        length : number
            The length of the rectangle
        width : number 
            The width of the rectangle
    
    Returns :
        area : number
            The area of the rectangle
    '''

    return length * width

def rectangle_calculatePerimeter(length, width):
    '''
    This function calculates the perimeter of a rectangle given the length and the width

    Parameters :
        length : number
            The length of the rectangle
        width : number 
            The width of the rectangle
    
    Returns :
        perimeter : number
            The perimeter of the rectangle
    '''

    return 2 * (length + width)

def triangle_calculateArea(height, width):
    '''
    This function calculates the area of a triangle given the height and the width

    Parameters :
        height : number
            The height of the triangle
        width : number 
            The width of the rectangle
    
    Returns :
        area : number
            The area of the triangle
    '''

    return height * width / 2

def circle_calculateArea(radius):
    '''
    This function calculates the area of a circle given it's radius

    Parameters : 
        radius : number
            The radius of the circle

    Returns :
        area : number
            The area of the circle
    '''

    return math.pi * radius ** 2

def circle_calculatePerimeter(radius):
    '''
    This function calculates the perimeter of a circle given its radius

    Parameters : 
        radius : number
            The radius of the circle

    Returns : 
        perimeter : number
            The perimeter of the circle
    '''

    return math.pi * 2 * radius

if __name__ == '__main__':
    print(f"a right triangle with a side of 3 and a side of 4 will have a hypotenuse : {rightTriangle_calculateHypotenuse_GivenTwoSides(3, 4)}")
    print(f"a triangle with a side of 3 and hypontenuse of 5 will have a second side of : {rightTriangle_calculateSide_GivenSideHypotenuse(given_side=3, hypotenuse=5)}")
    print(f"a polynomial with 6 sides will have an interior angle sum of : {polynomial_calculateInteriorAngleSum(6)}")
    print(f"a square with sides of 5 will have an area of : {square_calculateArea(5)}")
    print(f"a square with sides of 5 will have a perimeter of : {square_calculatePerimeter(5)}")
    print(f"A rectangle with a length 4 and a width 3 will have an area of : {rectangle_calculateArea(length=4, width=3)}")
    print(f"A rectangle with a length 4 and a width 3 will have an perimeter of : {rectangle_calculatePerimeter(length=4, width=3)}")
    print(f"a triangle with height 5 and width 3 will have an area of : {triangle_calculateArea(height=5, width=3)}")
    print(f"a circle with radius 4 will have an area of : {circle_calculateArea(4):.2f}")
    print(f"a circle with radius 4 will have a perimeter of : {circle_calculatePerimeter(4):.2f}")