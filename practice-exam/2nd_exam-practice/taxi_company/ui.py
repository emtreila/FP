from pprint import pprint

from taxi_company.address import Address
from taxi_company.service import Service


class UI(Service):
    def __init__(self, service: Service):
        super().__init__()
        self._service = service

    def main(self):
        while True:
            print("\n1. Add address")
            print("2. Display all addresses")
            print("3. Distance between given position")
            print("4. New taxi station")
            print("5. Exit")

            option = input("Enter option: ")

            try:
                option = int(option)
            except:
                print("Invalid option!")
            if not (1 <= option <= 5):
                print("Invalid option!")

            if option == 5:
                exit()

            elif option == 1:

                while True:
                    name = input("Name: ")
                    try:
                        self._service.handle_name(name)
                    except Exception as e:
                        print(e)
                        continue
                    break
                while True:
                    number = input("Number: ")
                    try:
                        number = int(number)
                    except:
                        print("Invalid number!")
                        continue

                    try:
                        self._service.handle_number(number)
                    except Exception as e:
                        print(e)
                        continue
                    break
                while True:
                    x = input("x= ")
                    try:
                        x = int(x)
                    except:
                        print("Invalid number!")
                        continue

                    try:
                        self._service.handle_x(x)
                    except Exception as e:
                        print(e)
                        continue
                    break

                while True:
                    y = input("y= ")
                    try:
                        y = int(y)
                    except:
                        print("Invalid number!")
                        continue

                    try:
                        self._service.handle_y(y)
                    except Exception as e:
                        print(e)
                        continue
                    break
                address = Address(name, number, x, y)
                self._service.add_address(address)

            elif option == 2:

                print("\nADDRESSES")
                pprint(self._service.get_all_addresses())

            elif option == 3:
                d = input("Distance d: ")
                from_x = input("x= ")
                from_y = input("y= ")

                try:
                    d = int(d)
                    from_x = int(from_x)
                    from_y = int(from_y)
                except:
                    print("Invalid number!")
                    continue
                addresses = self.get_all_addresses().values()
                for address in addresses:
                    distance = self._service.calculate_distance(from_x, address.x, from_y, address.y)
                    if distance <= d:
                        print(address, f"Distance: {distance}")

            elif option == 4:

                addresses = self._service.get_all_addresses().values()
                min_distance = 10000000000000000000000

                min_x = 0
                min_y = 0
                for x in range(-100, 101):
                    for y in range(-100, 101):
                        sum_ = 0
                        if self._service.check_coordinates(x,y):
                            continue
                        else:
                            for address in addresses:
                                distance = self._service.calculate_distance(x, address.x, y, address.y)
                                sum_ = sum_ + distance

                            if sum_ < min_distance:
                                min_distance = sum_
                                min_x = x
                                min_y = y

                print(f"\nNEW TAXI: x={min_x}, y={min_y}, distance={min_distance}")
