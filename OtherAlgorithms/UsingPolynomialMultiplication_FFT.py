from numpy.fft import fft, ifft
from numpy import real

def polynomialMultiplication_FFT(a_polynomial_as_coefficients_list, b_polynomial_as_coefficients_list):
    '''
    This function takes in two polynomials as a list of coefficients and returns a similar list for the polynomial that results from the multiplication

    It relies on using the Fast Fourier Transform to convert both polynomial coefficient lists, 
        multiplying each corresponing coefficient from both lists (pointwise multiplication),
        and then using the inverse fourier transform to return it to a polynomial coefficient list.

    polynomial = a0 + a1x + a2x**2 + a3x**3 + a4x**4 + .... + a(n-1)x**(n-1) + anx**n
    ==> list format = [a0, a1, a2, a3, a4, ..., a(n-1)x**(n-1), anx**n]

    Parameters :
        a_polynomial_as_coefficients_list : [int]
            The first polynomial to be multiplied, as a list of coefficient values
        b_polynomial_as_coefficients_list : [int]
            The first polynomial to be multiplied, as a list of coefficient values

    Returns :
        real_polynomial_multiplied_as_coefficients_list : [int]
            The polynomial result of the multiplication as a list of coefficient values
    '''

    length_a = len(a_polynomial_as_coefficients_list)
    length_b = len(b_polynomial_as_coefficients_list)
    expected_result_length = length_a + length_b - 1

    a_coefficients_padded = a_polynomial_as_coefficients_list + (expected_result_length-length_a)*[0]
    b_coefficients_padded = b_polynomial_as_coefficients_list + (expected_result_length-length_b)*[0]
    
    a_fft = fft(a_coefficients_padded)
    b_fft = fft(b_coefficients_padded)
    
    multiplied_fft = [a_fft[index]*b_fft[index] for index in range(0,expected_result_length)]

    multiplied_polynomial = ifft(multiplied_fft)

    real_polynomial_multiplied_as_coefficients_list = [real(coefficient) for coefficient in multiplied_polynomial]

    return real_polynomial_multiplied_as_coefficients_list

def checkForSum_FFTPolynomialMultiplication(a_set, b_set, c_set):
    '''
    This function checks if any value in c_set is the sum of any number in a_set with any number in b_set

    It converts the a_set and b_set to lists of polynomal coefficients and uses fast fourier transformation to multiply them.
    Then it compares the result list of polynomial coefficients with the values in c_set and returns true if one matches
    It relies on polynomial multiplication producing exponents that correspond with the sums of the exponents in the polynomials that were multiplied

    Parameters :
        a_set : (int)
            The first set to used to create the sums that may be in set_c
        b_set : (int)
            The second set to be used to create the sums that may be in set_c
        c_set : (int)
            The list of values that may contain values that are the sum of any value in set_a and any value in set_b
    '''

    maximum_number_in_any_set = max(max(a_set), max(b_set), max(c_set))
    
    a_polynomial_coefficients = [0]*(maximum_number_in_any_set + 1)
    b_polynomial_coefficients = [0]*(maximum_number_in_any_set + 1)
    
    for value in a_set:
        a_polynomial_coefficients[value] = 1
    for value in b_set:
        b_polynomial_coefficients[value] = 1

    multiplied_polynomial_coefficients = polynomialMultiplication_FFT(a_polynomial_coefficients, b_polynomial_coefficients)
    multiplied_polynomial_coefficients = [round(abs(coefficient)) for coefficient in multiplied_polynomial_coefficients]

    for value in c_set:
        if multiplied_polynomial_coefficients[value] >= 1 :
            return True
    return False

def checkForSum(a_set, b_set, c_set):
    '''
    This function checks if any value in c_set is the sum of any number in a_set with any number in b_set

    It sums every value of a_set with every value of b_set and then sees if c contains any of those values

    Parameters :
        a_set : (int)
            The first set to used to create the sums that may be in set_c
        b_set : (int)
            The second set to be used to create the sums that may be in set_c
        c_set : (int)
            The list of values that may contain values that are the sum of any value in set_a and any value in set_b
    '''

    sums_a_b = []
    for a in a_set:
        for b in b_set:
            sums_a_b.append(a+b)
    
    for c in c_set:
        if c in sums_a_b:
            return True
    return False