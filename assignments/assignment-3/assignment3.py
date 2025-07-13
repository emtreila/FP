import random
import timeit


def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1


def search1(rndlst, nr):
    result = binary_search(rndlst, 0, len(rndlst) - 1, nr)
    if result != -1:
        print(f"The position of the number you selected is: {result}")
    else:
        print("The number you entered isn't in the list.")


def search1_var2(rndlst, nr):
    binary_search(rndlst, 0, len(rndlst) - 1, nr)


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    return arr


def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


def permuteRec(arr, idx, step, steps):
    if idx == len(arr) - 1:
        step += 1

        if step % steps == 0:
            print(f"On step {step}, the list is: {arr}")
        if is_sorted(arr):
            return arr, step
        return None, step

    for i in range(idx, len(arr)):
        # Swapping
        arr = swap(arr, idx, i)

        rez, step = permuteRec(arr, idx + 1, step, steps)
        if rez:
            return arr, step

        # Backtrack
        arr = swap(arr, idx, i)
    return None, step


def permuteRec_var2(arr, idx):
    if idx == len(arr) - 1:
        if is_sorted(arr):
            return arr
        return None

    for i in range(idx, len(arr)):
        # Swapping
        arr = swap(arr, idx, i)

        rez = permuteRec_var2(arr, idx + 1)
        if rez:
            return arr

        # Backtrack
        arr = swap(arr, idx, i)
    return None


def sort1(arr, steps):
    return permuteRec(arr, 0, 0, steps)[0]


def sort1_var2(arr):
    return permuteRec_var2(arr, 0)


def sort2(arr, steps):
    k = 0
    n = len(arr)
    gap = n // 2

    while gap > 0:
        j = gap
        while j < n:
            i = j - gap
            while i >= 0:
                if arr[i + gap] > arr[i]:
                    break
                else:
                    arr[i + gap], arr[i] = arr[i], arr[i + gap]
                    k += 1
                    if k % steps == 0:
                        print(f"On step {k}, the list is: {arr}")
                i = i - gap
            j += 1
        gap = gap // 2


def sort2_var2(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        j = gap
        while j < n:
            i = j - gap
            while i >= 0:
                if arr[i + gap] > arr[i]:
                    break
                else:
                    arr[i + gap], arr[i] = arr[i], arr[i + gap]
                i = i - gap
            j += 1
        gap = gap // 2


def sort2_var3(arr):
    n = len(arr)
    k = 0
    gap = 3 * k + 1

    while gap < n:
        j = gap
        while j < n:
            i = j - gap
            while i >= 0:
                if arr[i + gap] > arr[i]:
                    break
                else:
                    arr[i + gap], arr[i] = arr[i], arr[i + gap]
                i = i - gap
            j += 1
        k += 1
        gap = 3 * k + 1


def sort2_var4(arr):
    n = len(arr)
    k = 1
    gap = 1  # 2^k - 1

    while gap < n:
        j = gap
        while j < n:
            i = j - gap
            while i >= 0:
                if arr[i + gap] > arr[i]:
                    break
                else:
                    arr[i + gap], arr[i] = arr[i], arr[i + gap]
                i = i - gap
            j += 1
        k += 1
        gap = 1
        for r in range(k):
            gap = gap * 2
        gap -= 1


option = 0
gen_list = False  # gen_list = checks if the list has been generated
sort_list = False  # sort_list = checks if the list has been sorted
show_steps = True
rndlst = []

while option != 8:
    print()
    print("MENU")
    print("1.Generate a list of random natural numbers.")
    print("2.Search for a number in the list using Binary Search (recursive implementation).")
    print("3.Sort the list using Permutation Sort.")
    print("4.Sort the list using Shell Sort.")
    print("5.Best case complexity.")
    print("6.Worst case complexity.")
    print("7.Average case complexity.")
    print("8.Exit the menu.")
    option = int(input("Please choose from the menu above:"))

    # EXITS the menu
    if option == 8:
        print("You have exited the menu. Bye, bye!")

    # creates a list with random numbers
    if option == 1:
        if (gen_list == True):
            sort_list = False
        else:
            gen_list = True
        n = int(input("Please write the length of the list: "))
        rndlst = random.choices(range(0, 1000), k=n)

        print(f"The list generated is: {rndlst}")

    # searches using binary search rec, the position of a number
    if option == 2:
        if gen_list == True:
            if sort_list == True:
                number_searched = int(input("Please choose the number that you are searching for: "))
                search1(rndlst, number_searched)
            else:
                print("Please sort the list before you search a number.")
        else:
            print(f"You didn't generate a list: {rndlst}")

    # sorts the list using permutation sort
    if option == 3:
        if gen_list == True:
            steps = int(input("Please choose the number of steps you want the list to be printed: "))
            if sort_list == False:
                rndlst = sort1(rndlst, steps)
                sort_list = True
                print(f"The sorted list is:{rndlst}")
            else:
                print("The list has been already sorted.")
        else:
            print(f"You didn't generate a list: {rndlst}")

    # sorts the list using shell sort
    if option == 4:
        if gen_list == True:
            steps = int(input("Please choose the number of steps you want the list to be printed: "))
            if sort_list == False:
                sort2(rndlst, steps)
                sort_list = True
                print(f"The sorted list is:{rndlst}")
            else:
                print("The list has been already sorted.")
        else:
            print(f"You didn't generate a list: {rndlst}")

    # BEST CASE COMPLEXITY
    """ 
    1) Permutation sort
            -> BEST CASE COMPLEXITY: O(n)
            -> It happens when the array is already sorted, because the first permutation will be the 
            sorted array itself. Since only one permutation is checked, the time complexity in this case is O(n). 
    
    2) Shell sort
            -> BEST CASE COMPLEXITY: O(n*log n)
            -> It happens when the array is already sorted, because when the given list is already sorted 
            the total count of comparisons of each interval is equal to the size of the given array.
            
    3) Binary search
            -> BEST CASE COMPLEXITY: O(1)
            -> It happens when the element is at the middle index of the array. It takes only one 
            comparison to find the target element.


    """

    if option == 5:
        # PERMUTATION SORT

        list1 = [i for i in range(1)]
        list2 = [i for i in range(2)]
        list3 = [i for i in range(4)]
        list4 = [i for i in range(8)]
        list5 = [i for i in range(16)]

        t1 = timeit.timeit("sort1_var2(list1)",
                           'from __main__ import sort1_var2, permuteRec_var2, is_sorted, swap, list1',
                           number=4)
        t2 = timeit.timeit("sort1_var2(list2)",
                           'from __main__ import sort1_var2, permuteRec_var2, is_sorted, swap, list2',
                           number=4)
        t3 = timeit.timeit("sort1_var2(list3)",
                           'from __main__ import sort1_var2, permuteRec_var2, is_sorted, swap, list3',
                           number=4)
        t4 = timeit.timeit("sort1_var2(list4)",
                           'from __main__ import sort1_var2, permuteRec_var2, is_sorted, swap, list4',
                           number=4)
        t5 = timeit.timeit("sort1_var2(list5)",
                           'from __main__ import sort1_var2, permuteRec_var2, is_sorted, swap, list5',
                           number=4)

        print("\nPermutation sort --> BEST CASE")
        print(f"List 1: 1 element ---> {t1} ms")
        print(f"List 2: 2 elements ---> {t2} ms")
        print(f"List 3: 4 elements ---> {t3} ms")
        print(f"List 4: 8 elements ---> {t4} ms")
        print(f"List 5: 16 elements ---> {t5} ms")

        # SHELL SORT

        list1 = [i for i in range(100)]
        list2 = [i for i in range(200)]
        list3 = [i for i in range(400)]
        list4 = [i for i in range(800)]
        list5 = [i for i in range(1600)]

        t1 = timeit.timeit("sort2_var4(list1)",
                           'from __main__ import sort2_var4, list1',
                           number=100)
        t2 = timeit.timeit("sort2_var4(list2)",
                           'from __main__ import sort2_var4, list2',
                           number=100)
        t3 = timeit.timeit("sort2_var4(list3)",
                           'from __main__ import sort2_var4, list3',
                           number=100)
        t4 = timeit.timeit("sort2_var4(list4)",
                           'from __main__ import sort2_var4, list4',
                           number=100)
        t5 = timeit.timeit("sort2_var4(list5)",
                           'from __main__ import sort2_var4, list5',
                           number=100)

        print("\nShell sort --> BEST CASE")
        print(f"List 1: 100 elements ---> {t1} ms")
        print(f"List 2: 200 elements ---> {t2} ms")
        print(f"List 3: 400 elements ---> {t3} ms")
        print(f"List 4: 800 elements ---> {t4} ms")
        print(f"List 5: 1600 elements ---> {t5} ms")

        # BINARY SEARCH

        list1 = [i for i in range(100)]
        list2 = [i for i in range(200)]
        list3 = [i for i in range(400)]
        list4 = [i for i in range(800)]
        list5 = [i for i in range(1600)]

        t1 = timeit.timeit("search1_var2(list1, 50)",
                           'from __main__ import search1_var2, binary_search, list1',
                           number=100)
        t2 = timeit.timeit("search1_var2(list2, 100)",
                           'from __main__ import search1_var2, binary_search, list2',
                           number=100)
        t3 = timeit.timeit("search1_var2(list3, 200)",
                           'from __main__ import search1_var2, binary_search, list3',
                           number=100)
        t4 = timeit.timeit("search1_var2(list4, 400)",
                           'from __main__ import search1_var2, binary_search, list4',
                           number=100)
        t5 = timeit.timeit("search1_var2(list5, 800)",
                           'from __main__ import search1_var2, binary_search, list5',
                           number=100)

        print("\nBinary search --> BEST CASE")
        print(f"List 1: 100 elements ---> {t1} ms")
        print(f"List 2: 200 elements ---> {t2} ms")
        print(f"List 3: 400 elements ---> {t3} ms")
        print(f"List 4: 800 elements ---> {t4} ms")
        print(f"List 5: 1600 elements ---> {t5} ms")

    # WORST CASE COMPLEXITY
    """ 
    1) 
            -> It happens when the array is sortPermutation sort
            -> WORST CASE COMPLEXITY: O(n!)ed in reverse. 
            It needs to generate all the permutations to sort it. 

    2) Shell sort
            -> WORST CASE COMPLEXITY:  O(n^2)
            -> It depends on the gap sequence used. The worst case time complexity is O(n^2).

    3) Binary search
            -> WORST CASE COMPLEXITY: O(log n)
            -> The worst case will be when the element is present in the first position. 


    """

    if option == 6:
        # 1) PERMUTATION SORT

        list1 = [i for i in range(1)]
        list2 = [i for i in range(2)]
        list3 = [i for i in range(4)]
        list4 = [i for i in range(8)]
        list5 = [i for i in range(10)]

        list1.reverse()
        list2.reverse()
        list3.reverse()
        list4.reverse()
        list5.reverse()

        t1 = timeit.timeit("sort1_var2(list1)",
                           'from __main__ import sort1_var2, permuteRec_var2, is_sorted, swap, list1',
                           number=4)
        t2 = timeit.timeit("sort1_var2(list2)",
                           'from __main__ import sort1_var2, permuteRec_var2, is_sorted, swap, list2',
                           number=4)
        t3 = timeit.timeit("sort1_var2(list3)",
                           'from __main__ import sort1_var2, permuteRec_var2, is_sorted, swap, list3',
                           number=4)
        t4 = timeit.timeit("sort1_var2(list4)",
                           'from __main__ import sort1_var2, permuteRec_var2, is_sorted, swap, list4',
                           number=4)
        t5 = timeit.timeit("sort1_var2(list5)",
                           'from __main__ import sort1_var2, permuteRec_var2, is_sorted, swap, list5',
                           number=4)

        print("\nPermutation sort --> WORST CASE")
        print(f"List 1: 1 element ---> {t1} ms")
        print(f"List 2: 2 elements ---> {t2} ms")
        print(f"List 3: 4 elements ---> {t3} ms")
        print(f"List 4: 8 elements ---> {t4} ms")
        print(f"List 5: 9 elements ---> {t5} ms")

        # SHELL SORT

        list1 = random.choices(range(0, 1000), k=100)
        list2 = random.choices(range(0, 1000), k=200)
        list3 = random.choices(range(0, 1000), k=400)
        list4 = random.choices(range(0, 1000), k=800)
        list5 = random.choices(range(0, 1000), k=1600)

        t1 = timeit.timeit("sort2_var2(list1)",
                           'from __main__ import sort2_var2, list1',
                           number=100)
        t2 = timeit.timeit("sort2_var2(list2)",
                           'from __main__ import sort2_var2, list2',
                           number=100)
        t3 = timeit.timeit("sort2_var2(list3)",
                           'from __main__ import sort2_var2, list3',
                           number=100)
        t4 = timeit.timeit("sort2_var2(list4)",
                           'from __main__ import sort2_var2, list4',
                           number=100)
        t5 = timeit.timeit("sort2_var2(list5)",
                           'from __main__ import sort2_var2, list5',
                           number=100)

        print("\nShell sort --> WORST CASE")
        print(f"List 1: 100 elements ---> {t1} ms")
        print(f"List 2: 200 elements ---> {t2} ms")
        print(f"List 3: 400 elements ---> {t3} ms")
        print(f"List 4: 800 elements ---> {t4} ms")
        print(f"List 5: 1600 elements ---> {t5} ms")

        # BINARY SEARCH

        list1 = [i for i in range(100)]
        list2 = [i for i in range(200)]
        list3 = [i for i in range(400)]
        list4 = [i for i in range(800)]
        list5 = [i for i in range(1600)]

        t1 = timeit.timeit("search1_var2(list1, 0)",
                           'from __main__ import search1_var2, binary_search, list1',
                           number=100)
        t2 = timeit.timeit("search1_var2(list2, 0)",
                           'from __main__ import search1_var2, binary_search, list2',
                           number=100)
        t3 = timeit.timeit("search1_var2(list3, 0)",
                           'from __main__ import search1_var2, binary_search, list3',
                           number=100)
        t4 = timeit.timeit("search1_var2(list4, 0)",
                           'from __main__ import search1_var2, binary_search, list4',
                           number=100)
        t5 = timeit.timeit("search1_var2(list5, 0)",
                           'from __main__ import search1_var2, binary_search, list5',
                           number=100)

        print("\nBinary search --> WORST CASE")
        print(f"List 1: 100 elements ---> {t1} ms")
        print(f"List 2: 200 elements ---> {t2} ms")
        print(f"List 3: 400 elements ---> {t3} ms")
        print(f"List 4: 800 elements ---> {t4} ms")
        print(f"List 5: 1600 elements ---> {t5} ms")

    # AVERAGE CASE COMPLEXITY
    """ 
    1) Permutation sort
            -> AVERAGE CASE 
            -> In the average case, we assume the sorted permutation will be found halfway through the set of all permutations.

    2) Shell sort
            -> AVERAGE CASE 
            -> The average-case complexity of Shell Sort largely depends on the gap sequence used. 
            The most commonly cited complexities are:
                        - Shell's original sequence:  O(n^2) 
                        - Knuth's sequence: O(n^(3/2))
                        - Sedgewick's sequence: O(n^(4/3))
                        - Tokuda's sequence: O(n^(5/3))
            We will use the Knuth's sequence for the gap in this example.

    3) Binary search
            -> AVERAGE CASE 
            -> There can be two scenarios: 
                        - Required element is present between index 0 to (n-1).
                        - Required element is not present in the given list from index 0 to (n-1).


    """
    if option == 7:
        # 1) PERMUTATION SORT

        list1 = [1]
        list2 = [2, 1]
        list3 = [3, 4, 2, 1]
        list4 = [4, 3, 2, 1, 8, 7, 6, 5]
        list5 = [6, 5, 4, 3, 2, 1, 10, 9, 8, 7]

        t1 = timeit.timeit("sort1_var2(list1)",
                           'from __main__ import sort1_var2, permuteRec_var2, is_sorted, swap, list1',
                           number=4)
        t2 = timeit.timeit("sort1_var2(list2)",
                           'from __main__ import sort1_var2, permuteRec_var2, is_sorted, swap, list2',
                           number=4)
        t3 = timeit.timeit("sort1_var2(list3)",
                           'from __main__ import sort1_var2, permuteRec_var2, is_sorted, swap, list3',
                           number=4)
        t4 = timeit.timeit("sort1_var2(list4)",
                           'from __main__ import sort1_var2, permuteRec_var2, is_sorted, swap, list4',
                           number=4)
        t5 = timeit.timeit("sort1_var2(list5)",
                           'from __main__ import sort1_var2, permuteRec_var2, is_sorted, swap, list5',
                           number=4)

        print("\nPermutation sort --> AVERAGE CASE")
        print(f"List 1: 1 element ---> {t1} ms")
        print(f"List 2: 2 elements ---> {t2} ms")
        print(f"List 3: 4 elements ---> {t3} ms")
        print(f"List 4: 8 elements ---> {t4} ms")
        print(f"List 5: 9 elements ---> {t5} ms")

        # 2) SHELL SORT

        list1 = random.choices(range(0, 1000), k=100)
        list2 = random.choices(range(0, 1000), k=200)
        list3 = random.choices(range(0, 1000), k=400)
        list4 = random.choices(range(0, 1000), k=800)
        list5 = random.choices(range(0, 1000), k=1600)

        t1 = timeit.timeit("sort2_var3(list1)",
                           'from __main__ import sort2_var3, list1',
                           number=100)
        t2 = timeit.timeit("sort2_var3(list2)",
                           'from __main__ import sort2_var3, list2',
                           number=100)
        t3 = timeit.timeit("sort2_var3(list3)",
                           'from __main__ import sort2_var3, list3',
                           number=100)
        t4 = timeit.timeit("sort2_var3(list4)",
                           'from __main__ import sort2_var3, list4',
                           number=100)
        t5 = timeit.timeit("sort2_var3(list5)",
                           'from __main__ import sort2_var3, list5',
                           number=100)

        print("\nShell sort --> AVERAGE CASE")
        print(f"List 1: 100 element ---> {t1} ms")
        print(f"List 2: 200 elements ---> {t2} ms")
        print(f"List 3: 400 elements ---> {t3} ms")
        print(f"List 4: 800 elements ---> {t4} ms")
        print(f"List 5: 1600 elements ---> {t5} ms")

        # BINARY SEARCH

        list1 = [i for i in range(100)]
        list2 = [i for i in range(200)]
        list3 = [i for i in range(400)]
        list4 = [i for i in range(800)]
        list5 = [i for i in range(1600)]

        t1 = timeit.timeit("search1_var2(list1, 70)",
                           'from __main__ import search1_var2, binary_search, list1',
                           number=100)
        t2 = timeit.timeit("search1_var2(list2, 70)",
                           'from __main__ import search1_var2, binary_search, list2',
                           number=100)
        t3 = timeit.timeit("search1_var2(list3, 70)",
                           'from __main__ import search1_var2, binary_search, list3',
                           number=100)
        t4 = timeit.timeit("search1_var2(list4, 70)",
                           'from __main__ import search1_var2, binary_search, list4',
                           number=100)
        t5 = timeit.timeit("search1_var2(list5, 70)",
                           'from __main__ import search1_var2, binary_search, list5',
                           number=100)

        print("\nBinary search --> AVERAGE CASE - the number is in the list")
        print(f"List 1: 100 elements ---> {t1} ms")
        print(f"List 2: 200 elements ---> {t2} ms")
        print(f"List 3: 400 elements ---> {t3} ms")
        print(f"List 4: 800 elements ---> {t4} ms")
        print(f"List 5: 1600 elements ---> {t5} ms")

        list1 = [i for i in range(100)]
        list2 = [i for i in range(200)]
        list3 = [i for i in range(400)]
        list4 = [i for i in range(800)]
        list5 = [i for i in range(1600)]

        t1 = timeit.timeit("search1_var2(list1, 999999999)",
                           'from __main__ import search1_var2, binary_search, list1',
                           number=100)
        t2 = timeit.timeit("search1_var2(list2, 999999999)",
                           'from __main__ import search1_var2, binary_search, list2',
                           number=100)
        t3 = timeit.timeit("search1_var2(list3, 999999999)",
                           'from __main__ import search1_var2, binary_search, list3',
                           number=100)
        t4 = timeit.timeit("search1_var2(list4, 999999999)",
                           'from __main__ import search1_var2, binary_search, list4',
                           number=100)
        t5 = timeit.timeit("search1_var2(list5, 999999999)",
                           'from __main__ import search1_var2, binary_search, list5',
                           number=100)

        print("\nBinary search --> AVERAGE CASE - the number is not the list")
        print(f"List 1: 100 elements ---> {t1} ms")
        print(f"List 2: 200 elements ---> {t2} ms")
        print(f"List 3: 400 elements ---> {t3} ms")
        print(f"List 4: 800 elements ---> {t4} ms")
        print(f"List 5: 1600 elements ---> {t5} ms")

else:
    print("Please choose an option from the menu.")
