import hashlib
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

msg = "CyberSecurityLab2026"

sha = hashlib.sha256(msg.encode()).hexdigest()

key = get_random_bytes(16)
aes = AES.new(key, AES.MODE_EAX)
ciphertext, tag = aes.encrypt_and_digest(msg.encode())
dec = AES.new(key, AES.MODE_EAX, nonce=aes.nonce).decrypt(ciphertext).decode()

rsa_key = RSA.generate(2048)
rsa_enc = PKCS1_OAEP.new(rsa_key.publickey()).encrypt(msg.encode())
rsa_dec = PKCS1_OAEP.new(rsa_key).decrypt(rsa_enc).decode()

print(f"Original Text: {msg}\n")
print("=== SHA-256 HASH ===")
print(f"Hash: {sha}\n")
print("=== AES ENCRYPTION ===")
print(f"Ciphertext (Hex): {ciphertext.hex()}")
print(f"Decrypted: {dec}\n")
print("=== RSA ENCRYPTION ===")
print(f"Ciphertext (Hex): {rsa_enc[:32].hex()}...")
print(f"Decrypted: {rsa_dec}")
