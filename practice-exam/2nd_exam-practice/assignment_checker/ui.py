from pprint import pprint

from assignment_checker.service import Service


class UI:
    def __init__(self, service: Service = Service):
        super().__init__()
        self._service = service

    def main(self):
        while True:
            print("1. Add assignment")
            print("2. Display assignments")
            print("3. Dishonesty check")
            print("4. Exit")

            option = input("Enter option: ")
            try:
                option = int(option)
            except ValueError:
                print("Invalid option!")
                continue

            if not(1 <= option <= 5):
                print("Invalid option!")
                continue

            if option == 5:
                exit()

            elif option == 1:
                while True:
                    name = input("Enter name: ")
                    solution = input("Enter solution: ")

                    if not solution:
                        print("Invalid solution!")
                        continue

                    if len(name)<3:
                        print("Invalid name!")
                        continue
    
                    self._service.add_assignment(name, solution)
                    break

            elif option == 2:
                assignments = sorted(self._service.get_all_assignments().values(), key = lambda x: x.student_id)
                print("Assignments:")
                pprint(assignments)

            elif option == 3:
                result = self._service.dishonesty_check()
                print("Dishonesty check:")
                pprint(result)
