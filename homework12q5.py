
import time
from graphics import GraphWin, Point, Circle, Text


class Ball:
    def __init__(self, x, y, vx, vy, radius, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = radius
        self.color = color
        self.shape = None

    def draw(self, win):
        self.shape = Circle(
            Point(self.x, self.y),
            self.radius
        )

        self.shape.setFill(self.color)
        self.shape.setOutline(self.color)
        self.shape.draw(win)

    def update(self, dt, gravity, width, height):
        # Gravity changes vertical velocity.
        self.vy -= gravity * dt

        # Update position.
        self.x += self.vx * dt
        self.y += self.vy * dt

        # Bounce off the floor.
        if self.y - self.radius < 0:
            self.y = self.radius
            self.vy = abs(self.vy) * 0.82

        # Bounce off the ceiling.
        elif self.y + self.radius > height:
            self.y = height - self.radius
            self.vy = -abs(self.vy) * 0.82

        # Bounce off the left wall.
        if self.x - self.radius < 0:
            self.x = self.radius
            self.vx = abs(self.vx) * 0.90

        # Bounce off the right wall.
        elif self.x + self.radius > width:
            self.x = width - self.radius
            self.vx = -abs(self.vx) * 0.90

    def move_graphics(self):
        center = self.shape.getCenter()

        self.shape.move(
            self.x - center.getX(),
            self.y - center.getY()
        )


def main():
    width = 600
    height = 400

    gravity = 450
    dt = 0.02

    win = GraphWin(
        "Three Bouncing Balls",
        width,
        height,
        autoflush=False
    )

    # Matching window and coordinate ratios
    # keep the balls round.
    win.setCoords(0, 0, width, height)
    win.setBackground("white")

    # Create three Ball objects.
    balls = [
        Ball(100, 250, 85, 20, 18, "red"),
        Ball(280, 320, -55, 0, 18, "blue"),
        Ball(480, 210, -75, 45, 18, "green")
    ]

    # Draw all three balls.
    for ball in balls:
        ball.draw(win)

    Text(
        Point(width / 2, height - 18),
        "Press q to quit"
    ).draw(win)

    win.update()

    # Keep updating all three balls.
    while True:
        key = win.checkKey()

        if key.lower() == "q":
            break

        for ball in balls:
            ball.update(dt, gravity, width, height)
            ball.move_graphics()

        win.update()
        time.sleep(dt)

    win.close()


if __name__ == "__main__":
    main()
