from tkinter import *
import tkintermapview

win = Tk()
win.geometry("500x440")
win.title("Ma carte")
win.iconbitmap("carte-localisation.ico")
win.resizable(False, False)

label = LabelFrame(win)
label.pack(pady=20)

map_widget = tkintermapview.TkinterMapView(label, width=1500, height=800)
map_widget.set_position(40.73010, -73.935242)
map_widget.set_zoom(10)

map_widget.pack()

win.mainloop()
