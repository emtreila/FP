# Solve the problem from the third set here

# 13. Determine the n-th element of the sequence 1,2,3,2,5,2,3,7,2,3,2,5,...obtained from the sequence of
# natural numbers by replacing composed numbers with their prime divisors, without memorizing the elements of the sequence.


def prime_divisors(n):
    """
    :param n: The given number.
    :return: The n-th element obtained from the sequence of natural numbers by replacing composed numbers with their prime divisors.
    """
    if n <= 1:
        return 1
    nr = 2  # nr=the number that is replaced with its prime divisors
    n -= 1  # n drops until it becomes 0, which means it reaches the n-th element
    while True:
        d = 2  # d=the divisor
        x = nr
        while x != 1:
            if x % d == 0:  # if d is a divisor for x, we check to see how many divisors are left until n becomes 0
                n -= 1
                if n == 0:
                    return d
                while x % d == 0:  # if n is still not 0, we divide x until we have to use another divisor
                    x = x // d
            d += 1
        nr += 1


n = int(input("Please give a natural number n: "))
print(
    f"The {n}-th element obtained from the sequence of natural numbers by replacing composed numbers with their prime divisors is",
    prime_divisors(n))
