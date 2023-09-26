from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
import os

# Charger la clé RSA pour le déchiffrement
with open("private_key.pem", "rb") as private_file:
    private_key = RSA.import_key(private_file.read())

# Spécifier le répertoire source chiffré
encrypted_directory = "C:\\Users\\NWORK 3\\Desktop\\Ranso\\encrypted_files"

# Spécifier le répertoire de destination pour les fichiers déchiffrés
decrypted_directory = "C:\\Users\\NWORK 3\\Desktop\\Ranso\\decrypted_files"

# Créer le répertoire "decrypted_files" s'il n'existe pas
if not os.path.exists(decrypted_directory):
    os.makedirs(decrypted_directory)

# Parcourir les fichiers dans le répertoire chiffré
for filename in os.listdir(encrypted_directory):
    with open(os.path.join(encrypted_directory, filename), "rb") as encrypted_file:
        enc_aes_key, nonce, tag, ciphertext = [encrypted_file.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1)]

    # Déchiffrer la clé AES avec la clé privée RSA
    cipher_rsa = PKCS1_OAEP.new(private_key)
    aes_key = cipher_rsa.decrypt(enc_aes_key)

    # Déchiffrer le contenu du fichier avec la clé AES
    cipher_aes = AES.new(aes_key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher_aes.decrypt_and_verify(ciphertext, tag)

    # Utiliser l'encodage UTF-8 lors de l'écriture des fichiers déchiffrés
    with open(os.path.join(decrypted_directory, filename), "wb") as decrypted_file:
        decrypted_file.write(plaintext)

print("Les fichiers ont été déchiffrés et sauvegardés dans le répertoire decrypted_files")
