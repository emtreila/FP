"""
2) Given the set of positive integers S and the natural number k, display one of the subsets of S which sum to k.
For example, if S = { 2, 3, 5, 7, 8 } and k = 14, subset { 2, 5, 7 } sums to 14.
"""


def find_subset(S, k):
    def subset_sum(S, k, current_subset):
        if k == 0:
            return current_subset  # k=0 -> we found a subset that sums to k
        if not S:
            return None  # set=empty, k!=0 ->no subset can sum to k

        first_elem = S[0]
        rest_of_elem = S[1:]
        if k >= first_elem:
            result_with = subset_sum(rest_of_elem, k - first_elem, current_subset + [first_elem])
            if result_with is not None: # if a subset that sums to k is found -> it is stored in result_with
                return result_with

        result_without = subset_sum(rest_of_elem, k, current_subset) # without the first element
        return result_without # if a subset that sums to k is found -> it is stored in result_without

    return subset_sum(S, k,[])

S=list(map(int, input("The set of positive integers: ").split(' ')))
k=int(input("The sum is:"))
result = find_subset(list(S),int(k))
print(result)
