# Solve the problem from the first set here

# 4.For a given natural number n find the largest natural
# number written with the same digits. (e.g. n=3658, m=8653).

def largest_number(x):
    """
    :param x: The given number.
    :return: Returns the largest number written with the same digits as the given number.
    """
    x = str(x)
    lx = list(x)  # copying the digits from the number x in a list
    lx.sort(reverse=True)  # sorting the digits in descending order
    c = ''
    for i in lx:
        c = c + i  # concatenating the digits stored in the list to form the new number
    b = int(c)
    return b


n = input("Please give a natural number n: ")
m = largest_number(n)
print(f"The largest natural number written with the same digits as {n} is {m}.")
