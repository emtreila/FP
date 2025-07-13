import unittest

from assignment_checker.repository import TextMemoRepo
from assignment_checker.service import Service


class TestService(unittest.TestCase):
    def setUp(self):
        self._assignment_repo = TextMemoRepo()
        self._service = Service(self._assignment_repo)

    def test_add_assignment(self):
        self._service.add_assignment("name", "solution")
        self.assertEqual(len(self._service.get_all_assignments()), 6)

