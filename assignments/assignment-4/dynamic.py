"""
2) Given the set of positive integers S and the natural number k, display one of the subsets of S which sum to k.
For example, if S = { 2, 3, 5, 7, 8 } and k = 14, subset { 2, 5, 7 } sums to 14.
"""


def find_subset(S, k):
    """
        We create a 2D boolean matrix where:
                -> dp[i][j] = True if a subset of the first i elements in S can sum up to j
                -> dp[i][j] = False otherwise

        S[i-1] (the (i-1)-th element of S, because matrix indexing starts from 1 while S indexing starts from 0).
    """
    n = len(S)
    matrix = []
    for i in range(n + 1):     # initialize the matrix with False values
        matrix.append([])
        for j in range(k + 1):
            matrix[i].append(False)

    for i in range(n + 1): # a sum of 0 can be achieved with an empty subset
        matrix[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if j < S[i - 1]:  # if the element is larger than the sum j
                # exclude the element
                matrix[i][j] = matrix[i - 1][j]
            else:
                # either exclude or include the element
                matrix[i][j] = matrix[i - 1][j] or matrix[i - 1][j - S[i - 1]]

    print("(Rows: elements considered (i)    Columns: target sums up to k (j))")
    header = ["   "]
    for j in range(k + 1):
        header.append(f"{j:>2}")  # append each sum value with formatted width
    print(" ".join(header))

    separator = "   " + "-" * ((k + 1) * 4)  # multiply the number of dashes based on the number of columns
    print(separator)


    for i in range(n + 1):
        if i == 0:
            row_label = f"{i} "  # the first row
        else:
            row_label = f"{i}({S[i - 1]})"  # show the index and the element in S
        row_data = []
        for value in matrix[i]:
            if value:
                row_data.append("T")
            else:
                row_data.append("F")

        formatted_row_data = " ".join(f"{x:>2}" for x in row_data)
        print(f"{row_label:<4} " + formatted_row_data)

    # if no subset with sum k exists, return None
    if not matrix[n][k]:
        return None

    # backtrack to find one subset that sums to k
    subset = []
    i, j = n, k
    while i > 0 and j > 0:
        if matrix[i][j] and not matrix[i - 1][j]: # matrix[i][j] -> True means we can achieve a sum of j using the first i elements
            subset.append(S[i - 1])               # not matrix[i - 1][j] -> True if the previous row (matrix[i-1][j]) does not allow us to reach the sum j without using S[i-1].
            j -= S[i - 1]                         # if both conditions are True -> the element S[i-1] was included in the subset in order to achieve the sum j.
        i -= 1

    return subset


S=list(map(int, input("The set of positive integers: ").split(' ')))
k=int(input("The sum is:"))
result = find_subset(S, k)
if result:
    print(f"Subset that sums to {k}: {result}")
else:
    print("No subset found")
