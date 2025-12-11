class Snake:

    def __init__(self, initial_snake, snake_color, canva):

        self.snake_body = initial_snake
        self.snake_color = snake_color
        self.coordinates = [[0, 250], [250, 0]]
        self.body_parts = []
        self._snake_direction = 'right'
        self.snake_size = 10
        self.canva = canva

        self.draw()

    def set_snake_direction(self, new_direction):
        self._snake_direction = new_direction

    def get_snake_direction(self):
        return self._snake_direction

    def snake_grow(self):
        self.coordinates.append([0, 0])

    def snake_controller(self):
        x, y = self.coordinates[0]

        if self._snake_direction == "up":
            y -= self.snake_size
        elif self._snake_direction == "down":
            y += self.snake_size
        elif self._snake_direction == "left":
            x -= self.snake_size
        elif self._snake_direction == "right":
            x += self.snake_size

        new_coordinates = [x, y]
        self.coordinates.insert(0, new_coordinates)
        self.coordinates.pop()

    def draw(self):
        self.canva.delete("snake")
        self.body_parts.clear()
        for x, y in self.coordinates:
            body_part = self.canva.create_rectangle(
                x, y, x + self.snake_size, y + self.snake_size, fill=self.snake_color, tag='snake')
            self.body_parts.append(body_part)
