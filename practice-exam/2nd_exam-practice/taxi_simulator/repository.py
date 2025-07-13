from taxi_simulator.domain import Taxi


class MemoRepo:
    def __init__(self):
        self._taxi_data: dict[int, Taxi] = {}
        self._last_id = 0

    def calculate_distance(self, x, y, taxi: Taxi):
        """
        Calculate Manhattan distance to a given point (x, y)
        :param x: coordinate x
        :param y: coordinate y
        :param taxi: the taxi
        :return: the distance
        """
        return abs(x - taxi.x) + abs(y - taxi.y)

    def is_valid_distance(self, x, y, taxi):
        """
        Checks if the distance between the given coordinates and the coordinates of the taxi is bigger than 5
        :param x: coordinate x
        :param y: coordniate y
        :param taxi: the taxi
        :return: True = if the distance is valid False = invalid distance
        """
        return self.calculate_distance(x, y, taxi) >= 5

    def add_taxi(self, taxi: Taxi):
        """
        Adds a new operational taxi
        :param taxi: the new taxi
        """
        self._taxi_data[self._last_id] = taxi
        taxi.taxi_id = self._last_id
        self._last_id += 1

    def update_taxi(self, new_taxi: Taxi):
        """
        Updates an existing taxi
        :param new_taxi: the updated taxi
        """
        self._taxi_data[new_taxi.taxi_id] = new_taxi

    def get_all_taxis(self):
        """
        :return: list of all the taxis
        """
        return list(self._taxi_data.values())

    def get_taxi_by_id(self, id_):
        """
        Gets the taxi by the id
        :param id_: the id for the taxi
        :return: the taxi with that id
        """
        return self._taxi_data[id_]
