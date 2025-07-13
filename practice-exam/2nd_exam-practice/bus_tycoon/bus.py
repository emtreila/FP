class Bus:

    def __init__(self, route_code, model, times_used, bus_id: int = None):
        self._bus_id = bus_id
        self._route_code = route_code
        self._model = model
        self._times_used = times_used

    @property
    def bus_id(self):
        return self._bus_id

    @bus_id.setter
    def bus_id(self, new):
        self._bus_id = new

    @property
    def route_code(self):
        return self._route_code

    @route_code.setter
    def route_code(self, new):
        self._route_code = new

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, new):
        self._model = new

    @property
    def times_used(self):
        return self._times_used

    @times_used.setter
    def times_used(self, new):
        self._times_used = new

    def __str__(self):
        return f"(Bus: {self._bus_id}, Route: {self._route_code}, Model: {self._model}, Times Used: {self._times_used})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self._bus_id == other.bus_id and \
            self._route_code == other.route_code and \
            self._model == other.model and \
            self._times_used == other
