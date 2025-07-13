from pprint import pprint

from src.services import Service


class UI(Service):
    def __init__(self, service: Service = Service):
        super().__init__()
        self._service = service

    def main(self):
        sorted_players = sorted(self._service.get_all_players().values(), key=lambda x: x.strength, reverse=True)
        print("PLAYERS:")
        pprint(sorted_players)
        print("\n")

        while True:
            if self._service.is_power_of_2(sorted_players):
                if len(sorted_players) == 1:
                    print(f"\nWINNER: {sorted_players}")
                    break

                else:
                    winners = []
                    pairs = self._service.pairs(sorted_players)
                    print(f"\nLast {len(sorted_players)} players")
                    for p in range(len(pairs)):
                        print("\nPlayer 1   vs   Player 2")
                        print(f"Player 1 = {pairs[p][0]}")
                        print(f"Player 2 = {pairs[p][1]}")
                        winner = int(input("Choose who wins: "))
                        if winner == 1:
                            winners.append(pairs[p][0])
                            loser = pairs[p][1]
                        elif winner == 2:
                            winners.append(pairs[p][1])
                            loser = pairs[p][0]

                        for player in sorted_players:
                            if player == loser:
                                sorted_players.remove(player)

            else:
                winners = []
                games_to_play = len(sorted_players) - self.closest_power_of_2(sorted_players)
                x = games_to_play * 2
                print(f"Games to play: {games_to_play} ---> {x} players\n")
                players_to_play = sorted_players[-x:].copy()
                pairs = self._service.pairs(players_to_play)
                print(f"QUALIFICATION")
                for p in range(len(pairs)):
                    print("\nPlayer 1   vs   Player 2")
                    print(f"Player 1 = {pairs[p][0]}")
                    print(f"Player 2 = {pairs[p][1]}")
                    winner = int(input("Choose who wins: "))

                    if winner == 1:
                        winners.append(pairs[p][0])
                        loser = pairs[p][1]

                    elif winner == 2:
                        winners.append(pairs[p][1])
                        loser = pairs[p][0]

                    for player in sorted_players:
                        if player == loser:
                            sorted_players.remove(player)
