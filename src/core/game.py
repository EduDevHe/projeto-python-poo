
from .config import Config
from src.sprites.snake import Snake
from src.sprites.food import Food


class Game(Config):

    def __init__(self):
        super().__init__()

        self.snake = Snake(2, 'green', self.canvas)
        self.food = Food(self.canvas, self.SCREEN_WIDTH, self.SCREEN_HEIGHT)

        self.speed = 2
        self.score = 0
        self.bind_keys()

        self.update()

    def bind_keys(self):
        self.root.bind("<Up>", lambda e: self.change_direction("up"))
        self.root.bind("<Down>", lambda e: self.change_direction("down"))
        self.root.bind("<Left>", lambda e: self.change_direction("left"))
        self.root.bind("<Right>", lambda e: self.change_direction("right"))

    def check_colision(self):

        food_x, food_y = self.food.coordinates
        snake_x, snake_y = self.snake.coordinates[0]

        if (food_x, food_y) == (snake_x, snake_y):
            self.speed += 1
            self.score += 1
            self.food.delet_food()
            self.snake.snake_grow()
            self.food.draw()

    def change_direction(self, new_direction):
        opposite = {
            "up": "down",
            "down": "up",
            "left": "right",
            "right": "left"
        }

        if new_direction != opposite[self.snake.get_snake_direction()]:
            self.snake.set_snake_direction(new_direction)

    def wrap_position(self):

        x, y = self.snake.coordinates[0]

        if x < 0:
            x = self.SCREEN_WIDTH - self.snake.snake_size
        elif x >= self.SCREEN_WIDTH:
            x = 0

        if y < 0:
            y = self.SCREEN_HEIGHT - self.snake.snake_size
        elif y >= self.SCREEN_HEIGHT:
            y = 0

        self.snake.coordinates.insert(0, (x, y))
        self.snake.coordinates.pop()

    def game_over(self):

        self.canvas.delete("all")

        self.canvas.create_image(0, 0, image=self.img, anchor="nw")
        self.canvas.create_text(
            self.SCREEN_WIDTH / 2,
            self.SCREEN_HEIGHT / 2,
            text="COMIDINHA BOA, VLW FLW",
            fill="red",
            font=("Arial", 20)
        )

    def update(self):

        self.snake.snake_controller()

        self.snake.draw()

        self.check_colision()
        self.wrap_position()
        self.root.after(400//self.speed, self.update)
        if self.score == 20:
            self.game_over()
