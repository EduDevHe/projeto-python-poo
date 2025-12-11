
import tkinter as tk


class Config:

    def __init__(self):

        self.root = tk.Tk()
        # self.root.attributes("-fullscreen", True)
        self.root.title("Snake Game UFOB")
        self.img = tk.PhotoImage(file="assets/gatopitao.png")

        self.SCREEN_WIDTH = 500
        # self.root.winfo_screenwidth()
        self.SCREEN_HEIGHT = 500
        # self.root.winfo_screenheight()

        self.canvas = tk.Canvas(
            self.root,
            width=self.SCREEN_WIDTH,
            height=self.SCREEN_HEIGHT,
            bg="black"
        )
        self.canvas.pack(fill="both", expand=True)

    def game_over(self):
        pass

    def update(self):
        pass

    def run(self):
        self.root.mainloop()
