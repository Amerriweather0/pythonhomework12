
from graphics import GraphWin, Point, Text, Entry, Rectangle
from ship_captain_crew import ShipCaptainCrewGame


class GraphicsInterface:
    def __init__(self):
        self.win = GraphWin(
            "Ship Captain and Crew", 650, 450
        )

        self.win.setCoords(0, 0, 650, 450)
        self.win.setBackground("white")

        Text(
            Point(325, 420),
            "SHIP - CAPTAIN - CREW"
        ).draw(self.win)

        Text(
            Point(325, 390),
            "6 = Ship    5 = Captain    4 = Crew"
        ).draw(self.win)

        self.players_text = ""
        self.status = ""

    def draw_state(self):
        self.status_area.undraw()
        self.players_area.undraw()

        self.status_area = Text(
            Point(325, 220), self.status
        )

        self.players_area = Text(
            Point(325, 300), self.players_text
        )

        self.status_area.draw(self.win)
        self.players_area.draw(self.win)

        self.win.update()

    def get_player_names(self):
        prompt = Text(
            Point(325, 350),
            "Enter number of players (at least 2):"
        )

        entry = Entry(Point(325, 310), 8)

        button = Rectangle(
            Point(275, 220),
            Point(375, 260)
        )

        label = Text(Point(325, 240), "Start")

        prompt.draw(self.win)
        entry.draw(self.win)
        button.draw(self.win)
        label.draw(self.win)

        while True:
            self.win.getMouse()

            try:
                count = int(entry.getText())

                if count >= 2:
                    break

            except ValueError:
                pass

            prompt.setText("Enter at least 2 players")
            entry.setText("")

        prompt.undraw()
        entry.undraw()
        button.undraw()
        label.undraw()

        self.players_text = "Players: " + str(count)
        self.status = "Game started"

        self.status_area = Text(
            Point(325, 220), self.status
        )

        self.players_area = Text(
            Point(325, 300), self.players_text
        )

        self.status_area.draw(self.win)
        self.players_area.draw(self.win)

        return [
            f"Player {i + 1}"
            for i in range(count)
        ]

    def show_players(self, players):
        self.players_text = "   ".join(
            f"{p.name}: {p.score}"
            for p in players
        )

        self.draw_state()

    def show_roll(self, player, results):
        self.status = f"{player.name} rolled: {results}"
        self.draw_state()

    def show_pot(self, pot):
        self.status = f"Center pot: {pot.chips}"
        self.draw_state()

    def show_message(self, message):
        if message:
            self.status = message + " (click to continue)"
            self.draw_state()

            self.win.getMouse()

            self.status = message
            self.draw_state()

    def show_winner(self, player, prize=None):
        self.status = (
            f"{player.name} WINS with {player.score} points!"
        )

        self.draw_state()

    def close(self):
        Text(
            Point(325, 50),
            "Click to close"
        ).draw(self.win)

        self.win.getMouse()
        self.win.close()


def main():
    interface = GraphicsInterface()
    names = interface.get_player_names()

    game = ShipCaptainCrewGame(names, interface)
    game.play()


if __name__ == "__main__":
    main()
