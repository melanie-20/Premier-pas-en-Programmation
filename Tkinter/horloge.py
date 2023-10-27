from tkinter import *
import time

root = Tk()
root.title("Horloge")

timenow = "Hello Gui"

cframe = Frame(root, width=100, height=20, bg="green", relief=GROOVE)
cframe.pack()

clock = Label(cframe, padx=25, pady=40, bd=3, fg="darkgreen", font=("arial", 48, "bold"), text=timenow, bg="lightgreen", relief=SUNKEN)
clock.pack()

def tick():
    global timenow
    newtime = time.strftime("%H:%M:%S %p")
    if newtime != timenow:
        timenow = newtime
        clock.config(text=timenow)
    clock.after(200, tick)

tick()
root.mainloop()
