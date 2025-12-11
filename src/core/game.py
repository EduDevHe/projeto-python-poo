
from .config import Config
from src.sprites.snake import Snake


class Game(Config):
    def __init__(self):
        super().__init__()

        self.snake = Snake(2, 'green', self.canvas)

        self.bind_keys()
        self.update()

        self.run()

    def bind_keys(self):
        self.root.bind("<Up>", lambda e: self.change_direction("up"))
        self.root.bind("<Down>", lambda e: self.change_direction("down"))
        self.root.bind("<Left>", lambda e: self.change_direction("left"))
        self.root.bind("<Right>", lambda e: self.change_direction("right"))

    def change_direction(self, new_direction):
        opposite = {
            "up": "down",
            "down": "up",
            "left": "right",
            "right": "left"
        }

        if new_direction != opposite[self.snake.get_snake_direction()]:
            self.snake.set_snake_direction(new_direction)

    def update(self):
        self.snake.move()
        self.snake.draw()
        self.root.after(150, self.update)
