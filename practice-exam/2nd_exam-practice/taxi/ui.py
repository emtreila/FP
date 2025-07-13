from pprint import pprint

from taxi.service import Service


class UI:
    def __init__(self, service: Service = Service):
        super().__init__()
        self._service = service

    def main(self):
        while True:
            print("\n1. Add a new order.")
            print("2. Display all driver and order information. ")
            print("3. Total income. ")
            print("4. Exit\n")

            option = input("Choose an option: ")
            if not option:
                print("Invalid option!")
                continue

            try:
                option = int(option)
            except ValueError:
                print("Invalid option!")
                continue

            if not(1 <= option <= 4):
                print("Invalid option!")
                continue

            if option == 4:
                exit()

            elif option == 1:
                driver_id = input("Enter the driver id: ")
                km = input("Enter the distance in km: ")
                try:
                    driver_id = int(driver_id)
                    km = int(km)
                except ValueError:
                    print("Invalid input!")
                    continue

                if not(km >= 1):
                    print("Invalid km!")
                    continue

                drivers = self._service.get_all_drivers().values()
                k = 0
                for driver in drivers:
                    if driver.driver_id == driver_id:
                        k = 1

                if k == 0:
                    print("Invalid id!")
                    continue

                self._service.add_order(driver_id, km)
                print("Order added!")

            elif option == 2:
                drivers = self._service.get_all_drivers()
                orders = self._service.get_all_orders()
                print("DRIVERS")
                pprint(drivers)
                print("\nORDERS")
                pprint(orders)

            elif option == 3:
                driver_id = input("Id of the driver: ")
                try:
                    driver_id = int(driver_id)
                except ValueError:
                    print("Invalid input!")
                    continue

                check_drivers = self._service.get_all_drivers().values()
                k = 0
                for driver in check_drivers:
                    if driver.driver_id == driver_id:
                        k = 1

                if k == 0:
                    print("Invalid id!")
                    continue

                total_income = self._service.calculate_income(driver_id)
                driver = self._service.get_driver_by_id(driver_id)
                print(driver)
                print(f"Total income: {total_income}")