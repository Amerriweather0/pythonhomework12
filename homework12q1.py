
import random


class Die:
    """An LCR die."""

    def roll(self):
        return random.choice(["L", "C", "R", ".", ".", "."])


class Player:
    def __init__(self, name):
        self.name = name
        self.chips = 3


class Pot:
    def __init__(self):
        self.chips = 0

    def add_chip(self):
        self.chips += 1


class TextInterface:
    def get_player_names(self):
        count = int(input("Number of players (at least 3): "))
        while count < 3:
            count = int(input("Enter at least 3 players: "))

        names = []
        for i in range(count):
            name = input(f"Player {i + 1} name: ")
            names.append(name or f"Player {i + 1}")
        return names

    def show_players(self, players):
        for player in players:
            print(player.name, ":", player.chips, "chips")

    def show_roll(self, player, results):
        print(player.name, "rolled:", results)

    def show_pot(self, pot):
        print("Center pot:", pot.chips)

    def show_message(self, message):
        print(message)

    def show_winner(self, player, prize):
        print(player.name, "wins and receives", prize, "chips!")

    def close(self):
        print("Game over!")


class LCRGame:
    def __init__(self, names, interface):
        self.players = [Player(name) for name in names]
        self.interface = interface
        self.pot = Pot()
        self.dice = [Die(), Die(), Die()]
        self.last_player = self.players[0]

    def play(self):
        current = 0

        while sum(p.chips > 0 for p in self.players) > 1:
            player = self.players[current]

            if player.chips > 0:
                self.last_player = player
                number = min(player.chips, 3)

                results = [
                    self.dice[i].roll()
                    for i in range(number)
                ]

                self.interface.show_roll(player, results)

                for result in results:
                    if result == "L":
                        player.chips -= 1
                        self.players[
                            (current - 1) % len(self.players)
                        ].chips += 1

                    elif result == "R":
                        player.chips -= 1
                        self.players[
                            (current + 1) % len(self.players)
                        ].chips += 1

                    elif result == "C":
                        player.chips -= 1
                        self.pot.add_chip()

                self.interface.show_players(self.players)
                self.interface.show_pot(self.pot)

            current = (current + 1) % len(self.players)

        winner = next(
            (p for p in self.players if p.chips > 0),
            self.last_player
        )

        prize = self.pot.chips
        winner.chips += prize

        self.interface.show_winner(winner, prize)
        self.interface.close()


def main():
    interface = TextInterface()
    names = interface.get_player_names()

    game = LCRGame(names, interface)
    game.play()


if __name__ == "__main__":
    main()
