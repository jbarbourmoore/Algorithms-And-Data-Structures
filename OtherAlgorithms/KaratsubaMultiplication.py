def convertDecimalToBinary(decimal_number):
    '''
    This function converts a positive decimal integer into a binary number as a reversed list of 0s and 1s

    It uses modulous division by to determine if the next binary digit is a zero or one
    It uses integer divisoion so the decimal number decreases by a factor of so and the next binary digit can be calculates

    Parameters : 
        decimal_number : int
            A positive integer value in decimal notation to be converted into binary

    Returns :
        binary_number_list : [int]
            A list holding each 0 or 1 for the binary number as a separate element
    '''

    binary_number_list = []

    if decimal_number == 0:
        binary_number_list.append(0)
    
    # This loop goes through all of the values in the decimal number to construct a binary array from its highest binary digit
    #
    # decimal = 82 binary array = []
    # decimal = 41 binary array = [1,0]
    # decimal = 20 binary array = [0,1,0]
    # decimal = 10 binary array = [0,0,1,0]
    # decimal = 5 binary array = [1,0,0,1,0]
    # decimal = 2 binary array = [0,1,0,0,1,0]
    # decimal = 1 binary array = [1,0,1,0,0,1,0]
    while decimal_number > 0:
        binary_number_list.insert(0, decimal_number % 2)
        decimal_number = decimal_number // 2

    return binary_number_list 

def convertBinaryToDecimal(binary_number_list):
    '''
    This number converts a positive binary integer into a decimal value

    Parameters :
        binary_number_list : [int]
            The binary number with each of its bits stored as a separate item in a list

    Returns :
        decimal_number : int
            The decimal number equivalent to the binary number list
    '''

    decimal_number = 0
    binary_number_length = len(binary_number_list)

    # This loop goes through all of the bits in the binary number 
    # and multiplies them by their corresponding factor of two in order to sum the totals to convert to binary
    #
    # decimal : 0 += [1, 0, 1, 0, 0, 1, {0}][6] * 2**0 => 0 * 1 = 0
    # decimal : 0 += [[1, 0, 1, 0, 0, {1}, 0][5] * 2**1 => 1 * 2 = 2
    # decimal : 2 += [1, 0, 1, 0, {0}, 1, 0][4] * 2**2 => 0 * 4 = 2
    # decimal : 2 += [1, 0, 1, {0}, 0, 1, 0][3] * 2**3 => 0 * 8 = 2
    # decimal : 2 += [1, 0, {1}, 0, 0, 1, 0][2] * 2**4 => 1 * 16 = 18
    # decimal : 18 += [1, {0}, 1, 0, 0, 1, 0][1] * 2**5 => 0 * 32 = 18
    # decimal : 18 += [{1}, 0, 1, 0, 0, 1, 0][0] * 2**5 => 1 * 64 = 82
    for n in range(0, binary_number_length):
        nth_power_of_2 = 2**n

        decimal_number += binary_number_list[binary_number_length - 1 - n] * nth_power_of_2

    
    return decimal_number 

def testDecimalToBinaryToDecimal(original_decimal):
    '''
    This function tests the the decimal number can be converted to binary and the back to decimal successfully

    Parameters :
        original_decimal : int
            The decimal number being convert to binary
    '''

    binary_from_decimal = convertDecimalToBinary(original_decimal)
    decimal_from_binary = convertBinaryToDecimal(binary_from_decimal)

    assert original_decimal == decimal_from_binary

    print(f"binary : {binary_from_decimal} <-> decimal : {decimal_from_binary}")

def bitwiseAddition(first_bit, second_bit, carry_bit):
    '''
    This function adds a bit from two binary nummbers as well as a carry bit (three digits total that are 0 or 1)

    Parameters :
        first_bit : int (0 or 1)
            The bit from the first number being added
        second_bit : int (0 or 1)
            The bit from the second number being added
        carry_bit : int (0 or 1)
            The bit being carried over from the bitwaise addition of the previous two bits 

    Returns : 
        result : int (0 or 1)
            The result of the addition operation for this bit is the first value in the tuple
        carry_bit : int (0 or 1)
            If there is a value to carry into the next bit of the addition is the second value in the tuple
    '''
    
    if first_bit == 0:
        if second_bit == 0:
            # If both first and second bits are 0, the result is simply the carry bit and the new carry bit is 0
            return (carry_bit, 0)
        else:
             # If the first bit is 0 and second bit is 1, the result is simply one minus the carry bit and the new carry bit is the same as this one
            #print("second is 1, first is 0")
            #print(f"carry_bit:{carry_bit}  -> ({1-carry_bit}, {carry_bit})")
            return (1-carry_bit, carry_bit)
    else:
        if second_bit == 0:
            # If the first bit is 1 and second bit is 0, the result is simply one minus the carry bit and the new carry bit is the same as this one
            return (1-carry_bit, carry_bit)
        else:
            # If both first and second bits are 0, the result is simply the carry bit and the new carry bit is 1
            #print("both are 1")
            return (carry_bit, 1)
        
def binaryAddition(first_binary_number, second_binary_number):
    '''
    This function adds together two binary numbers

    Parameters :
        first_binary_number : [int]
            The first number to be added together as a bit array
        second_binary_number : [int]
            The second number to be added together as a bit array

    Returns :
        result_binary_number : [int]
            The result of the addition as a bit array
    '''

    first_binary_length = len(first_binary_number)
    second_binary_length = len(second_binary_number)
    max_length = max(second_binary_length,first_binary_length)

    carry_bit = 0
    result_binary_number = []

    # This goes through every element in both binary numbers from the smallest to the largest, adding them bitwise with carry
    # If one of the binary numbers is larger than the other al the preceeding digits of the smaller number are assumed to be 0
    #
    # 0: [  1, 0, {0}]:[0] + [1, 1, 0, {1}]:[1] + c[0] = [1] + c[0] = [1]
    # 1: [  1, {0}, 0]:[0] + [1, 1, {0}, 1]:[0] + c[0] = [0] + c[0] = [0, 1]
    # 2: [  {1}, 0, 0]:[1] + [1, {1}, 0, 1]:[1] + c[0] = [0] + c[1] = [0, 0, 1]
    # 3: [{}, 1, 0, 0]:[0] + [{1}, 1, 0, 1]:[1] + c[1] = [0] + c[1] = [0, 0, 0, 1]
    for i in range(0, max_length):
        first_bit = 0
        second_bit = 0
        if i < first_binary_length :
            first_bit = first_binary_number[first_binary_length-i-1]
        if i < second_binary_length:
            second_bit = second_binary_number[second_binary_length-i-1]
        (result_bit, carry_bit) = bitwiseAddition(first_bit, second_bit, carry_bit)
        result_binary_number.insert(0, result_bit)
    
    # if there is still a carry bit after the loop is completed that is appended to the front of the result
    # C: [{},  , 1, 0, 0]:[0] + [{}, 1, 1, 0, 1]:[0] + c[1]  = [1, 0, 0, 0, 1]
    if carry_bit == 1:
        result_binary_number.insert(0, carry_bit)


    return result_binary_number

def testBinaryAddition(first_decimal_number, second_decimal_number):
    '''
    This function tests adding two numbers together with binary addition

    It converts two decimal numbers to binary, adds them togerther and then converts that back to decimal.
    This result is then compared to the value from decimal addition to assertain the binary addition's accuracy

    Parameters :
        first_decimal_number : int
            The first decimal number to add together
        second_decimal_number : int
            The second decimal number to add together

    '''

    original_decimal_sum = first_decimal_number + second_decimal_number

    first_binary_number = convertDecimalToBinary(first_decimal_number)
    second_binary_number = convertDecimalToBinary(second_decimal_number)

    result_binary_sum = binaryAddition(first_binary_number=first_binary_number, second_binary_number=second_binary_number)
    result_decimal_sum = convertBinaryToDecimal(result_binary_sum)


    print(f"{first_decimal_number}:{first_binary_number} + {second_decimal_number}:{second_binary_number} = {result_decimal_sum}:{result_binary_sum}")
    assert original_decimal_sum == result_decimal_sum

def binarySubtraction(first_binary_number, second_binary_number):
    '''
    This function performs binary subtraction using two's complement

    Two's complement works by flipping all of the bits of the number to be subtracted and then adding one to it
    This number is then added to the number from which it is being subtracted

    Parameters :
        first_binary_number : [int]
            The first number to be subtracted from as a bit array
        second_binary_number : [int]
            The second number to be subtracted as a bit array

    Returns :
        result_binary_number : [int]
            The result of the subtraction as a bit array 
    ''' 
    first_binary_length = len(first_binary_number)
    second_binary_length = len(second_binary_number)

    # since I am so far working with positive numbers and don't really have a set binary array size with which to implement the negative numbers
    assert first_binary_length >= second_binary_length

    # if the second binary number is shorter than the first binary number then 0s are added to the front so they are the same length without changing the value
    padding_length = len(first_binary_number) - len(second_binary_number)    
    for _ in range(0,padding_length):
        second_binary_number.insert(0,0)
    
    # the 2s complement is calculated for the second binary number by flipping every bit and then adding 1
    second_binary_complement = [1-bit_value for bit_value in second_binary_number]
    second_binary_complement = binaryAddition(second_binary_complement, [1])

    # the first binary number and the second binary complement are added together and any front carry value is removed
    result = binaryAddition(first_binary_number, second_binary_complement)
    if len(result) > first_binary_length :
        result = result[1:first_binary_length+1]
   # print(f"{first_binary_number} - {second_binary_number}")
    original_decimal_subtract = convertBinaryToDecimal(first_binary_number) - convertBinaryToDecimal(second_binary_number)
    #print(f"{convertBinaryToDecimal(first_binary_number)}:{first_binary_number} i {convertBinaryToDecimal(second_binary_number)}:{second_binary_number} = {original_decimal_subtract}:{convertBinaryToDecimal(result)}")
    assert original_decimal_subtract == convertBinaryToDecimal(result)

    return result

def testBinarySubtraction(first_decimal_number, second_decimal_number):
    '''
    This function tests subtracting two numbers with binary subtraction

    It converts two decimal numbers to binary, subtracts them  and then converts that back to decimal.
    This result is then compared to the value frm decimal subtraction to assertain the binary subtraction's accuracy

    Parameters :
        first_decimal_number : int
            The first decimal number to subtract from
        second_decimal_number : int
            The second decimal number to be subtracted
    '''

    original_decimal_subtract = first_decimal_number - second_decimal_number

    first_binary_number = convertDecimalToBinary(first_decimal_number)
    second_binary_number = convertDecimalToBinary(second_decimal_number)

    result_binary_subtract = binarySubtraction(first_binary_number=first_binary_number, second_binary_number=second_binary_number)
    result_decimal_subtract = convertBinaryToDecimal(result_binary_subtract)

    print(f"{first_decimal_number}:{first_binary_number} i {second_decimal_number}:{second_binary_number} = {result_decimal_subtract}:{result_binary_subtract}")
    assert original_decimal_subtract == result_decimal_subtract

def gradeSchoolBinaryMultiplication(first_binary_number, second_binary_number):
    '''
    This function performs binary multiplication using the grade school method

    Parameters :
        first_binary_number : [int]
            The first number to be multiplied together as a bit array
        second_binary_number : [int]
            The second number to be multiplied together as a bit array

    Returns :
        result_binary_number : [int]
            The result of the multiplication as a bit array 
    ''' 
    first_binary_length = len(first_binary_number)
    second_binary_length = len(second_binary_number)
    
    temporary_number = first_binary_number
    result = [0]

    # this loop goes through every bit in the second binary number from smallest to largest
    # if the bit is 1, it adds the tempory number to the result number
    # the result number is shifted to the left each iteration 
    #
    # first used for temp->5*[1, 0, 1] * 9*[1, 0, 0, 1]<-second used for bit each loop
    # 0: bit:1 * temp:[0, 0, 0, 1, 0, 1] + prev_result[0, 0, 0] = result:[0, 0, 0, 1, 0, 1]
    # 1: bit:0 * temp:[0, 0, 1, 0, 1, 0] + prev_result[1, 0, 1] = result:[0, 0, 0, 1, 0, 1]
    # 2: bit:0 * temp:[0, 1, 0, 1, 0, 0] + prev_result[1, 0, 1] = result:[0, 0, 0, 1, 0, 1]
    # 3: bit:1 * temp:[1, 0, 1, 0, 0, 0] + prev_result[1, 0, 1] = result:[1, 0, 1, 1, 0, 1]
    #
    # 5:[1, 0, 1] * 9:[1, 0, 0, 1] = 45:[1, 0, 1, 1, 0, 1]
    for i in range(0, second_binary_length):
        
        bit = second_binary_number[second_binary_length-i-1]
        if bit == 1:
            result = binaryAddition(result, temporary_number)
        
        temporary_number = temporary_number + [0]
    return result 

def testGradeSchoolBinaryMultiplication(first_decimal_number, second_decimal_number):
    '''
    This function tests subtracting two numbers with binary subtraction

    It converts two decimal numbers to binary, subtracts them  and then converts that back to decimal.
    This result is then compared to the value frm decimal subtraction to assertain the binary subtraction's accuracy

    Parameters :
        first_decimal_number : int
            The first decimal number to subtract from
        second_decimal_number : int
            The second decimal number to be subtracted

    '''

    original_decimal_multiply = first_decimal_number * second_decimal_number

    first_binary_number = convertDecimalToBinary(first_decimal_number)
    second_binary_number = convertDecimalToBinary(second_decimal_number)

    result_binary_multiply = gradeSchoolBinaryMultiplication(first_binary_number=first_binary_number, second_binary_number=second_binary_number)
    result_decimal_multiply = convertBinaryToDecimal(result_binary_multiply)

    print(f"{first_decimal_number}:{first_binary_number} * {second_decimal_number}:{second_binary_number} = {result_decimal_multiply}:{result_binary_multiply}")
    assert original_decimal_multiply == result_decimal_multiply

def padBinaryNumberRight(binary_number, amount_of_padding):
    return  binary_number+[0]*amount_of_padding 

def karatsubaBinaryMultiplication(first_binary_number, second_binary_number):
    '''
    This function multiplies two binary numbers using Karatsubas Binary Muliplication

    Parameters :
        first_binary_number : [int]
            one of the binary numbers to be multiplied
        second_binary_number : [int]
            one of the binary numbers to be multiplied
    
    Returns :
        first_binary_number : [int]
            The binary number that is the result of this multiplication
    '''
    
    first_binary_length = len(first_binary_number)
    second_binary_length = len(second_binary_number)
    max_length = max(first_binary_length, second_binary_length)

    if first_binary_length <= 2 or second_binary_length <= 2:
        return gradeSchoolBinaryMultiplication(first_binary_number, second_binary_number)
    
    else:
        half_max_length = max_length // 2

        first_binary_number, second_binary_number = equalizeBinaryLength(first_binary_number,second_binary_number)
        
        first_leading, first_trailing = first_binary_number[:half_max_length], first_binary_number[half_max_length:]
        second_leading, second_trailing = second_binary_number[:half_max_length], second_binary_number[half_max_length:]

        multiply_leading = karatsubaBinaryMultiplication(first_leading, second_leading)
        multiply_trailing = karatsubaBinaryMultiplication(first_trailing, second_trailing)
        multiply_cross_sums = karatsubaBinaryMultiplication(binaryAddition(first_leading, first_trailing), binaryAddition(second_leading, second_trailing))
        cross_multiply_minus_trailing_leading = binarySubtraction(multiply_cross_sums, binaryAddition(multiply_leading, multiply_trailing))

        rasult_with_potential_zeros = binaryAddition(binaryAddition(multiply_leading + [0] * max_length, cross_multiply_minus_trailing_leading + [0] * half_max_length), multiply_trailing)
        result = removeLeadingZeros(rasult_with_potential_zeros)
        return result

def removeLeadingZeros(binary_number):
    '''
    This function removes the leading zeros from a binary number

    Paraneters : 
        binary_number : [int]
            The binary number for which you are removing the leading zeros

    Returns :
        binary_number :[int]
            The binary number without the leading zeros
    '''

    if 1 not in binary_number:
        return[0]
    index_first_one =binary_number.index(1)
    return binary_number[index_first_one:]

def equalizeBinaryLength(first_binary_number, second_binary_number):
    '''
    This function utilizes leading zeros to equalize the length of two binary numbers

    Parameters :
        first_binary_number : [int]
            one of the binary numbers to be equalized
        second_binary_number : [int]
            one of the binary numbers to be equalized
    
    Returns :
        first_binary_number : [int]
            one of the binary numbers that now have equal length
        second_binary_number : [int]
            one of the binary numbers that now have equal length
    '''

    first_binary_length = len(first_binary_number)
    second_binary_length = len(second_binary_number)

    max_length = max(first_binary_length, second_binary_length)
    min_length = min(first_binary_length, second_binary_length)
    padding_length = max_length - min_length

    if max_length > first_binary_length:
        first_binary_number = [0]*padding_length + first_binary_number
    elif max_length > second_binary_length:
        second_binary_number = [0]*padding_length + second_binary_number
    return first_binary_number, second_binary_number
    
def testKaratsubaBinaryMultiplication(first_decimal_number, second_decimal_number):
    '''
    This function tests subtracting two numbers with binary subtraction

    It converts two decimal numbers to binary, subtracts them  and then converts that back to decimal.
    This result is then compared to the value frm decimal subtraction to assertain the binary subtraction's accuracy

    Parameters :
        first_decimal_number : int
            The first decimal number to subtract from
        second_decimal_number : int
            The second decimal number to be subtracted

    '''

    original_decimal_multiply = first_decimal_number * second_decimal_number

    first_binary_number = convertDecimalToBinary(first_decimal_number)
    second_binary_number = convertDecimalToBinary(second_decimal_number)

    result_binary_multiply = karatsubaBinaryMultiplication(first_binary_number, second_binary_number)
    result_decimal_multiply = convertBinaryToDecimal(result_binary_multiply)

    print(f"{original_decimal_multiply == result_decimal_multiply} - {first_decimal_number}:{first_binary_number} * {second_decimal_number}:{second_binary_number} = {result_decimal_multiply}:{result_binary_multiply}")
    assert original_decimal_multiply == result_decimal_multiply   
    return   original_decimal_multiply == result_decimal_multiply

if __name__ == '__main__':

    testDecimalToBinaryToDecimal(82)
    testDecimalToBinaryToDecimal(5)
    testDecimalToBinaryToDecimal(253)

    testBinaryAddition(4,13)
    testBinaryAddition(21,82)
    testBinaryAddition(523,102)

    testBinarySubtraction(13,4)
    testBinarySubtraction(12,12)
    testBinarySubtraction(524,234)

    testGradeSchoolBinaryMultiplication(5,9)
    testGradeSchoolBinaryMultiplication(12,12)
    testGradeSchoolBinaryMultiplication(1,0)

    testKaratsubaBinaryMultiplication(6,12)
    testKaratsubaBinaryMultiplication(8, 8)
    testKaratsubaBinaryMultiplication(12, 12)
