from src.domain import Player


class TextRepoPlayer:
    def __init__(self, file_name: str = "players.txt"):
        self._file_name = file_name
        self._last_id = 0
        self._players_data: dict[int, Player] = {}
        self.__read_players()

    def __read_players(self):
        """
        Reads from file all the players
        """
        with open(self._file_name, "r") as f:
            for line in f.readlines():
                attributes = line.strip().split(",")
                if len(attributes) != 3:
                    continue

                player_id = int(attributes[0])
                name = str(attributes[1])
                strength = int(attributes[2])

                player = Player(name, strength, player_id)
                self._players_data[player_id] = player

                self._last_id = player_id + 1
                self._players_data[player_id] = player

    def get_all_players(self):
        """
        Returns all the players
        :return: all the players
        """
        return self._players_data

    def get_player_by_id(self, id_):
        """
        Retursn the player with the given id
        :param id_: the id for the player
        :return: the player with the given id
        """
        return self._players_data[id_]
