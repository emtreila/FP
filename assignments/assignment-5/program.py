import math
# Write the implementation for A5 in this file
#

# 
# Write below this comment 
# Functions to deal with complex numbers -- list representation
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#
""" 
def create_number(real, imag):
    return [real, imag]

def get_real(nr):
    return nr[0]

def get_imag(nr):
    return nr[1]

def set_real(nr, real):
    nr[0] = real

def set_imag(nr, imag):
    nr[1] = imag

def to_string(nr):
    return f"{nr[0]} + {nr[1]}i"
"""
#
# Write below this comment
# Functions to deal with complex numbers -- dict representation
# -> There should be no print or input statements in this section
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#


def create_number(real, imag):
    return {'real': real, 'imag': imag}

def get_real(nr):
    return nr['real']

def get_imag(nr):
    return nr['imag']

def set_real(nr, real):
    nr['real'] = real

def set_imag(nr, imag):
    nr['imag'] = imag

def to_string(nr):
    real = get_real(nr)
    imag = get_imag(nr)
    return f"{real} + {imag}i"


#
# Write below this comment 
# Functions that deal with subarray/subsequence properties
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#


#Set A (naive implementation): Determine the length and the elements of a longest subarray of numbers having the same modulus.
def modulus(nr):
    real = float(get_real(nr))
    imag = float(get_imag(nr))
    return math.sqrt(real ** 2 + imag ** 2)


def longest_subarray_same_modulus(nr):
    if not nr:
        return []

    max_len, max_subarray = 1, [nr[0]]
    current_len, current_subarray = 1, [nr[0]]
    current_modulus = modulus(nr[0])

    for i in range(1, len(nr)):
        if modulus(nr[i]) == current_modulus:
            current_len += 1
            current_subarray.append(nr[i])
        else:
            if current_len > max_len:
                max_len, max_subarray = current_len, current_subarray
            current_modulus = modulus(nr[i])
            current_len, current_subarray = 1, [nr[i]]

    if current_len > max_len:
        max_subarray = current_subarray

    return max_subarray

#Set B (dynamic programming implementation): Determine the length and the elements of a longest increasing subsequence, when considering each number's real part.

def longest_increasing_subsequence_real(nr):
    if not nr:
        return []

    n = len(nr)
    dp = [1] * n  # dp[i] = length of the longest increasing subsequence ending at index i
    prev = [-1] * n  # prev[i] = index of the previous element in the longest increasing subsequence ending at index i
    max_len = 1
    max_index = 0  # max_index = index of the last element of the longest increasing subsequence

    for i in range(1, n):
        for j in range(i):
            real_i = get_real(nr[i])
            real_j = get_real(nr[j])
            if real_i > real_j and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                prev[i] = j
        if dp[i] > max_len:
            max_len = dp[i]
            max_index = i

    subsequence = []
    while max_index != -1:
        subsequence.insert(0, nr[max_index])
        max_index = prev[max_index]

    return subsequence


#
# Write below this comment 
# UI section
# Write all functions that have input or print statements here
# Ideally, this section should not contain any calculations relevant to program functionalities
#

list_of_nr = [
        create_number(1, 2), create_number(3, 4), create_number(-3, -4),
        create_number(-3, 4), create_number(5, 0), create_number(2, 3),
        create_number(3, 4), create_number(1, 2), create_number(6, -3),
        create_number(4, 4)
    ]


option = 0
while option != 4:
    print()
    print("MENU")
    print("1.Read a list of complex numbers (in z = a + bi form).")
    print("2.Display the entire list of numbers on the console.")
    print("3.Display the subsequence/subarray with some properties")
    print("4.Exit the menu.")
    option = int(input("Please choose from the menu above:"))


    if option == 4:
        print("You have exited the menu. Bye, bye!")

    elif option == 1:
        list_of_nr=[]
        n=int(input("How many numbers do you want in your list?"))
        while n:
            real=input("Give the real part:")
            imag=input("Give the imaginary part:")
            complex_number = create_number(real,imag)
            list_of_nr.append(complex_number)
            n-=1

    elif option == 2:
        for i in list_of_nr:
            print(to_string(i))

    elif option == 3:
        subarray = longest_subarray_same_modulus(list_of_nr)
        length_1 = len(subarray)
        print("Longest subarray with the same modulus:")
        for i in subarray:
            print(to_string(i))
        print(f"Length: {length_1}")
        subsequence = longest_increasing_subsequence_real(list_of_nr)
        print("Longest increasing subsequence based on real parts:")
        for i in subsequence:
            print(to_string(i))
        length_2 = len(subsequence)
        print(f"Length: {length_2}")



