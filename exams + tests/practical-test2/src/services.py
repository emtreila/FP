import math
import random

from src.repository import TextRepoPlayer


class Service(TextRepoPlayer):
    def __init__(self, player_repo: TextRepoPlayer = TextRepoPlayer):
        super().__init__()
        self._player_repo = player_repo

    def get_all_players(self):
        """
        Returns all the players
        :return: all the players
        """
        return self._player_repo.get_all_players()

    def pairs(self, players):
        """
        Generates random pairs to play the game
        :return: the pairs
        """
        players_to_play = []
        random.shuffle(players)
        for i in range(0, len(players) - 1, 2):
            players_to_play.append((players[i], players[i + 1]))
        return players_to_play

    def is_power_of_2(self, players):
        """
        Check to see if the number of players is a power of 2
        :param players: the players that play
        :return: True = power of 2, False = otherwise
        """
        n = len(players)
        if n <= 0:
            return False
        while n % 2 == 0:
            n //= 2
        return n == 1

    def closest_power_of_2(self, players):
        """
        Finds the closest power of 2 to the number of players
        :param players: the players
        :return: closest power of 2 to the number of players
        """
        n = len(players)
        if n <= 0:
            return None
        return 2 ** (math.floor(math.log2(n)))
