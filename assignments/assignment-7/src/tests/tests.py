import unittest

from src.domain.domain import Expense
from src.repository.repository import Repository, ExpenseMemoryRepo
from src.services.services import Services



class TestDomain(unittest.TestCase):

    def test_expense(self):
        expense = Expense(4, 20, "abcdef")
        self.assertEqual(expense.id, None, "There should be no id")

        # test setter + getter id
        expense.id = 13
        self.assertEqual(expense.id, 13, "The ids arent the same")

        # test setter + getter day
        self.assertEqual(expense.day, 4, "The days arent the same")
        expense.day = 7
        self.assertEqual(expense.day, 7, "The days arent the same")

        # test setter + getter amount
        self.assertEqual(expense.amount, 20, "The amounts arent the same")
        expense.amount = 29
        self.assertEqual(expense.amount, 29, "The amounts arent the same")

        # test setter + getter type
        self.assertEqual(expense.type, "abcdef", "The types arent the same")
        expense.type = "testtest"
        self.assertEqual(expense.type, "testtest", "The types arent the same")


class TestRepo(unittest.TestCase):

    def test_memory_repo(self):
        memory_rep = ExpenseMemoryRepo()
        self.assertEqual(len(memory_rep.expenses), 10, "The lenghts arent the same")
        expense = Expense(4, 20, "abcdef")
        memory_rep.add(expense)
        self.assertEqual(len(memory_rep.expenses), 11, "The lenghts arent the same")
        memory_rep.undo()
        self.assertEqual(len(memory_rep.expenses), 10, "The lenghts arent the same")


class TestServices(unittest.TestCase):

    def test_services(self):
        repo = ExpenseMemoryRepo()
        services = Services(repo)

        services.add(14, 43, "test")
        self.assertEqual(len(services.display()), 11, "The lenghts arent the same")


if __name__ == "__main__":
    unittest.main()
