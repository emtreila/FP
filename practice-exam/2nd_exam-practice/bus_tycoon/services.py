from bus_tycoon.repository import TextFileRepoBus, TextFileRepoRoute


class Service:
    def __init__(self, bus_repo: TextFileRepoBus = TextFileRepoBus, route_repo: TextFileRepoRoute = TextFileRepoRoute):
        self._bus_repo = bus_repo
        self._route_repo = route_repo

    def busses_across_certain_route(self, given_route):
        """
        :param given_route: the route the buses are on
        :return: list with all the buses that are on that route
        """
        buses_route = []
        for bus in self._bus_repo.get_all_buses():
            if bus.route_code == given_route:
                buses_route.append(bus)

        return buses_route

    def km_travelled(self, id_):
        """
        Compute how many km the bus travelled on that route
        :param id_: the bus id
        :return: the km travelled
        """
        print(self._route_repo.get_all_routes())
        bus = self._bus_repo.get_bus_by_id(id_)
        if bus is None:
            raise ValueError(f"Bus with ID {id_} not found.")

        route_length = self._route_repo.get_route_length(bus.route_code)
        if route_length is None:
            raise ValueError(f"Route length for route {bus.route_code} not found.")

        return bus.times_used * route_length

    def total_mileage(self):
        """"
        :return: the total mileage done
        """
        route_mileage = {}
        for route in self._route_repo.get_all_routes():
            total_mileage = 0
            assigned_buses = []
            for bus in self._bus_repo.get_all_buses():
                if bus.route_code == route.route_code:
                    assigned_buses.append(bus)
            for bus in assigned_buses:
                total_mileage = total_mileage + bus.times_used * route.length
            route_mileage[route.route_code] = (total_mileage, assigned_buses)
        return route_mileage


    def get_bus_by_id(self, id_):
        """
        :param id_: the id for the bus
        :return: the bus with the given id
        """
        return self._bus_repo.get_bus_by_id(id_)
