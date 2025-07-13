"""
 11) Two natural numbers m and n are given. Display in all possible modalities the numbers from 1 to n,
 such that between any two numbers on consecutive positions, the difference in absolute value is at least m.
 If there is no solution, display a message.
"""

def find_sequences_back(m, n):
    solutions = []
    def backtrack(current_sequence):
        if len(current_sequence) == n:
            solutions.append(current_sequence[:])
            return
        for i in range(1, n + 1):  # we try to add each number from 1 to n as the next element in the sequence
            if not current_sequence or abs(current_sequence[-1] - i) >= m:
                current_sequence.append(i)
                backtrack(current_sequence)
                current_sequence.pop() # remove `i` to try a new possibility

    backtrack([])
    if solutions:
        for seq in solutions:
            print(seq)
    else:
        print("There is no solution.")


n = int(input("The value of n is:"))
m = int(input("The value of m is:"))
find_sequences_back(m, n)
