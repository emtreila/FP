from orders import Orders
from driver import Driver


class TextMemoRepoDriver:
    def __init__(self, file_name: str = "drivers.txt"):
        self._file_name = file_name
        self._drivers_data: dict = {}
        self._last_id = 0
        self.__read_from_file()

    def __read_from_file(self):
        with open(self._file_name, "r") as f:
            for line in f.readlines():
                attributes = line.strip().split(",")
                if len(attributes) != 2:
                    continue

                taxi_id = int(attributes[0])
                name = attributes[1]

                taxi = Driver(name)
                taxi.driver_id = taxi_id
                self._last_id = taxi_id + 1
                self._drivers_data[taxi_id] = taxi

    def get_all_drivers(self):
        """
        :return: gets all drivers
        """
        return self._drivers_data

    def get_driver_by_id(self, driver_id):
        """
        :param driver_id: the id for the driver
        :return: the driver with the given id
        """
        drivers = self._drivers_data.values()
        for driver in drivers:
            if driver.driver_id == driver_id:
                return driver


class TextMemoRepoOrder:
    def __init__(self, file_name: str = "orders.txt"):
        self._file_name = file_name
        self._orders_data: list[Orders] = []
        self.__read_from_file()

    def __read_from_file(self):
        with open(self._file_name, "r") as f:
            for line in f.readlines():
                attributes = line.strip().split(",")
                if len(attributes) != 2:
                    continue

                driver_id = int(attributes[0])
                km = int(attributes[1])

                order = Orders(driver_id, km)
                self._orders_data.append(order)

    def write_to_file(self):

        with open(self._file_name, "w") as f:
            orders_list = self._orders_data
            for order in orders_list:
                f.write(f"{order.driver_id}, {order.km}\n")

    def add_to_file(self, order):
        with open(self._file_name, "a") as f:
            f.write(f"{order.driver_id}, {order.km}\n")

    def add_order(self, driver_id, km):
        """
        Adds order to the file
        :param driver_id: the drivers id
        :param km: the distance in km
        """
        order = Orders(driver_id, km)
        self._orders_data.append(order)
        self.add_to_file(order)

    def get_all_orders(self):
        """
        :return: all the orders
        """
        return self._orders_data
