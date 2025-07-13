#
# Functions section
#


def create_product(name, p1, p2):
    return [name, p1, p2]


def add(products, name, p1, p2):
    products.append(create_product(name, p1, p2))


def remove(products, name):
    for i in range(len(products)):
        if products[i][0] == name:
            products.pop(i)
            break


def list(products: list):
    return sorted(products, key=lambda x: x[0], reverse=True)


def total(products):
    s = 0
    for i in range(len(products)):
        s = s + products[1] * products[2]
    return s


#
# User interface section
#
def handle_add(command: list, products: list):
    if len(command) != 4:
        raise ValueError("The command is incorrect.")

    name = command[1].strip()
    p1 = command[2]
    p2 = command[3]

    try:
        p1 = int(p1)
        p2 = int(p2)
    except:
        raise ValueError("The parameters must be integers.")

    if not (p1 >= 0 and p2 >= 0):
        raise ValueError("The integers must be positive.")

    add(products, name, p1, p2)


def handle_remove(command, products):
    if len(command) != 2:
        raise ValueError("The command is incorrect.")
    name = command[1].strip()
    k = 0
    for i in range(len(products)):
        if products[i][0] == name:
            k = 1
            break
    if k == 0:
        raise SyntaxError(f"No product {name} in the list")
    else:
        remove(products, name)


def handle_list(command, products):
    if len(command) != 2:
        raise ValueError("The command is incorrect.")
    arg = command[1]
    if arg == "all":
        sorted_products = list(products)
        print(sorted_products)
    elif arg == "total":
        total_value = total(products)
        print(f"The total value is {total_value}.")


def handle_exit():
    print("You've exited the program. Bye, bye!")
    exit()


def handle_help():
    print("COMMANDS")
    print("1)Add a product:")
    print(" - add <product_name> <quantity> <item_price>")
    print("2)Remove a product:")
    print(" - remove <product_name>")
    print("3)List all the products:")
    print(" - list all")
    print("4)Total value of the products in the warehouse:")
    print(" - list total")
    print("5)Exit")
    print(" - exit")


def main():
    commands = {
        "add": handle_add,
        "remove": handle_remove,
        "list": handle_list
    }

    products = [
        ["mela", 4, 5], ["aelx", 3, 5], ["dnadi", 3, 3]
    ]

    handle_help()
    while True:
        command = input("Enter the command:").strip()
        if not command:
            print("No command given!")
            continue
        if command == "help":
            handle_help()
            continue
        if command == "exit":
            handle_exit()
            continue

        arguments = command.split()
        command_name = arguments[0].strip()

        handle_for_command = commands.get(command_name)

        if not handle_for_command:
            print(f"Command {handle_for_command} not accepted!")

        try:
            handle_for_command(arguments, products)
        except Exception as error:
            print(error)


main()
