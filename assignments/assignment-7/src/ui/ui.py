from src.services.services import Services
from pprint import pprint

class UI:
    def __init__(self, services=Services):
        self._services = services

    def main(self):

        print("MENU")
        print("1) Add an expense.")
        print("2) Display the list of expenses.")
        print("3) Filter the list so that it contains only expenses above a certain value.")
        print("4) Undo the last operation that modified program data.")
        while True:
            option = input("Please choose an option: ")

            if not option:
                print("No option given!")
                continue

            try:
                option = int(option)
            except:
                print("The option must be a number.")
                continue

            if not (1 <= option <= 4):
                print("No valid option!")
                continue

            if option == 1:
                day = input("Day: ")
                amount = input("Amount: ")
                type = input("Type: ")

                try:
                    day = int(day)
                    amount = int(amount)
                except:
                    print("The option must be a number.")
                    continue

                try:
                    self._services.add(day,amount,type)
                except Exception as error:
                    print(error)

            if option == 2:
                print("\nExpenses\n")
                pprint(self._services.display())

            if option == 3:
                filteramount = input("Amount for filtered list: ")
                try:
                    filteramount = int(filteramount)
                except:
                    print("The option must be a number.")
                    continue

                pprint(self._services.filter(filteramount))

            if option == 4:

                try:
                    self._services.undo()
                except Exception as error:
                    print(error)