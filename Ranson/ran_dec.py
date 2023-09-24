from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
import os
#Charger la clé RSA pour le dechiffrement 
with open("private_key.pem", "rb") as private_file:
	private_key = RSA.import_key(private_file.read()) 
	
#Parcourir les fichiers dans le repertoire chiffré
encrypted_directory = "encrypted_files"
for filename in os.listdir(encrypted_directory):
	with open(os.path.join(encrypted_directory, filename), "rb") as encrypted_file:
		enc_aes_key , nonce, tag, ciphertext = [encrypted_file.read(x) for x in(private_key.size_in_bytes(), 16, 16, -1)]
		
	#Dechiffrer la clé AES avec la clé privé RSA
	cipher_rsa = PKCS1_OAEP.new(private_key)
	aes_key = cipher_rsa.decrypt(enc_aes_key)
	
	#Dechiffrer le contenu du fichier avec la clé AES
	cipher_aes = AES.new(aes_key, AES.MODE_EAX, nonce=nonce)
	plaintext = cipher_aes.decrypt_and_verify(ciphertext, tag)
	
	
	with open(os.path.join("decrypted_files", filename), "wb") as decrypted_file:
		decrypted_file.write(plaintext)
print("les fichiers ont ete decrypté et sauvegarder dans le repertoire decrypted_files")
