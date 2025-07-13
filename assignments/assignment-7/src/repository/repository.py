from src.domain.domain import Expense
import copy
import pickle
import random
import string


class RepositoryError(Exception):
    # this means that class RepositoryError is inherited from Python's default Exception class
    def __init__(self, message: str = ""):
        self.__message = message

    @property
    def message(self):
        return self.__message


class Repository:
    def __init__(self):
        self._data: list[Expense] = []
        self._last_id = 0
        self._undo_list = []

    @property
    def expenses(self):
        return self._data

    def add(self, expense: Expense):
        """
        Adds the given expense to the repository
        :param expense: the expense to be added
        :raises RepositoryError: if an expense with the same id already exists
        """
        pass

    def undo(self):
        """
        Undos the last change on data
        """
        pass

    def generate_entries(self):
        gen_entries = []
        for _ in range(10):
            day = random.randint(1, 30)
            amount = random.randint(1, 100)
            type_ = "".join(random.choices(string.ascii_letters, k=10))

            expense = Expense(day, amount, type_)
            expense.id = self._last_id
            self._last_id += 1

            gen_entries.append(expense)
        self._data = gen_entries


class ExpenseMemoryRepo(Repository):
    def __init__(self):
        super().__init__()

        # Generate entries in init only if
        # the repository is in memory
        # The entries for the other repositories will be
        # randomly generated if the files do not exist
        if type(self) == ExpenseMemoryRepo:
            self.generate_entries()

    def add(self, expense: Expense):
        """
        Adds the given expense to the repository
        :param expense: the expense to be added
        :raises RepositoryError: if an expense with the same id already exists
        """
        self._undo_list.append(copy.deepcopy(self._data))
        expense.id = self._last_id
        self._data.append(expense)
        self._last_id += 1

    def undo(self):
        """
        Undos the last change on data
        """
        if not self._undo_list:
            raise RepositoryError("No more undos!")

        self._data = self._undo_list.pop()


class ExpenseTextFileRepo(ExpenseMemoryRepo):
    def __init__(self, filename: str = "FileExpenses.txt"):
        super().__init__()
        self._file_name = filename
        self.__read_from_file()

    def __read_from_file(self):
        """
        Reads from file all the expenses
        """
        try:
            with open(self._file_name, "r") as f:
                for line in f.readlines():
                    attributes = line.strip().split(",")
                    if len(attributes) != 4:
                        continue

                    id_ = int(attributes[0])
                    day = int(attributes[1])
                    amount = int(attributes[2])
                    type_ = attributes[3]

                    expense = Expense(day, amount, type_)
                    expense.id = id

                    self._last_id = id_ + 1
                    self._data.append(expense)
        except FileNotFoundError:
            # file will be created on first write
            self.generate_entries()
            self.__write_to_file()

    def __add_to_file(self, expense):
        """
        Adds an expense to file
        :param expense: new expense
        """

        with open(self._file_name, "a") as f:
            f.write(f"{expense.id},{expense.day},{expense.amount},{expense.type}\n")

    def __write_to_file(self):
        """
        Writes all expenses to file
        """

        with open(self._file_name, "w") as f:
            for expense in self._data:
                f.write(f"{expense.id},{expense.day},{expense.amount},{expense.type}\n")

    def add(self, expense):
        super().add(expense)
        self.__add_to_file(expense)

    def undo(self):
        super().undo()
        self.__write_to_file()


class ExpenseBinaryFileRepo(ExpenseTextFileRepo):
    def __init__(self, filename: str = "FileExpenses.bin"):
        super().__init__(filename)

    def __read_from_file(self):
        try:
            with open(self._file_name, "rb") as f:
                self._data = pickle.load(f)
        except FileNotFoundError:
            self.generate_entries()
            self.__write_to_file()

    def __add_to_file(self, expense):
        with open(self._file_name, "ab") as f:
            pickle.dump(expense, f)

    def __write_to_file(self):
        with open(self._file_name, "wb") as f:
            pickle.dump(self._data, f)
