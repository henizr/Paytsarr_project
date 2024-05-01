import tkinter as tk
from scr_bright_contr import *

class Bright(tk.Tk):
    STYLES : dict = {
        "ice" : { #the name of the first theme
            "buttons" : {
                "bg" : "#8458B3",
                "fg" : "#e5eaf5"
            },
            "two_buttons" : {
                "bg" : "#d0bdf4",
                "fg" : "#8458B3"
            }
         }
    }
    def __init__(self) -> None:
        super().__init__()
        self.title("Bright control v.0.0.1")
        self.geometry("285x100")
        self.configure(bg="#a28089")

        for i, lbl in zip(range(0, 271, 30), range(10, 91, 10)):
            button = tk.Button(
                self, 
                text=str(lbl), 
                width=2, 
                height=1,
                bg=Bright.STYLES.get("ice").get("buttons").get("bg"),
                fg=Bright.STYLES.get("ice").get("buttons").get("fg"),
                command= lambda cur_val = lbl : ScreenBrightnessControl.set_brightness_to_specific_percent(cur_val)         
            )
            button.place(x=i + 10, y=15)
        
        for i, bright_data in enumerate((("մութ", 0), ("լույս", 50))):
            btn_text, btn_percent = bright_data
            button = tk.Button(
                self, 
                text=btn_text, 
                width=8, 
                height=1,
                bg=Bright.STYLES.get("ice").get("two_buttons").get("bg"),
                fg=Bright.STYLES.get("ice").get("two_buttons").get("fg"),
                font=("Verdana", 10),
                command= lambda cur_val = btn_percent : ScreenBrightnessControl.set_brightness_to_specific_percent(cur_val)         
            )
            button.place(x=i * 100 + 100, y=55)

        self.mainloop()

window = Bright()
