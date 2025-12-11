class Food:
    def __init__(self):
        
        x = random.randint(0,
        (WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (HEIGHT / SPACE_SIZE)-1)* SPACE_SIZE

        self.coordinates = [x, y]

    def draw():
        canva.create_oval(x, y, z + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD, tag="food")