
from graphics import GraphWin, Point, Text, Entry, Rectangle
from lcr import LCRGame


class GraphicsInterface:
    def __init__(self):
        self.win = GraphWin("LCR Game", 600, 450)
        self.win.setCoords(0, 0, 600, 450)
        self.win.setBackground("white")

        Text(Point(300, 420), "LEFT CENTER RIGHT").draw(self.win)

        self.players_text = ""
        self.pot_text = "Center pot: 0 chips"
        self.status = ""

    def draw_state(self):
        # Redraw the current game information.
        if hasattr(self, "player_display"):
            self.player_display.undraw()
            self.pot_display.undraw()
            self.status_display.undraw()

        self.player_display = Text(
            Point(300, 340), self.players_text
        )
        self.pot_display = Text(
            Point(300, 290), self.pot_text
        )
        self.status_display = Text(
            Point(300, 220), self.status
        )

        self.player_display.draw(self.win)
        self.pot_display.draw(self.win)
        self.status_display.draw(self.win)

    def get_player_names(self):
        prompt = Text(
            Point(300, 350),
            "Enter number of players (at least 3):"
        )
        entry = Entry(Point(300, 310), 8)
        button = Rectangle(Point(250, 220), Point(350, 260))
        label = Text(Point(300, 240), "Start")

        prompt.draw(self.win)
        entry.draw(self.win)
        button.draw(self.win)
        label.draw(self.win)

        while True:
            self.win.getMouse()
            try:
                count = int(entry.getText())
                if count >= 3:
                    break
            except ValueError:
                pass

            prompt.setText("Enter a number of at least 3")
            entry.setText("")

        prompt.undraw()
        entry.undraw()
        button.undraw()
        label.undraw()

        self.players_text = "Players: " + str(count)
        self.status = "Game started"
        self.draw_state()

        return [f"Player {i + 1}" for i in range(count)]

    def show_players(self, players):
        self.players_text = "   ".join(
            f"{p.name}: {p.chips}" for p in players
        )
        self.draw_state()

    def show_roll(self, player, results):
        self.status = f"{player.name} rolled: {results}"
        self.draw_state()

    def show_pot(self, pot):
        self.pot_text = f"Center pot: {pot.chips} chips"
        self.draw_state()

    def show_message(self, message):
        if message:
            self.status = message
            self.draw_state()
            self.win.getMouse()

    def show_winner(self, player, prize):
        self.status = f"{player.name} WINS! Prize: {prize}"
        self.draw_state()

    def close(self):
        Text(Point(300, 60), "Click to close").draw(self.win)
        self.win.getMouse()
        self.win.close()


def main():
    interface = GraphicsInterface()
    names = interface.get_player_names()

    game = LCRGame(names, interface)
    game.play()


if __name__ == "__main__":
    main()
