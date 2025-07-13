from src.domain import Reservation, Room


class Repo:
    def __init__(self, file_name1: str = "rooms.txt", file_name2: str = "reservations.txt"):
        self._file_name1 = file_name1
        self._file_name2 = file_name2
        self._rooms_data: dict = {}
        self._reservations_data: dict[int, Reservation] = {}
        self._last_id = 0
        self.read_from_file_rooms()
        self.read_from_file_reservations()

    def read_from_file_rooms(self):
        """
        Reads from file all the rooms
        """
        try:
            with open(self._file_name1, "r") as f:
                for line in f.readlines():
                    attributes = line.strip().split(",")
                    if len(attributes) != 3:
                        continue
                    room_number = int(attributes[0])
                    room_type = str(attributes[1])
                    capacity = int(attributes[2])

                    room = Room(room_number, room_type, capacity)

                    self._rooms_data[room_number] = room
        except FileNotFoundError:
            raise Exception("File not found")

    def read_from_file_reservations(self):
        """
        Reads from file all the reservations
        """
        try:
            with open(self._file_name2, "r") as f:
                for line in f.readlines():
                    attributes = line.strip().split(",")
                    if len(attributes) != 6:
                        continue
                    reservation_id = int(attributes[0])
                    room_number = int(attributes[1])
                    name = str(attributes[2])
                    guests = int(attributes[3])
                    arrival_date = attributes[4]
                    departure_date = attributes[5]

                    reservation = Reservation(room_number, name, guests, arrival_date, departure_date)
                    reservation.reservation_id = reservation_id

                    self._last_id = reservation_id + 1
                    self._reservations_data[reservation_id] = reservation
        except FileNotFoundError:
            raise Exception("File not found")

    def write_to_file_reservations(self):
        """
        Writes to file all the reservations
        """
        with open(self._file_name2, "w") as f:
            for reservation in self._reservations_data.values():
                f.write(f"{reservation.reservation_id},{reservation.room_number},{reservation.name},"
                        f"{reservation.guests},{reservation.arrival_date},{reservation.departure_date}\n")

    def get_rooms(self):
        """
        :return: all the rooms
        """
        return self._rooms_data

    def get_reservations(self):
        """
        :return: all the reservations
        """
        return self._reservations_data

    def add_reservation(self, reservation: Reservation):
        """
        Adds a reservation
        :param reservation: the reservation to be added
        """
        reservation.reservation_id = self._last_id
        self._last_id += 1

        self._reservations_data[reservation.reservation_id] = reservation
        self.write_to_file_reservations()

    def delete_reservation_by_id(self, reservation_id):
        """
        Deletes a reservation by id
        :param reservation_id: the id of the reservation
        :return: the deleted reservation
        """
        if reservation_id not in self._reservations_data:
            return None

        reservation = self._reservations_data[reservation_id]
        del self._reservations_data[reservation_id]
        self.write_to_file_reservations()
        return reservation

