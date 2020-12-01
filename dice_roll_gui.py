import random
from tkinter import *


root = Tk()

root.geometry("1920x1200")
l1 = Label(root,
           fg="white",
           bg="black",
           width=1920,
           height=1200,
           font=('times', 200))


def dice_roll():
    """
    Dice roll
    """
    number = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    l1.config(text=f'{random.choice(number)}{random.choice(number)}')
    l1.pack(pady=10, padx=10)


b1 = Button(root, text='Roll the Die', relief=RAISED, command=dice_roll)
b1.place(x=880, y=0)

root.mainloop()
