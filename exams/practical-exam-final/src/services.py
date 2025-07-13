from src.domain import Reservation
from src.repository import Repo


class Service:
    def __init__(self, repo: Repo = Repo):
        self.repo = repo
        self.MONTHS_AND_DAYS = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }

    def reservation_for_period_of_time(self, arrival_month: int, arrival_day: int, departure_month: int,
                                       departure_day: int):
        """
        Returns the reservations for a given period of time
        :param arrival_month: the month of the arrival date
        :param arrival_day: the day of the arrival date
        :param departure_month: the month of the departure date
        :param departure_day: the day of the departure date
        :return: a list of reservations for a given period of time
        """
        table = []
        reservations = self.repo.get_reservations().values()

        for reservation in reservations:
            reservation_day, reservation_month = reservation.arrival_date.split("-")
            reservation_departure_day, reservation_departure_month = reservation.departure_date.split("-")
            if (arrival_month <= int(reservation_month) <= departure_month and arrival_day <= int(
                    reservation_day) <= departure_day) or (
                    int(reservation_departure_month) == departure_month and int(
                reservation_departure_day) <= departure_day):
                table.append(
                    [reservation.reservation_id, reservation.arrival_date, reservation.departure_date, reservation.name,
                     reservation.guests])
        return sorted(table, key=lambda x: (x[1], x[2], x[3]))

    def get_month(self, month):
        """
        Returns the month as a string
        :param month: the month as an integer
        :return: the month as a string
        """
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
                  "November", "December"]
        return months[month - 1]

    def get_available_rooms(self, arrival_month: int, arrival_day: int, departure_month: int, departure_day: int):
        """
        Returns the available rooms for a given period of time
        :param arrival_month: the month of the arrival date
        :param arrival_day: the day of the arrival date
        :param departure_month: the month of the departure date
        :param departure_day: the day of the departure date
        :return: the available rooms for a given period of time
        """
        rooms = self.repo.get_rooms().values()
        reservations = self.repo.get_reservations().values()
        available_rooms = []
        for room in rooms:
            is_available = True
            for reservation in reservations:
                reserv_day = int(reservation.arrival_date.split("-")[0])
                reserv_month = int(reservation.arrival_date.split("-")[1])
                reserv_dep_day = int(reservation.departure_date.split("-")[0])
                reserv_dep_month = int(reservation.departure_date.split("-")[1])
                if (
                        arrival_month <= reserv_month <= departure_month and arrival_day <= reserv_day <= departure_day) or (
                        reserv_dep_month == departure_month and reserv_dep_day <= departure_day):
                    if room.room_number == reservation.room_number:
                        is_available = False
                        break
            if is_available:
                available_rooms.append(room)
        return available_rooms

    def get_rooms(self):
        """
        :return: all the rooms
        """
        return self.repo.get_rooms()

    def get_reservations(self):
        """
        :return: all the reservations
        """
        return self.repo.get_reservations()

    def create_reservation(self, room_number: int, name: str, guests: int, arrival_date: str, departure_date: str):
        """
        Creates a reservation
        :param room_number: the room number
        :param name: the name of the guest
        :param guests: the number of guests
        :param arrival_date: the arrival date
        :param departure_date: the departure date
        :raises ValueError: if the number of guests is invalid or the room is not available
        """
        arrival_day, arrival_month = arrival_date.split(".")
        departure_day, departure_month = departure_date.split(".")

        # Checking the number of guests
        if guests < 1 or self.repo.get_rooms()[room_number].capacity < guests:
            raise ValueError("Invalid number of guests")

        reservations = self.repo.get_reservations().values()
        for reservation in reservations:
            if room_number == reservation.room_number:
                reserv_day, reserv_month = reservation.arrival_date.split("-")
                reserv_dep_day, reserv_dep_month = reservation.departure_date.split("-")

                if int(reserv_month) <= int(arrival_month) <= int(reserv_dep_month) and int(reserv_day) <= int(
                        arrival_day) <= int(reserv_dep_day):
                    raise ValueError("Room not available")

                if int(reserv_month) <= int(departure_month) <= int(reserv_dep_month) and int(reserv_day) <= int(
                        departure_day) <= int(reserv_dep_day):
                    raise ValueError("Room not available")

        reservation = Reservation(room_number, name, guests, f"{arrival_day}-{arrival_month}",
                                  f"{departure_day}-{departure_month}")
        self.repo.add_reservation(reservation)

    def delete_reservation_by_id(self, reservation_id):
        """
        Deletes a reservation by id
        :param reservation_id: the id of the reservation
        :raise ValueError: if the reservation is not found
        """
        if not self.repo.delete_reservation_by_id(reservation_id):
            raise ValueError("Reservation not found")

    def monthly_report(self, month: int):
        """
        Returns a monthly report, each day/number of available rooms
        :param month: The month to get the monthly report of
        :return: A dictionary containing the day and the number of available rooms
        """
        len_rooms = len(self.repo.get_rooms())
        reservations = self.repo.get_reservations().values()

        result = {day: len_rooms for day in range(1, self.MONTHS_AND_DAYS[month] + 1)}
        for reservation in reservations:
            reserv_day, reserv_month = reservation.arrival_date.split("-")
            reserv_dep_day, reserv_dep_month = reservation.departure_date.split("-")
            if int(reserv_month) <= month <= int(reserv_dep_month):
                for day in range(1, self.MONTHS_AND_DAYS[month] + 1):
                    if int(reserv_day) <= day <= int(reserv_dep_day):
                        result[day] -= 1

        return result

