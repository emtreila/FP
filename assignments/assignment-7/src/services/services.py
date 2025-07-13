from src.domain.domain import Expense
from src.repository.repository import Repository


class ServiceError(Exception):
    # this means that class ServiceError is inherited from Python's default Exception class
    def __init__(self, message: str = ""):
        self.__message = message

    @property
    def message(self):
        return self.__message


class Services:
    def __init__(self, repository: Repository):
        self._repository = repository

    def add(self, day: int, amount: int, type: str):
        """
        Adds a new expense
        :param day: new day
        :param amount: new amount
        :param type: new type
        """
        if not (day > 0 and amount > 0 and type != ""):
            raise ServiceError("Invalid parameters!")

        if not (1 <= day <= 30):
            raise ServiceError("The day must be an integer between 1 and 30!")

        expense = Expense(day, amount, type)
        self._repository.add(expense)

    def display(self):
        """
        Displays all the expenses
        :return: all the expenses
        """
        return self._repository.expenses

    def filter(self, amount: int):
        """
        Filters the list so that it contains only expenses above a certain value read from the console
        :param amount: the amount for which the expenses need to be above
        :return: the filtered list
        """
        if not (amount > 0):
            raise ServiceError("Invalid amount!")

        filtered_expenses = []
        for expense in self._repository.expenses:
            if amount < expense.amount:
                filtered_expenses.append(expense)

        return filtered_expenses

    def undo(self):
        """
        Undos the last operation that  modified the program data
        """
        self._repository.undo()
