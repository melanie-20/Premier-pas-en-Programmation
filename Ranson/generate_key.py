from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

#Generation de la paire de clés RSA
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()#Generation de la clé AES

aes_key = get_random_bytes(16)


with open("private_key.pem", "wb") as private_file:
    private_file.write(private_key)

with open("public_key.pem", "wb") as public_file:
    public_file.write(public_key)


with open("aes_key.bin", "wb") as aes_file:
    aes_file.write(aes_key)

print("done")
