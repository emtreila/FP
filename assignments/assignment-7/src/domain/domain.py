class Expense:
    def __init__(self, day: int, amount: int, type_: str):
        self._id = None
        self._day = day
        self._amount = amount
        self._type = type_

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, new_id):
        self._id = new_id

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, new_day):
        self._day = new_day

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, new_amount):
        self._amount = new_amount

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, new_type):
        self._type = new_type

    def __str__(self):
        return f"Day: {self._day}, Amount: {self._amount}, Type:{self._type}"

    def __repr__(self):
        return self.__str__()