from repository import TextMemoRepoDriver, TextMemoRepoOrder


class Service:
    def __init__(self, driver_repo: TextMemoRepoDriver = TextMemoRepoDriver, order_repo: TextMemoRepoOrder = TextMemoRepoOrder):
        super().__init__()
        self._driver_repo = driver_repo
        self._order_repo = order_repo

    def add_order(self, driver_id, km):
        """
        Adds a new order to the file
        :param driver_id: the id for the driver
        :param km: the distance in km
        """
        self._order_repo.add_order(driver_id, km)

    def get_all_drivers(self):
        """
        :return: all the drivers
        """
        return self._driver_repo.get_all_drivers()

    def get_driver_by_id(self, driver_id):
        """
        :param driver_id: the id for the driver
        :return: the driver with that id
        """
        return self._driver_repo.get_driver_by_id(driver_id)


    def get_all_orders(self):
        """
        :return: all the orders
        """
        return self._order_repo.get_all_orders()

    def calculate_income(self, driver_id):
        """
        Calculate the total income of a driver
        :param driver_id: the driver
        :return: the total income
        """
        orders = self._order_repo.get_all_orders()
        income = 0
        for order in orders:
            if order.driver_id == driver_id:
                income += order.km
        return income * 2.5