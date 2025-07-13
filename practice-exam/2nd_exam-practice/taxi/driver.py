class Driver:
    def __init__(self, name, driver_id: int = None):
        self._name = name
        self._driver_id = driver_id

    @property
    def driver_id(self):
        return self._driver_id

    @driver_id.setter
    def driver_id(self, new):
        self._driver_id = new

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new):
        self._name = new

    def __str__(self):
        return f"Id: {self._driver_id}, Name: {self._name}"

    def __repr__(self):
        return self.__str__()
