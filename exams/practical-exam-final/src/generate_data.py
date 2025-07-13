import random


def generate_rooms_file(file_name: str):
    rooms = [
        {"room_number": 1, "type": "Single", "capacity": 1},
        {"room_number": 2, "type": "Single", "capacity": 1},
        {"room_number": 3, "type": "Double", "capacity": 2},
        {"room_number": 4, "type": "Family", "capacity": 4},
        {"room_number": 5, "type": "Family", "capacity": 4}
    ]

    with open(file_name, "w") as file:
        for room in rooms:
            file.write(f"{room['room_number']},{room['type']},{room['capacity']}\n")


def generate_random_reservations(file_name: str, num_reservations: int = 1000):
    rooms = [
        {"room_number": 1, "type": "Single", "capacity": 1},
        {"room_number": 2, "type": "Single", "capacity": 1},
        {"room_number": 3, "type": "Double", "capacity": 2},
        {"room_number": 4, "type": "Family", "capacity": 4},
        {"room_number": 5, "type": "Family", "capacity": 4}
    ]

    family = ["Adumitroaei", "Antohi", "Badea", "Balan", "Bejan", "Cosnita", "Iovu", "Silitra", "Ciulei", "Rarita",
              "Gavril", "Florea", "Roman", "Munteanu", "Patras", "Stan", "Gutu", "Condrea", "Vrajitoru", "Calancea",
              "Zaharia", "Pasarica", "Mircea"]

    given = ["Melania", "Maria", "Miruna", "Nikolas", "Costel", "Alexandru", "Amalia", "Rares", "Iurie", "David",
             "Tudor", "Alexandra", "Alessia", "Malina", "Fabian", "George", "Razvan", "Sofia", "Elisa", "Teona",
             "Teodora", "Teodor", "Iasmin", "Dragos", "Georgiana", "Clara", "Roxana"]

    names = [
        f"{random.choice(family)} {random.choice(given)}" for _ in range(100)
    ]

    reservations = []

    for _ in range(num_reservations):
        room = random.choice(rooms)
        name = random.choice(names)
        num_guests = random.randint(1, room["capacity"])

        arrival_day = random.randint(1, 31)
        arrival_month = random.randint(1, 12)

        departure_day = random.randint(arrival_day, 31)
        departure_month = random.randint(arrival_month, 12)

        reservations.append(
            f"{room['room_number']},{name},{num_guests},{arrival_day}-{arrival_month},{departure_day}-{departure_month}")

    with open(file_name, "w") as file:
        for reservation in reservations:
            file.write(reservation + "\n")


def main():
    generate_rooms_file("rooms.txt")
    generate_random_reservations("reservations_generated.txt", 1000)


main()

