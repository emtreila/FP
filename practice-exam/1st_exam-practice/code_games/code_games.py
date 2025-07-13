import random


#
# Functions section
#

def random_number():
    digits_with_0 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    digits_without_0 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    nr_list= []
    digit = random.choice(digits_without_0)
    nr_list.append(digit)
    nr = digit

    digits_with_0.remove(nr_list[0])
    for i in range(1, 4):
        digit = random.choice(digits_with_0)
        nr_list.append(digit)
        nr = nr*10 + digit
        digits_with_0.remove(nr_list[i])

    return nr_list,nr


def list_of_user_number(nr):
    i = 3
    list_user = [0] * 4
    while nr != 0:
        list_user[i] = nr % 10
        nr = nr // 10
        i -= 1
    return list_user


def conditions(list_user) -> bool:
    if list_user[0] == 0:
        return False
    if not (list_user[0] != list_user[1] != list_user[2] != list_user[3]):
        return False
    return True

def codes_runners(list_user,list_nr):
    c=0
    r=0
    for i in range(len(list_nr)):
        for j in range(len(list_user)):
            if list_nr[i] == list_user[j]:
                if i == j:
                    c +=1
                else:
                    r +=1
    return c,r



#
# User interface section
#

def handle_user_number(nr):
    pass


def main():
    list_nr , nr = random_number()
    print(list_nr)


    game_over = False
    while not game_over:
        user_input = input("Enter the number:").strip()

        list_user = [0] * 4

        try:
            user_input = int(user_input)
        except:
            print("You must enter an integer. GAME OVER!")
            return

        if user_input < 0:
            print("The number must be positive.  GAME OVER!")
            return

        if user_input == 8086:
            print(f"The number selected must be {nr}")

        if not (1000 <= user_input <= 9999):
            print("The number must have 4 digits.  GAME OVER!")
            return

        list_user = list_of_user_number(user_input)

        if not conditions(list_user):
            print("The number isnt correct.  GAME OVER!")
            return

        if user_input == nr:
            print("GAME WON!")
            return

        codes, runners = codes_runners(list_user, list_nr)
        print(f"{user_input}: {codes} codes , {runners} runners")


main()
