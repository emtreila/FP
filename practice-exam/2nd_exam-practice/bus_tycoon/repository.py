from bus_tycoon.bus import Bus
from bus_tycoon.bus_route import BusRoute


class TextFileRepoBus:
    def __init__(self, file_name: str = "buses.txt"):
        self._bus_data: dict[int, Bus] = {}
        self._last_id = 0
        self._file_name = file_name
        self.__read_from_file()

    def __read_from_file(self):
        """
        Reads from file all the buses
        """
        with open(self._file_name, "r") as f:
            for line in f.readlines():
                attributes = line.strip().split(",")
                if len(attributes) != 4:
                    continue

                bus_id = int(attributes[0])
                route_code = int(attributes[1])
                model = str(attributes[2])
                times_used = int(attributes[3])

                bus = Bus(route_code, model, times_used)
                bus.bus_id = bus_id

                self._last_id = bus_id + 1
                self._bus_data[bus_id] = bus

    def get_bus_by_id(self, id_):
        """
        :param id_: the id for the bus
        :return: the bus with the given id
        """
        return self._bus_data[id_]

    def get_all_buses(self):
        """
        :return: a list with all the buses
        """
        return list(self._bus_data.values())


class TextFileRepoRoute:
    def __init__(self, file_name: str = "bus_routes.txt"):
        self._route_data: list[BusRoute] = []
        self._last_id = 0
        self._file_name = file_name
        self.__read_from_file()

    def __read_from_file(self):
        """
        Reads from file all the bus routes
        """
        with open(self._file_name, "r") as f:
            for line in f.readlines():
                attributes = line.strip().split(",")
                if len(attributes) != 2:
                    continue

                route_code = int(attributes[0])
                length = int(attributes[1])

                bus_route = BusRoute(route_code, length)
                self._route_data.append(bus_route)

    def get_all_routes(self):
        """
        :return: a list with all the buses
        """
        return self._route_data

    def get_route_length(self, given_route):
        """
        Get route length
        :param given_route: the code for the route
        :return: the route length
        """
        for route in self._route_data:
            if route.route_code == given_route:
                return route.length
        return None

