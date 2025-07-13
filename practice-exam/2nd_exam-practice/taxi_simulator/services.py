from taxi_simulator.domain import Taxi
from taxi_simulator.repository import MemoRepo
import random


class Service:
    def __init__(self, taxi_repo: MemoRepo = MemoRepo()):
        self._taxi_repo = taxi_repo

    def generate_taxis(self, nr_of_taxi):
        """
        Generates taxis and sets their coordinates at random
        :param nr_of_taxi: the number of taxis that will be generated
        """
        for i in range(nr_of_taxi):
            while True:
                x = random.randint(0, 100)
                y = random.randint(0, 100)
                if all(self._taxi_repo.is_valid_distance(x, y, taxi) for taxi in self.list_taxis()):
                    taxi_generated = Taxi(x, y, 0)
                    break
            self._taxi_repo.add_taxi(taxi_generated)

    def add_ride(self, start_x, start_y, end_x, end_y, nr_of_taxis):
        """
        Adds a new ride and assigns to it the closest taxi
        :param start_x: start coordinate x
        :param start_y: start coordinate y
        :param end_x: end coordinate x
        :param end_y: end coordinate y
        :param nr_of_taxis: the number of taxis we can use
        """
        min_ = 100000000000
        id_ = 0
        for i in range(nr_of_taxis):
            distance = self._taxi_repo.calculate_distance(start_x, start_y, self._taxi_repo.get_taxi_by_id(i))
            if distance < min_:
                min_ = distance
                id_ = i

        new_fare = self._taxi_repo.get_taxi_by_id(id_).fare + abs(end_x - start_x) + abs(end_y - start_y)
        in_use_taxi = self._taxi_repo.get_taxi_by_id(id_)
        in_use_taxi.x = end_x
        in_use_taxi.y = end_y
        in_use_taxi.fare = new_fare

    def generate_ride(self, nr_of_taxis):
        """
        Generates a random ride and assigns the closest taxi to it
        :param nr_of_taxis: the number of taxis we can use
        :return: the coordinates generated
        """
        d = 0
        start_x_generated = 0
        start_y_generated = 0
        end_x_generated = 0
        end_y_generated = 0
        while d < 10:
            start_x_generated = random.randint(0, 100)
            start_y_generated = random.randint(0, 100)
            end_x_generated = random.randint(0, 100)
            end_y_generated = random.randint(0, 100)
            d = abs(end_x_generated - start_x_generated) + abs(end_y_generated - start_y_generated)

        min_ = 100000000000
        id_ = 0
        for i in range(nr_of_taxis):
            distance = self._taxi_repo.calculate_distance(start_x_generated, start_y_generated,
                                                          self._taxi_repo.get_taxi_by_id(i))
            if min_ > distance:
                min_ = distance
                id_ = i

        new_fare = self._taxi_repo.get_taxi_by_id(id_).fare + abs(end_x_generated - start_x_generated) + abs(
            end_y_generated - start_y_generated)
        in_use_taxi = self._taxi_repo.get_taxi_by_id(id_)
        in_use_taxi.x = end_x_generated
        in_use_taxi.y = end_y_generated
        in_use_taxi.fare = new_fare
        return start_x_generated, start_y_generated, end_x_generated, end_y_generated

    def list_taxis(self):
        """
        :return: returns all the taxis
        """
        return self._taxi_repo.get_all_taxis()
