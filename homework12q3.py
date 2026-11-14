
import random


class Die:
    def roll(self):
        return random.randint(1, 6)


class DiceCup:
    def __init__(self):
        self.dice = [Die() for i in range(5)]

    def roll_available(self, number):
        return [self.dice[i].roll() for i in range(number)]


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0


class TextInterface:
    def get_player_names(self):
        count = int(input("Number of players (at least 2): "))

        while count < 2:
            count = int(input("Enter at least 2 players: "))

        names = []

        for i in range(count):
            name = input(f"Player {i + 1} name: ")
            names.append(name or f"Player {i + 1}")

        return names

    def show_players(self, players):
        print("\nScores:")
        for player in players:
            print(player.name, ":", player.score)

    def show_roll(self, player, results):
        print(player.name, "rolled:", results)

    def show_pot(self, pot):
        pass

    def show_message(self, message):
        if message:
            print(message)

    def show_winner(self, player, prize=None):
        print(f"\n{player.name} wins with {player.score} points!")

    def close(self):
        print("Game over!")


class ShipCaptainCrewGame:
    def __init__(self, names, interface):
        self.players = [Player(name) for name in names]
        self.interface = interface
        self.cup = DiceCup()

    def take_turn(self, player):
        ship = False
        captain = False
        crew = False
        score = 0

        for roll_number in range(1, 4):
            locked = int(ship) + int(captain) + int(crew)
            dice_to_roll = 5 - locked

            results = self.cup.roll_available(dice_to_roll)
            available = results[:]

            self.interface.show_roll(player, results)

            # Find the Ship (6).
            if not ship and 6 in available:
                available.remove(6)
                ship = True

            # Find the Captain (5).
            if ship and not captain and 5 in available:
                available.remove(5)
                captain = True

            # Find the Crew (4).
            if ship and captain and not crew and 4 in available:
                available.remove(4)
                crew = True

            if ship and captain and crew:
                score = sum(available)

            self.interface.show_message(
                f"Roll {roll_number}: "
                f"Ship={ship}, Captain={captain}, Crew={crew}, "
                f"Score={score}"
            )

        if not (ship and captain and crew):
            score = 0

        player.score = score

        self.interface.show_message(
            f"{player.name}'s final score: {score}"
        )

    def play(self):
        contenders = self.players[:]
        round_number = 1

        while len(contenders) > 1:
            self.interface.show_message(
                f"\nRound {round_number}"
            )

            for player in contenders:
                self.take_turn(player)

            self.interface.show_players(contenders)

            highest = max(p.score for p in contenders)

            contenders = [
                p for p in contenders
                if p.score == highest
            ]

            if len(contenders) > 1:
                self.interface.show_message(
                    "Tie! The tied players play again."
                )

            round_number += 1

        winner = contenders[0]

        self.interface.show_winner(winner)
        self.interface.close()


def main():
    interface = TextInterface()
    names = interface.get_player_names()

    game = ShipCaptainCrewGame(names, interface)
    game.play()


if __name__ == "__main__":
    main()
