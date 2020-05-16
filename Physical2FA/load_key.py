from cryptography.fernet import Fernet

def open_key():
    return open("D:\key.key", "rb").read()

