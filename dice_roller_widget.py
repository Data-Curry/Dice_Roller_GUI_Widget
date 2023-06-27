"""
Dice Roller Widget
"""

from tkinter import *
import random

result_r1 = 1

d4 = [1, 2, 3, 4]
d6 = [1, 2, 3, 4, 5, 6]
d8 = [1, 2, 3, 4, 5, 6, 7, 8]
d10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d12 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
d20 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
d100 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
        41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
        61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
        81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]


def roll_d4():
    # rolls 4-sided die
    r1.delete(1.0)
    d4_result = random.choice(d4)
    r1.insert(END, d4_result)


def roll_d6():
    r1.delete(1.0)
    d6_result = random.choice(d6)
    r1.insert(END, d6_result)


def roll_d8():
    r1.delete(1.0)
    d8_result = random.choice(d8)
    r1.insert(END, d8_result)


def roll_d10():
    r1.delete(1.0)
    d10_result = random.choice(d10)
    r1.insert(END, d10_result)


def roll_d12():
    r1.delete(1.0)
    d12_result = random.choice(d12)
    r1.insert(END, d12_result)


def roll_d20():
    r1.delete(1.0)
    d20_result = random.choice(d20)
    r1.insert(END, d20_result)


def roll_d100():
    r1.delete(1.0)
    d100_result = random.choice(d100)
    r1.insert(END, d100_result)


# Called when radio button clicked
def radio_used():
    sides = radio_state.get()
    return sides


# BUTTON: Roll Dice
def roll():
    r1.delete(1.0, END)
    sides = radio_used()
    if sides == 4:
        roll_d4()
    elif sides == 6:
        roll_d6()
    elif sides == 8:
        roll_d8()
    elif sides == 10:
        roll_d10()
    elif sides == 12:
        roll_d12()
    elif sides == 20:
        roll_d20()
    elif sides == 100:
        roll_d100()


# Create a new window and configurations
window = Tk()
window.title("Dice Roller Widget")
window.minsize(width=300, height=500)

# LABEL: Number of sides
num_of_sides = Label(text="Number of Sides")
num_of_sides.grid(column=0, row=2)

# RADIO BUTTONS: 4, 6, 8, 10, 12, 20, 100
# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="4-sided", value=4, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="6-sided", value=6, variable=radio_state, command=radio_used)
radiobutton3 = Radiobutton(text="8-sided", value=8, variable=radio_state, command=radio_used)
radiobutton4 = Radiobutton(text="10-sided", value=10, variable=radio_state, command=radio_used)
radiobutton5 = Radiobutton(text="12-sided", value=12, variable=radio_state, command=radio_used)
radiobutton6 = Radiobutton(text="20-sided", value=20, variable=radio_state, command=radio_used)
radiobutton7 = Radiobutton(text="100-sided", value=100, variable=radio_state, command=radio_used)
radiobutton1.grid(column=0, row=3)
radiobutton2.grid(column=0, row=4)
radiobutton3.grid(column=0, row=5)
radiobutton4.grid(column=0, row=6)
radiobutton5.grid(column=0, row=7)
radiobutton6.grid(column=0, row=8)
radiobutton7.grid(column=0, row=9)

# Button calls roll() when pressed
roll_button = Button(text="Roll Dice", command=roll)
roll_button.grid(column=0, row=10)

# LABEL: Results (1,0)
result = Label(text="Roll Result")
result.grid(column=1, row=0)
result.config(padx=50, pady=0)

# TEXT BOX
r1 = Text(height=1, width=3)
r1.grid(column=1, row=1)
r1.config(padx=50, pady=0)


window.mainloop()
