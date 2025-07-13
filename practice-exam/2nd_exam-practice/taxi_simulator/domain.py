class Taxi:
    def __init__(self, x, y, fare, taxi_id: int = None):
        self._taxi_id = taxi_id
        self._x = x
        self._y = y
        self._fare = fare

    @property
    def taxi_id(self):
        return self._taxi_id

    @taxi_id.setter
    def taxi_id(self, new_id):
        self._taxi_id = new_id

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, new_x):
        self._x = new_x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, new_y):
        self._y = new_y

    @property
    def fare(self):
        return self._fare

    @fare.setter
    def fare(self, new_fare):
        self._fare = new_fare

    def __str__(self):
        return f"(Taxi: {self._taxi_id},Location: {self._x}, {self._y}), Fare: {self._fare}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self._taxi_id == other.driver_id and \
            self._x == other.x and \
            self._y == other.y and \
            self._fare == other.fare