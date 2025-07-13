#
# Functions section
#

def add(code,name,type,species):
    return [code,name,type,species]

def check_code(zoo,code)->bool:
    for i in range(len(zoo)):
        if zoo[i][0] == code:
            return False
    return True

def modify(zoo,code,type):
    for i in range(len(zoo)):
        if zoo[i][0] == code:
            zoo[i][2] = type
    return zoo

def sort_type(zoo,type):
    type_list =[]
    for i in range(len(zoo)):
        if zoo[i][2] == type:
            type_list.append(zoo[i])
    type_list.sort(key=lambda x: x[2])
    return type_list

def change_all(zoo,species,new_type):

    for i in range(len(zoo)):
        if zoo[i][3] == species:
            zoo[i][2] = new_type
    return zoo

def check_species(zoo,species):
    for i in range(len(zoo)):
        if zoo[i][3] == species:
            return True
    return False
#
# User interface section
#

def main():

    print("MENU")
    print("1) Add an animal ( code, name, type, species )")
    print("2) Modify type ( code , type )")
    print("3) Modify species and new type ( species, type )")
    print("4) Show all animals with a type ( type )")

    zoo = [
        ["Z01", "mimi", "herbivore", "zebra"],
        ["L01", "ana", "carnivore", "lion"],
        ["E01", "moana", "herbivore", "elephant"],
        ["T01", "albert", "carnivore", "tiger"],
        ["M01", "lola", "herbivore", "monkey"]
    ]

    while True:

        command =input("Please enter your choice:")

        try:
            command = int(command)
        except:
            print("give a number")
            continue

        if not (1<= command <=5):
            print("command incorrect")
            continue

        if command == 1:
            code = input("code:").strip()
            name = input("name:").strip()
            type = input("type:").strip()
            species = input("species:").strip()

            if not ( code or name or type or species):
                print("invalid parameters")
                continue

            is_ok =check_code(zoo,code)
            if not is_ok:
                print("code already used")
                continue

            zoo.append(add(code,name,type,species))


        if command == 2:

            code = input("code:").strip()
            type = input("type:").strip()

            is_ok = check_code(zoo,code)
            if is_ok:
                print("invalid code")
                continue
            zoo = modify(zoo,code,type)

        if command == 3:
            species = input("species:")
            new_type = input(("new type:"))
            if not ( new_type or species):
                print("invalid parameters")
                continue
            is_ok = check_species(zoo, species)
            if not is_ok:
                print("no such species at zoo")
                continue

            zoo = change_all(zoo,species,new_type)

        if command == 4:
            type = input("type:").strip()
            new = sort_type(zoo,type)
            print(new)

        if command == 5:
            print(zoo)




main()