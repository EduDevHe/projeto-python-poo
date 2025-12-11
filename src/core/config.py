
import tkinter as tk


class Config:

    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes("-fullscreen", True)
        self.root.title("Snake Game UFOB")
        self.SCREEN_WIDTH = self.root.winfo_screenwidth()
        self.SCREEN_HEIGHT = self.root.winfo_screenheight()

        self.canvas = tk.Canvas(
            self.root,
            width=self.SCREEN_WIDTH,
            height=self.SCREEN_HEIGHT,
            bg="black"
        )
        self.canvas.pack(fill="both", expand=True)

    def run(self):
        self.root.mainloop()
