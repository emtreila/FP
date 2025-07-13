class Orders:
    def __init__(self, driver_id, km):
        self._driver_id = driver_id
        self._km = km

    @property
    def driver_id(self):
        return self._driver_id

    @driver_id.setter
    def driver_id(self, new):
        self._driver_id = new

    @property
    def km(self):
        return self._km

    @km.setter
    def km(self, new):
        self._km = new

    def __str__(self):
        return f"Driver ID: {self._driver_id}, KM: {self._km}"

    def __repr__(self):
        return self.__str__()
