import random


class Food:

    def __init__(self, canva, screen_width, screen_height):

        self.food_size = 10
        self.canva = canva
        self.food_color = 'red'
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.coordinates = []
        self.draw()

    def draw(self):

        x = random.randint(0,
                           (self.screen_width // self.food_size) - 1) * self.food_size

        y = random.randint(
            0, (self.screen_height // self.food_size)-1) * self.food_size

        self.canva.create_oval(x, y, x + self.food_size,
                               y + self.food_size, fill=self.food_color, tag="food")

        self.coordinates = (x, y)

    def delet_food(self):
        self.canva.delete("food")
