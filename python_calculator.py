import tkinter
from tkinter import messagebox
from tkinter import ttk
from math import sqrt

WINDOW = tkinter.Tk()

ns = [0, 0]
operation = ""
current_number = 0

number_display = tkinter.Label(WINDOW, text="0")

def reset():
    global operation, current_number
    operation = ""
    ns = [0, 0]
    current_number = 0

def equals():
    global operation, current_number

    result = str(eval(f"{ns[0]}{operation}{ns[1]}"))
    number_display["text"] = result

    operation = ""
    ns[0] = result
    current_number = 0

def backspace():
    ns[current_number] = int(str(current_number)[:-1])

def dot():
    pass

PARENT_FRAME = tkinter.Frame(WINDOW)
PARENT_FRAME.pack(fill="both", expand=True)
#frame for the whole window. Holds buttons in place and makes them dinamically resize.

TOP_FRAME = tkinter.Frame(PARENT_FRAME)
number_display.pack(fill="both", expand=True)
TOP_FRAME.pack(fill="both", expand=True)
#Top frame for the number display.

BOTTOM_FRAME = tkinter.Frame(PARENT_FRAME)

class NumberButton(ttk.Button):
    def __init__(self, number):
        self.number = number
        ttk.Button.__init__(self, BOTTOM_FRAME, text=str(number), command=self.change)

    def __repr__(self):
        return f"NumberButton({self.number})"

    def change(self):
        global current_number
        ns[current_number] = ns[current_number] * 10 + self.number
        number_display["text"] = str(ns[current_number])

class ArithmeticButton(ttk.Button):
    def __init__(self, operator):
        self.operator = operator
        ttk.Button.__init__(self, BOTTOM_FRAME, text=operator, command=self.operate)

    def __repr__(self):
        return f"ArithmeticButton({self.operator})"

    def operate(self):
        global operation, current_number
        if current_number == 1:
            equals()
            operation = self.operator
        else:
            operation = self.operator
            current_number = 1
            number_display["text"] = self.operator

def reciprocal():
    global operation

    operation = operation + "1/" + current_number
    equals()

def square():
    global operation

    operation = operation + current_number + "**2"
    equals()

def root():
    global operation

    operation = operation + f"sqrt({current_number})"
    equals()

for r in range(5):
    BOTTOM_FRAME.grid_rowconfigure(r, weight=1)

for c in range(3):
    BOTTOM_FRAME.grid_columnconfigure(c, weight=1)

C_BUTTON = ttk.Button(BOTTOM_FRAME, text="C", command=reset)
CE_BUTTON = ttk.Button(BOTTOM_FRAME, text="CE", command=reset)
BACKSPACE_BUTTON = ttk.Button(BOTTOM_FRAME, text="<", command=backspace)

C_BUTTON.grid(row=0, column=1, sticky="nsew")
CE_BUTTON.grid(row=0, column=2, sticky="nsew")
BACKSPACE_BUTTON.grid(row=0, column=3, sticky="nsew")

DIGIT_BUTTONS = [NumberButton(n) for n in range(1,10)]
ARITHETIC_BUTTONS = [ArithmeticButton(c) for c in ("/", "*", "-", "+")]
EQUAL_BUTTON = ttk.Button(BOTTOM_FRAME, text="=", command=equals)

for r, db in enumerate(ARITHETIC_BUTTONS):
    db.grid(row=r+1, column=3, sticky="nsew")

EQUAL_BUTTON.grid(row=5, column=3, sticky="nsew")

for y in range(3, 0, -1):
    for x in range(3):
        DIGIT_BUTTONS[y * 3 - 3 + x].grid(row=5-y, column=x, sticky="nsew")
#Grids number buttons correspondingly:
#789
#456
#123

ZERO_BUTTON = NumberButton(0)
ZERO_BUTTON.grid(row=5, column=1, sticky="nsew")

DOT_BUTTON = ttk.Button(BOTTOM_FRAME, text=".", command=dot)
DOT_BUTTON.grid(row=5, column=2, sticky="nsew")

RECIPROCAL = ttk.Button(BOTTOM_FRAME, text="1/x", command=reciprocal)
SQUARE = ttk.Button(BOTTOM_FRAME, text="x^2", command=square)
ROOT = ttk.Button(BOTTOM_FRAME, text="v/", command=root)

RECIPROCAL.grid(row=1, column=0, sticky="nsew")
SQUARE.grid(row=1, column=1, sticky="nsew")
ROOT.grid(row=1, column=2, sticky="nsew")

BOTTOM_FRAME.pack(fill="both", expand=True)
#Bottom frame for calculator buttons.

WINDOW.mainloop()
