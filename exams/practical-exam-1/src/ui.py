import functions
from src.functions import show_artist
from src.functions import show_season
from src.functions import test_add
from src.functions import add
from src.functions import check_festival_name


def menu():
    print("MENU")
    print("1) Add a music festival")
    print("2) Show all festivals taking place during a season")
    print("3) Show all festivals where an artist performs")


def main():
    menu()
    test_add()
    festival = [
        ["Untold", 8, "500", ["A", "B", "C"]],
        ["Beach", 4, "400", ["E", "F", "G"]],
        ["Winter", 1, "200", ["H", "A", "J"]]

    ]
    while True:
        command = input("Please enter your choice:")

        try:
            command = int(command)
        except:
            print("give a number")
            continue

        if command == 1:
            name = input("name:")
            month = input("month:")
            ticket = input("ticket cost:")
            artists = list(input("name:"))

            try:
                month = int(month)
            except:
                print("The month must be a number")

            if not (1 <= month <= 12):
                print("Not valid month")
                continue

            try:
                ticket = int(ticket)
            except:
                print("The ticket must be a number")
                continue

            is_ok = check_festival_name(festival, name)
            if not is_ok:
                print("Name already used")
                continue

            festival = add(festival, name, month, ticket, artists)

        if command == 2:
            season = input("season:")
            festivals_season = show_season(festival, season)
            for i in range(len(festivals_season)):
                if festivals_season[i][1] == 1:
                    festivals_season[i][1] = "January"
                if festivals_season[i][1] == 2:
                    festivals_season[i][1] = "February"
                if festivals_season[i][1] == 3:
                    festivals_season[i][1] = "March"
                if festivals_season[i][1] == 4:
                    festivals_season[i][1] = "April"
                if festivals_season[i][1] == 5:
                    festivals_season[i][1] = "May"
                if festivals_season[i][1] == 6:
                    festivals_season[i][1] = "June"
                if festivals_season[i][1] == 7:
                    festivals_season[i][1] = "July"
                if festivals_season[i][1] == 8:
                    festivals_season[i][1] = "August"
                if festivals_season[i][1] == 9:
                    festivals_season[i][1] = "September"
                if festivals_season[i][1] == 10:
                    festivals_season[i][1] = "October"
                if festivals_season[i][1] == 11:
                    festivals_season[i][1] = "November"
                if festivals_season[i][1] == 12:
                    festivals_season[i][1] = "December"

            print(festivals_season)

        if command == 3:
            festivals_performing_artist = []
            artist_name = input("Artist:")
            festivals_performing_artist = show_artist(festival, artist_name)
            print(festivals_performing_artist)


main()
