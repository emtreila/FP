"""
 11) Two natural numbers m and n are given. Display in all possible modalities the numbers from 1 to n,
 such that between any two numbers on consecutive positions, the difference in absolute value is at least m.
 If there is no solution, display a message.
"""

def find_sequences_iterative(n, m):
    stack = []
    solutions = []

    for i in range(1, n + 1): # appends a tuple ([i], i) to the stack
        stack.append(([i], i)) #[i]: A list containing the single element i.
                               #i: An integer representing the current value of i

    while stack:
        current_sequence, last_number = stack.pop()
        if len(current_sequence) == n:
            solutions.append(current_sequence)
            continue

        for i in range(1, n + 1):
            if abs(i - last_number) >= m:
                new_sequence = current_sequence + [i] # create a new sequence with the added number
                stack.append((new_sequence, i))

    if solutions:
        for seq in solutions:
            print(seq)
    else:
        print("There is no solution.")


n = int(input("The value of n is:"))
m = int(input("The value of m is:"))
find_sequences_iterative(n, m)
