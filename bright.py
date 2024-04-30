import tkinter as tk

class Bright(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("")
        self.geometry("285x100")

        for i, lbl in zip(range(0, 271, 30), range(10, 91, 10)):
            button = tk.Button(self, text=str(lbl), width=2, height=1)
            button.place(x=i + 10, y=15)

        self.mainloop()

window = Bright()
