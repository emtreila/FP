import calendar

from texttable import Texttable

from src.services import Service

CURRENT_YEAR = 2025


class UI:
    def __init__(self, service: Service = Service):
        self._service = service
        self._first = True

    def show_table(self, table, month):
        new = Texttable()

        header = ["Number", month, "Name", "Guests"]
        new.header(header)

        for row in table:
            new.add_row([row[0], f"{row[1]}-{row[2]}", row[3], row[4]])
        print(new.draw())

    def show_monthly_report(self, report, month):
        cal = calendar.TextCalendar()
        month_calendar = cal.monthdayscalendar(CURRENT_YEAR, month)

        table = Texttable()
        table.header(["M", "T", "W", "T", "F", "S", "S"])

        for week in month_calendar:
            row = []
            for day in week:
                if day == 0:
                    row.append("")
                    continue
                row.append(f"{day}/{report.get(int(day), "")}")

            table.add_row(row)

        print(table.draw())

    def main(self):

        while True:
            print("\n1. Display all reservations for a given period.")
            print("2. Create reservation.")
            print("3. Delete reservation by number.")
            print("4. Monthly report.")
            print("0. Exit.")

            choice = input("Enter your choice: ")
            if not choice:
                print("Invalid choice")
            try:
                choice = int(choice)
            except ValueError:
                print("Invalid choice")
                continue
            if not (0 <= choice <= 4):
                print("Invalid choice")
                continue

            if choice == 0:
                print("Exiting reservations!")
                break

            if choice == 1:
                period_of_time = input("Enter the period of time: ")
                if not period_of_time:
                    print("Invalid period of time")
                    continue

                try:
                    arrival_date, departure_date = period_of_time.split("-")
                    arrival_day = int(arrival_date.split(".")[0])
                    arrival_month = int(arrival_date.split(".")[1])
                    departure_day = int(departure_date.split(".")[0])
                    departure_month = int(departure_date.split(".")[1])
                except:
                    print("Invalid period of time passed! Format: dd.mm-dd.mm")
                    continue

                if not (
                        1 <= arrival_day <= 31 and 1 <= arrival_month <= 12 and 1 <= departure_day <= 31 and 1 <= departure_month <= 12):
                    print("Invalid period of time")
                    continue
                if arrival_month > departure_month or (
                        arrival_month == departure_month and arrival_day > departure_day):
                    print("Invalid period of time")
                    continue

                while arrival_month <= departure_month:
                    if self._first:
                        table = self._service.reservation_for_period_of_time(arrival_month, arrival_day, arrival_month,
                                                                             31)
                        self._first = False
                    else:
                        table = self._service.reservation_for_period_of_time(arrival_month, 1, arrival_month, 31)

                    month = self._service.get_month(arrival_month)
                    self.show_table(table, month)

                    arrival_month += 1

            elif choice == 2:
                arrival_date = input("Enter the arrival date: ").strip()
                if not arrival_date:
                    print("Invalid arrival date")
                    continue

                try:
                    arrival_day = int(arrival_date.split(".")[0])
                    arrival_month = int(arrival_date.split(".")[1])
                except:
                    print("Invalid arrival date! Format: dd.mm")
                    continue

                if not (1 <= arrival_day <= 31 and 1 <= arrival_month <= 12):
                    print("Invalid arrival date")
                    continue

                departure_date = input("Enter the departure date: ").strip()
                if not departure_date:
                    print("Invalid departure date")
                    continue

                try:
                    departure_day = int(departure_date.split(".")[0])
                    departure_month = int(departure_date.split(".")[1])
                except:
                    print("Invalid departure date! Format: dd.mm")
                    continue

                if not (1 <= departure_day <= 31 and 1 <= departure_month <= 12):
                    print("Invalid departure date")
                    continue

                available_rooms = self._service.get_available_rooms(arrival_month, arrival_day, departure_month,
                                                                    departure_day)
                if not available_rooms:
                    print("No available rooms")
                    continue

                print("Available rooms:")
                for room in available_rooms:
                    print(room)

                room_number = input("Enter the room number: ").strip()
                if not room_number:
                    print("Invalid room number")
                    continue

                try:
                    room_number = int(room_number)
                except:
                    print("Invalid room number")
                    continue

                name = input("Enter the name: ").strip()

                if not name:
                    print("Invalid name")
                    continue

                guests = input("Enter the number of guests: ").strip()
                if not guests:
                    print("Invalid number of guests")
                    continue

                try:
                    guests = int(guests)
                except:
                    print("Invalid number of guests")
                    continue

                try:
                    self._service.create_reservation(room_number, name, guests, arrival_date, departure_date)
                    print("Reservation created successfully")
                except Exception as e:
                    print(f"Error creating reservation: {e}")
                    continue


            elif choice == 3:
                reservation_id = input("Enter the reservation number: ").strip()
                if not reservation_id:
                    print("Invalid reservation number")
                    continue

                try:
                    reservation_id = int(reservation_id)
                except:
                    print("Invalid reservation number")
                    continue

                try:
                    self._service.delete_reservation_by_id(reservation_id)
                    print("Reservation deleted successfully")
                except Exception as e:
                    print(f"Error deleting reservation: {e}")
                    continue

            elif choice == 4:
                month = input("Enter the month: ")
                if not month:
                    print("Invalid month")
                    continue

                try:
                    month = int(month)
                except:
                    print("Invalid month")
                    continue

                if not (1 <= month <= 12):
                    print("Invalid month")
                    continue

                result = self._service.monthly_report(month)
                self.show_monthly_report(result, month)

