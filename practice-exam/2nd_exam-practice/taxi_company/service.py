import math

from taxi_company.repository import TextMemoRepo


class Service(TextMemoRepo):
    def __init__(self, address_repo: TextMemoRepo = TextMemoRepo):
        super().__init__()
        self._address_repo = address_repo

    def add_address(self, new):
        """
        Add a new address
        :param new: the new address
        """
        self._address_repo.add_address(new)

    def handle_name(self, name: str):
        """
        Check if the name is ok
        :param name: name to be checked
        """
        words = name.strip().split(" ")
        for word in words:
            if len(word) < 3:
                raise ValueError("The words must have at least 3 letters!")

    def handle_number(self, number):
        """
        Check if the number is ok
        :param number: the number to be checked
        """
        if number < 0:
            raise ValueError("The number must be positive!")
        if number > 100:
            raise ValueError("The max number is 100!")

    def handle_x(self, x):
        """
        Check if the x is ok
        :param x: the number to be checked
        """
        if not (-100 <= x <= 100):
            raise ValueError("X must be between -100 and 100!")

    def handle_y(self, y):
        """
        Check if the y is ok
        :param y: the number to be checked
        """
        if not (-100 <= y <= 100):
            raise ValueError("Y must be between -100 and 100!")

    def calculate_distance(self, x1, x2, y1, y2):
        """
        Calculates the Euclidian distance
        :param x1: coordonate x1
        :param x2: coordonate x2
        :param y1: coordonate y1
        :param y2: coordonate y2
        :return: the distance
        """
        return math.sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))

    def check_coordinates(self, x, y):
        """
        Check if there is already a taxi with those coordinates
        :param x: coordinate x
        :param y: coordinate y
        :return: True = there is, False = there is not
        """

        addresses = self.get_all_addresses().values()
        for address in addresses:
            if address.x == x and address.y == y:
                return True
        return False
