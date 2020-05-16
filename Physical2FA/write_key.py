from cryptography.fernet import Fernet
key = Fernet.generate_key()
with open("D:\key.key", "wb") as key_file:
    key_file.write(key)
