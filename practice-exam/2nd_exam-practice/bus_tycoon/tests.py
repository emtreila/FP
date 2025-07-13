import unittest

from bus_tycoon.repository import TextFileRepoBus, TextFileRepoRoute
from bus_tycoon.services import Service


class TestService(unittest.TestCase):
    def setUp(self):
        self._repo_bus = TextFileRepoBus()
        self._repo_bus_route = TextFileRepoRoute()
        self._service = Service(self._repo_bus, self._repo_bus_route)

    def test_km_travelled(self):
        # Add a bus and a route to the repos
        bus_id = 5
        times_used = 1

        # Calculate the expected km
        expected_km = times_used * 20

        # Check if the service returns the correct km
        self.assertEqual(self._service.km_travelled(bus_id), expected_km)

