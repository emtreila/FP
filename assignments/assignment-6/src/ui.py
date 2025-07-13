#
# This is the program's UI module. The user interface and all interaction with the user (print and input statements) are found here
#
import random
import texttable

import functions


def handle_help():
    print("COMMANDS\n")
    print("1) Add the result of a new participant. Commands:")
    print("\t- add <P1 score> <P2 score> <P3 score>")
    print("\t- insert <P1 score> <P2 score> <P3 score> at <position>")
    print("2) Modify scores. Commands:")
    print("\t- remove <position>")
    print("\t- remove <start position> to <end position>")
    print("\t- replace <old score> <P1 | P2 | P3> with <new score>")
    print("3) Display participants whose score has different properties. Commands:")
    print("\t- list")
    print("\t- list sorted")
    print("\t- list [ < | = | > ] <score>")
    print("4) Establish the podium")
    print("\t- top <number>")
    print("\t- top <number> <P1 | P2 | P3>")
    print("\t- remove [ < | = | > ] <score>")
    print("5) Undo ")
    print("\t- undo ")
    print("6) Exit ")
    print("\t- exit ")


def handle_add(command: list[str], scores: list, undo_scores: list):
    if len(command) != 4:
        raise ValueError("The command is incorrect.")

    p1 = command[1]
    p2 = command[2]
    p3 = command[3]

    try:
        p1 = int(p1)
        p2 = int(p2)
        p3 = int(p3)
    except:
        raise ValueError("The parameters must be integers.")

    errors = ""
    if not (0 <= p1 <= 10):
        errors += f"The value {p1} cannot be used to grade a problem."
    if not (0 <= p2 <= 10):
        errors += f"The value {p2} cannot be used to grade a problem."
    if not (0 <= p3 <= 10):
        errors += f"The value {p3} cannot be used to grade a problem."

    if errors:
        raise Exception(errors)

    undo_scores.append(scores[:])
    functions.add(p1, p2, p3, scores)


def handle_insert(command: list[str], scores: list, undo_scores: list):
    if len(command) != 6:
        raise ValueError("The command is incorrect.")

    p1 = command[1]
    p2 = command[2]
    p3 = command[3]
    position = command[5]

    try:
        p1 = int(p1)
        p2 = int(p2)
        p3 = int(p3)
        position = int(position)
    except:
        raise ValueError("The parameters must be integers.")

    errors = ""
    if not (0 <= p1 <= 10):
        raise ValueError(f"The value {p1} cannot be used to grade a problem.")
    if not (0 <= p2 <= 10):
        raise ValueError(f"The value {p2} cannot be used to grade a problem.")
    if not (0 <= p3 <= 10):
        raise ValueError(f"The value {p3} cannot be used to grade a problem.")
    if not (position >= 0):
        raise ValueError(f"The position must be >= 0")

    if errors:
        raise ValueError(errors)

    if command[4] != "at":
        raise SyntaxError("The command is incorrect.")

    undo_scores.append(scores[:])
    functions.insert1(p1, p2, p3, scores, position)


def handle_remove(command: list[str], scores: list, undo_scores: list):
    if len(command) != 2 and len(command) != 3 and len(command) != 4:
        raise ValueError("The command is incorrect.")

    if len(command) == 2:
        position = command[1]
        try:
            position = int(position)
        except:
            raise ValueError("The parameters must be integers.")

        if not (0 <= position < len(scores)):
            raise ValueError("The position is not in the list of grades.")

        undo_scores.append(scores[:])
        functions.remove1(scores, position)

    elif len(command) == 3:
        x = command[2]
        try:
            x = int(x)
        except:
            raise ValueError("The parameter must be integer.")
        sign = command[1]
        if not (sign in [">", "=", "<"]):
            raise SyntaxError("The command is incorrect.")

        undo_scores.append(scores[:])
        functions.remove3(scores, sign, x)


    elif len(command) == 4:
        start = command[1]
        end = command[3]
        try:
            start = int(start)
            end = int(end)
        except:
            raise ValueError("The parameters must be integers.")
        if not (0 <= start <= end < len(scores)):
            raise ValueError("The interval is not valid. ")

        if command[2] != "to":
            raise SyntaxError("The command is incorrect.")

        undo_scores.append(scores[:])
        functions.remove2(scores, start, end)


def handle_replace(command: list[str], scores: list, undo_scores: list):
    if len(command) != 5:
        raise ValueError("The program is incorrect.")
    old = command[1]
    p = command[2]
    new = command[4]
    try:
        old = int(old)
        new = int(new)
    except:
        raise ValueError("The parameters must be integers.")

    if not (p in ["P1", "P2", "P3"]):
        raise ValueError("The command is incorrect.")

    if not (0 <= old < len(scores)):
        raise ValueError("The participant position is not correct!")

    if command[3] != "with":
        raise SyntaxError("The command is incorrect.")
    index = ["P1", "P2", "P3"].index(p)

    undo_scores.append(scores[:])
    functions.replace(scores, old, index, new)


def handle_list(command: list[str], scores: list):
    if len(command) > 3:
        raise ValueError("The command is incorrect.")

    new_scores = scores
    if len(command) == 1:
        new_scores = functions.list1(scores)

    elif len(command) == 2:
        if command[1] != "sorted":
            raise SyntaxError("The command is incorrect.")
        new_scores = functions.list2(scores)

    elif len(command) == 3:
        score = command[2]
        try:
            score = int(score)
        except:
            raise ValueError("The parameter must be integer.")

        if not (command[1] in ["<", "=", ">"]):
            raise SyntaxError("The command is incorrect.")

        new_scores = functions.list3(scores, command[1], score)

    # Create texttable object
    tableObj = texttable.Texttable()

    # Set columns
    tableObj.set_cols_align(["c", "c", "c"])

    # Set datatype of each column
    tableObj.set_cols_dtype(["i", "i", "i"])

    # Adjust columns
    tableObj.set_cols_valign(["m", "m", "m"])

    # Insert rows
    tableObj.add_rows([
        ["P1", "P2", "P3"],
    ])

    for x in new_scores:
        tableObj.add_row(x)

    # Display table
    print(tableObj.draw())


def handle_top(command: list[str], scores: list):
    if len(command) != 2 and len(command) != 3:
        raise ValueError("The command is incorrect.")

    new_scores = scores
    if len(command) == 2:
        number = command[1]
        try:
            number = int(number)
        except:
            raise ValueError("The parameters must be integers.")
        if number >= len(scores):
            raise ValueError("There aren't that many participants.")

        new_scores = functions.top1(scores, number)

    elif len(command) == 3:
        number = command[1]
        try:
            number = int(number)
        except:
            raise ValueError("The parameters must be integers.")
        if number >= len(scores):
            raise ValueError("There aren't that many participants.")
        p = command[2]
        if not (p in ["P1", "P2", "P3"]):
            raise SyntaxError("The command is incorrect.")
        index = ["P1", "P2", "P3"].index(p)

        new_scores = functions.top2(scores, number, index)

    # Create texttable object
    tableObj = texttable.Texttable()

    # Set columns
    tableObj.set_cols_align(["c", "c", "c"])

    # Set datatype of each column
    tableObj.set_cols_dtype(["i", "i", "i"])

    # Adjust columns
    tableObj.set_cols_valign(["m", "m", "m"])

    # Insert rows
    tableObj.add_rows([
        ["P1", "P2", "P3"],
    ])

    for x in new_scores:
        tableObj.add_row(x)

    # Display table
    print(tableObj.draw())


def handle_undo(command: list[str], undo_scores: list):
    if len(command) != 1:
        raise ValueError("The command is incorrect.")

    if not undo_scores:
        raise Exception("No more undos!")

    return functions.undo(undo_scores)


def handle_exit():
    print("You've exited the program. Bye, bye!")
    exit()


def main():
    scores = []
    undo_scores = []
    for i in range(10):
        current = [
            random.randint(0, 10),
            random.randint(0, 10),
            random.randint(0, 10)
        ]
        scores.append(current)

    # Dictionary containing the commands
    # Entry: command: method_for_command
    commands = {
        "add": handle_add,
        "insert": handle_insert,
        "remove": handle_remove,
        "replace": handle_replace,
        "list": handle_list,
        "top": handle_top,
        "undo": handle_undo,
    }
    handle_help()
    while True:

        command = input("Enter the command: ").strip()
        # no command provided
        if not command:
            print("No command given!")
            continue
        if command == "help":
            handle_help()
            continue
        if command == "exit":
            handle_exit()

        # Split the command by whitespaces
        arguments = command.split()
        command_name = arguments[0].strip()

        handle_for_command = commands.get(command_name)

        # Command not accepted
        if not handle_for_command:
            print(f"Command {command_name} is not accepted!")
            continue

        # Handle the command
        try:
            if command_name in ["add", "insert", "remove", "replace"]:
                handle_for_command(arguments, scores, undo_scores)
            elif command_name == "undo":
                scores = handle_for_command(arguments, undo_scores)
            else:
                handle_for_command(arguments, scores)
        except Exception as error:
            print(error)
