import tkinter as tk
from datetime import datetime, timedelta


def update_countdown():
    current_time = datetime.now()
    remaining_time = end_time - current_time
    if remaining_time.total_seconds() <= 0:
        label.config(text="Temps écoulé!")
    else:
        countdown = str(remaining_time).split(".")[0]
        label.config(text=countdown)
    root.after(1000, update_countdown)

# Crée une fenêtre Tkinter
root = tk.Tk()
label2 = tk.Label(root, text="your data is encrypted pay me 10 BTCs\n to unlock them!!!", font=('calibri', 10, 'bold'))
label2.pack()
root.title("Ransomware")
root.geometry("500x300")
root.resizable(False, False)


# Calcule l'heure de fin
end_time = datetime.now() + timedelta(hours=6)

# Crée une étiquette pour afficher le compte à rebours
label = tk.Label(root, font=("Helvetica", 48), fg="black", bg='red')
label.pack(pady=20)

# Lance la fonction de mise à jour du compte à rebours
label2 = tk.Label(root, text=" if the runs out your file will be gone!!", font=('calibri', 10, 'bold'))
label2.pack()

update_countdown()

root.mainloop()