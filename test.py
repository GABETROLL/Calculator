import tkinter

W = tkinter.Tk()
F1 = tkinter.Frame(W)
F2 = tkinter.Frame(W)

F1.pack()
F2.pack()

buttons1 = [tkinter.Button(W, text=str(n)) for n in range(2)]
buttons2 = [tkinter.Button(W, text=str(n)) for n in range(2)]

for b in buttons1:
    b.pack(side="right")

for b in buttons2:
    b.pack(side="right")
