from cryptography.fernet import Fernet
import os
import sys
import load_key
orignialdir = os.getcwd()
print(orignialdir)
path = "./"
array = os.listdir(path)
if input(f"you will decrypt the following files: {array}. Are you sure you want to continue? y/n: ") == "y":
    pass
else:
    sys.exit("User raised exception")
files = []
directory = []

print(array)
for i in range(0, len(array)):
    if os.path.isfile(array[i]):
        files.append(array[i])
    else:
        print(directory.append(array[i]))
for f in directory:
    if f.startswith('.') or f == "__pycache__" or f == "encrypt.py":
        directory.remove(f)
        print("one file removed")


def backdecrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)


def encrypt(key):
    for i in files:
        backdecrypt(i, key)

    for g in directory:
        os.chdir(g)
        array = os.listdir()
        print("array!!!!!11111", array)
        filess = []
        directorys = []
        for i in range(0, len(array)):
            if os.path.isfile(array[i]):
                filess.append(array[i])
            else:
                print(directorys.append(array[i]))
        encrypt(load_key.open_key())
        os.chdir(orignialdir)


encrypt(load_key.open_key())
