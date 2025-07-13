# Solve the problem from the second set here

# 8.Find the smallest number m from the Fibonacci sequence, defined by f[0]=f[1]=1, f[n]=f[n-1] + f[n-2], for n > 2,
# larger than the given natural number n. (e.g. for n = 6, m = 8).

def fib_nr(x):
    """
    :param x: The given number.
    :return: Returns the smallest number from the Fibonacci sequence,larger than the given number.
    """
    a = 1  # a and b are the first elements from the Fibonacci sequence
    b = 1
    f = a + b
    while x >= f:
        a = b
        b = f
        f = a + b
    return f


n = int(input("Please give a natural number n: "))
m = fib_nr(n)
print(f"The smallest number from the Fibonacci sequence,larger than the given number {n} is {m}.")
