from taxi_company.address import Address


class TextMemoRepo:
    def __init__(self, file_name: str = "addresses.txt"):
        self._file_name = file_name
        self._address_data: dict[int, Address] = {}
        self._last_id = 0
        self.__read_from_file()

    def __read_from_file(self):
        """
        Reads from file the addresses
        """
        with open(self._file_name, "r") as f:
            for line in f.readlines():
                attributes = line.strip().split(",")
                if len(attributes) != 5:
                    continue

                address_id = int(attributes[0])
                name = str(attributes[1])
                number = int(attributes[2])
                x = int(attributes[3])
                y = int(attributes[4])

                address = Address(name, number, x, y)
                address.address_id = address_id

                self._last_id = address_id + 1
                self._address_data[address_id] = address

    def __write_to_file(self):
        """
        Writes to file the addresses
        """
        with open(self._file_name, "w") as f:
            address_list = sorted(self._address_data.values(), key = lambda x: x.address_id)

            for address in address_list:
                f.write(f"{address.address_id}, {address.name}, {address.number}, {address.x}, {address.y}")

    def __add_to_file(self, address):
        """
        Adds to file a new address
        """
        with open(self._file_name, "a") as f:
            f.write(f"{address.address_id}, {address.name}, {address.number}, {address.x}, {address.y}")

    def add_address(self, new: Address):
        """
        Adds a new student
        :param new: the student to be added
        """
        new.address_id = self._last_id
        self._last_id += 1
        self._address_data[new.address_id] = new
        self.__add_to_file(new)

    def get_all_addresses(self):
        """
        :return: all the addresses
        """
        return self._address_data

