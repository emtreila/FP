import math
import random

from petite_slam.player import Player
from petite_slam.repository import TextRepoPlayer


class Service(TextRepoPlayer):
    def __init__(self, player_repo: TextRepoPlayer = TextRepoPlayer):
        super().__init__()
        self._player_repo = player_repo

    def get_all_players(self):
        """
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

    def remove_loser(self, loser: Player, players):
        """
        Removes the loser from the game
        :param loser: the loser
        :param players: the players
        :return: the players without the loser
        """
        for player in players:
            if player.id == loser.player_id:
                players.remove(player)
                break
        return players

    def increase_strength(self, player, list_players):
        """
        Increases the strength of a player
        :param player: the player we increase the strength for
        :param list_players: the list of players
        """
        for p in list_players:
            if player.id == p.id:
                player.strength += 1



