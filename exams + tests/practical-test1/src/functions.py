def create_festival(name, month, ticket, artist):
    return [name, month, ticket, artist]


def get_name(festival, position):
    return festival[position][0]


def get_month(festival, position):
    return festival[position][1]


def get_ticket(festival, position):
    return festival[position][2]


def get_artists(festival, position):
    return festival[position][3]


def set_name(festival, position, name):
    festival[position][0] = name


def set_month(festival, position, month):
    festival[position][1] = month


def set_ticket(festival, position, ticket):
    festival[position][2] = ticket


def set_artists(festival, position, artists):
    festival[position][3] = artists


def to_string(name, month, ticket, artists):
    return f"{name}, {month}, {ticket}, {artists}"


def check_festival_name(festival, name):
    for i in range(len(festival)):
        if festival[i][0] == name:
            return False
    return True


def add(festivals, name, month, ticket, artists):
    """
    Adds a festival to the list of festivals
    :param festivals: list of festivals
    :param name: name of festival
    :param month: month of festival
    :param ticket: ticket price of festival
    :param artists: artists playing
    :return: the new festival
    """
    new_festival = create_festival(name, month, ticket, artists)
    return festivals.append(new_festival)


def test_add():
    festivals = [
        ["Untold", 8, "500", ["A", "B", "C"]],
        ["Beach", 4, "400", ["E", "F", "G"]],
        ["Winter", 1, "200", ["H", "A", "J"]]
    ]
    add(festivals, "F1", 2, 400, ["a1", "a2"])
    try:
        assert festivals[3] == ["F1", 2, 400, ["a1", "a2"]]
        print("test add success")
    except:
        print("fail")


def show_season(festival, season):

    festivals_during_season = []
    if season == "winter":
        for i in range(len(festival)):
            if festival[i][1] == 12 or festival[i][1] == 1 or festival[i][1] == 2:
                festivals_during_season.append(festival[i])
    if season == "spring":
        for i in range(len(festival)):
            if festival[i][1] == 3 or festival[i][1] == 4 or festival[i][1] == 5:
                festivals_during_season.append(festival[i])
    if season == "summer":
        for i in range(len(festival)):
            if festival[i][1] == 6 or festival[i][1] == 7 or festival[i][1] == 8:
                festivals_during_season.append(festival[i])
    if season == "autumn":
        for i in range(len(festival)):
            if festival[i][1] == 9 or festival[i][1] == 10 or festival[i][1] == 11:
                festivals_during_season.append(festival[i])

    festivals_during_season.sort(key=lambda x: x[1])
    return festivals_during_season


def show_artist(festival, artist):
    artists_performing = []
    for i in range(len(festival)):
        for j in get_artists(festival,i):
            if j == artist:
                artists_performing.append(festival[i])
    artists_performing.sort(key=lambda x: x[1], reverse=False)
    return artists_performing
