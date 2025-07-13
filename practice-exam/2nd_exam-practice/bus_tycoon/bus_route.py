class BusRoute:
    def __init__(self, route_code, length ):
        self._route_code = route_code
        self._length = length

    @property
    def route_code(self):
        return self._route_code

    @route_code.setter
    def route_code(self, new):
        self._route_code = new

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, new):
        self._length = new

    def __str__(self):
        return f"(Route code: {self._route_code}, Length: {self._length} km)"

    def __repr__(self):
        return self.__str__()
