import unittest

from taxi_simulator.repository import MemoRepo
from taxi_simulator.services import Service
from taxi_simulator.domain import Taxi


class TestService(unittest.TestCase):
    def setUp(self):
        self._repository = MemoRepo()
        self._service = Service(self._repository)
        # Add predefined taxis to the repo
        self._repository.add_taxi(Taxi(10, 10, 0, 0))  # Taxi ID 0
        self._repository.add_taxi(Taxi(20, 20, 0, 1))  # Taxi ID 1
        self._repository.add_taxi(Taxi(30, 30, 0, 2))  # Taxi ID 2

    def test_add_ride_updates_correct_taxi(self):
        # Start and end point of the ride
        start_x, start_y = 12, 12  # Closer to Taxi ID 0
        end_x, end_y = 25, 25
        nr_of_taxis = 3

        # Calculate expected values
        expected_taxi_id = 0
        expected_ride_distance = abs(end_x - start_x) + abs(end_y - start_y)
        expected_new_fare = expected_ride_distance
        expected_new_location = (end_x, end_y)

        self._service.add_ride(start_x, start_y, end_x, end_y, nr_of_taxis)

        # Verify if the correct taxi was updated
        updated_taxi = self._repository.get_taxi_by_id(expected_taxi_id)
        self.assertEqual(updated_taxi.fare, expected_new_fare)
        self.assertEqual((updated_taxi.x, updated_taxi.y), expected_new_location)


