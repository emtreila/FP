from pprint import pprint

from taxi_simulator.services import Service


class UI:
    def __init__(self, services: Service):
        self._services = services

    def main(self):

        while True:
            nr_of_taxis = input("Enter the number of operational taxis (between 0-10): ")
            try:
                nr_of_taxis = int(nr_of_taxis)
            except:
                "Invalid number!"
                continue
            if nr_of_taxis == 0:
                print("No taxis available!")
                continue
            elif not (0 < nr_of_taxis <= 10):
                print("Invalid number!")
                continue

            self._services.generate_taxis(nr_of_taxis)
            print("\nOPERATIONAL TAXIS:\n")
            pprint(self._services.list_taxis())

            while True:
                print("\n")
                print("1) Add a ride.")
                print("2) Simulate a ride.")
                print("3) Exit.")
                option = input("Please choose an option:")

                try:
                    option = int(option)
                except:
                    "Invalid option!"
                    continue
                if not (1 <= option <= 3):
                    print("Invalid option!")
                    continue
                elif not option:
                    print("Invalid option!")
                    continue

                if option == 1:
                    print("Entry coordinates for the starting point:")
                    start_x = input("x = ")
                    start_y = input("y = ")
                    print("Entry coordinates for the ending point:")
                    end_x = input("x = ")
                    end_y = input("y = ")

                    try:
                        start_x = int(start_x)
                        start_y = int(start_y)
                        end_x = int(end_x)
                        end_y = int(end_y)
                    except:
                        print("Invalid coordinates!")
                        return

                    if not (start_x and start_y and end_x and end_y):
                        print("Invalid coordinates!")
                        return
                    elif not (0 <= start_x <= 100 and 0 <= start_y <= 100 and 0 <= end_x <= 100 and 0 <= end_y <= 100):
                        print("Invalid coordinates!")
                        return

                    self._services.add_ride(start_x, start_y, end_x, end_y, nr_of_taxis)
                    sorted_taxis = sorted(self._services.list_taxis(), key=lambda x: x.fare, reverse=True)
                    print("\nTAXIS\n")
                    pprint(sorted_taxis)

                elif option == 2:

                    start_x, start_y, end_x, end_y = self._services.generate_ride(nr_of_taxis)
                    print("Ride generated:")
                    print(f"({start_x},{start_y}) --> ({end_x},{end_y})")
                    sorted_taxis = sorted(self._services.list_taxis(), key=lambda x: x.fare, reverse=True)
                    print("\nTAXIS\n")
                    pprint(sorted_taxis)

                elif option == 3:
                    exit()
