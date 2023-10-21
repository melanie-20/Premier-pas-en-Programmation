import tkinter as tk

root = tk.Tk()
fontFamily = ('monospace', 25)
btnFontSize = 50

output = tk.Label(root, fg="#FF595E", font=fontFamily, width=20)
output.grid(row=0, column=0, columnspan=4)

def add_txt(char):
   current_text = output["text"]
   if current_text == "0":
       output["text"] = char
   else:
       output["text"] += char

def clear_txt():
   output["text"] = "0"

def calcul_txt():
   try:
       result = str(eval(output["text"]))
       output["text"] = result
   except Exception as e:
       output["text"] = "Error"

tk.Button(root, text="1", font=fontFamily, command=lambda: add_txt("1")).grid(row=1, column=0)
tk.Button(root, text="2", font=fontFamily, command=lambda: add_txt('2')).grid(row=1, column=1)
tk.Button(root, text="3", font=fontFamily, command=lambda: add_txt('3')).grid(row=1, column=2)
tk.Button(root, text="4", font=fontFamily, command=lambda: add_txt("4")).grid(row=2, column=0)
tk.Button(root, text="5", font=fontFamily, command=lambda: add_txt("5")).grid(row=2, column=1)
tk.Button(root, text="6", font=fontFamily, command=lambda: add_txt("6")).grid(row=2, column=2)
tk.Button(root, text="7", font=fontFamily, command=lambda: add_txt('7')).grid(row=3, column=0)
tk.Button(root, text="8", font=fontFamily, command=lambda: add_txt('8')).grid(row=3, column=1)
tk.Button(root, text="9", font=fontFamily, command=lambda: add_txt('9')).grid(row=3, column=2)
tk.Button(root, text="C", font=fontFamily, command=clear_txt).grid(row=4, column=0)
tk.Button(root, text="0", font=fontFamily, command=lambda: add_txt("0")).grid(row=4, column=1)
tk.Button(root, text="=", font=fontFamily, command=calcul_txt).grid(row=4, column=2)
tk.Button(root, text="+", font=fontFamily, command=lambda: add_txt("+")).grid(row=1, column=3)
tk.Button(root, text="-", font=fontFamily, command=lambda: add_txt("-")).grid(row=2, column=3)
tk.Button(root, text="*", font=fontFamily, command=lambda: add_txt("*")).grid(row=3, column=3)
tk.Button(root, text="/", font=fontFamily, command=lambda: add_txt("/")).grid(row=4, column=3)

root.mainloop()
