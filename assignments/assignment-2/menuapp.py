# binary rec search/ permutation sort/ shell sort
import random


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



def sort1(arr, steps):
    i = 0
    while not sorted(arr) == arr:
        random.shuffle(arr)
        i += 1
        if i % steps == 0:
            print(f"On step {i}, the list is: {arr}")


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


option = 0
gen_list = False  # gen_list = checks if the list has been generated
sort_list = False  # sort_list = checks if the list has been sorted
rndlst = []

while option != 5:
    print()
    print("MENU")
    print("1.Generate a list of random natural numbers.")
    print("2.Search for a number in the list using Binary Search (recursive implementation).")
    print("3.Sort the list using Permutation Sort.")
    print("4.Sort the list using Shell Sort.")
    print("5.Exit the menu.")
    option = int(input("Please choose from the menu above:"))


    if option == 5:
        print("You have exited the menu. Bye, bye!")


    if option == 1:
        if(gen_list == True):
            sort_list=False
        else:
            gen_list = True
        n = int(input("Please write the length of the list: "))
        rndlst = random.choices(range(0, 1000), k=n)

        print(f"The list generated is: {rndlst}")


    if option == 2:
        if gen_list == True:
            if sort_list == True:
                number_searched = int(input("Please choose the number that you are searching for: "))
                search1(rndlst, number_searched)
            else:
                print("Please sort the list before you search a number.")
        else:
            print(f"You didn't generate a list: {rndlst}")


    if option == 3:
        if gen_list == True:
            steps = int(input("Please choose the number of steps you want the list to be printed: "))
            if sort_list == False:
                sort1(rndlst, steps)
                sort_list = True
                print(f"The sorted list is:{rndlst}")
            else:
                print("The list has been already sorted.")
        else:
            print(f"You didn't generate a list: {rndlst}")


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


    else:
        print("Please choose an option from the menu.")
