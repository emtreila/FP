from pprint import pprint

from bus_tycoon.services import Service


class UI:
    def __init__(self, service: Service):
        self._service = service

    def main(self):
        while True:
            print("\n1. Busses across certain route")
            print("2. Km travelled by a bus")
            print("3. Total mileage on a route")
            print("4. Exit\n")

            option = int(input("Enter option: "))

            if option == 4:
                exit()

            elif option == 1:
                route = int(input("Enter route: "))
                print(f"\nBuses on route {route}:")
                pprint(self._service.busses_across_certain_route(route))

            elif option == 2:
                bus_id = int(input("Enter bus id: "))
                print(f"\nKm travelled by bus {bus_id}: {self._service.km_travelled(bus_id)}")
                print(self._service.get_bus_by_id(bus_id))

            elif option == 3:
                route_mileage = self._service.total_mileage()
                sorted_routes = sorted(route_mileage.items(), key=lambda x: x[1][0], reverse=True)
                print("\nTotal mileage on each route:")
                for route_code, (total_mileage, assigned_buses) in sorted_routes:
                    print(f"Route {route_code}: Total mileage = {total_mileage}")
                    for bus in assigned_buses:
                        print(f"    Bus {bus.bus_id}: {bus.model}, {bus.times_used} times used")


