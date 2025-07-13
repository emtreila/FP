class Room:
    def __init__(self, room_number: int, room_type: str, capacity: int):
        self._room_number = room_number
        self._room_type = room_type
        self._capacity = capacity

    @property
    def room_number(self):
        return self._room_number

    @room_number.setter
    def room_number(self, value):
        self._room_number = value

    @property
    def room_type(self):
        return self._room_type

    @room_type.setter
    def room_type(self, value):
        self._room_type = value

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        self._capacity = value

    def str(self):
        return f"Room {self.room_number}: {self.room_type}, {self.capacity} guests"

    def __repr__(self):
        return self.str()


class Reservation:
    def __init__(self, room_number: int, name: str, guests: int, arrival_date, departure_date):
        self._reservation_id = None
        self._room_number = room_number
        self._name = name
        self._guests = guests
        self._arrival_date = arrival_date
        self._departure_date = departure_date

    @property
    def reservation_id(self):
        return self._reservation_id

    @reservation_id.setter
    def reservation_id(self, value):
        self._reservation_id = value

    @property
    def room_number(self):
        return self._room_number

    @room_number.setter
    def room_number(self, value):
        self._room_number = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def guests(self):
        return self._guests

    @guests.setter
    def guests(self, value):
        self._guests = value

    @property
    def arrival_date(self):
        return self._arrival_date

    @arrival_date.setter
    def arrival_date(self, value):
        self._arrival_date = value

    @property
    def departure_date(self):
        return self._departure_date

    @departure_date.setter
    def departure_date(self, value):
        self._departure_date = value

    def __str__(self):
        return (f"Reservation(Room {self.room_number}, {self.name}, {self.guests} guests, "
                f"{self.arrival_date} to {self.departure_date})")

    def __repr__(self):
        return self.__str__()

