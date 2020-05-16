from cryptography.fernet import Fernet
import os
import sys
import load_key
path = "./"
array = os.listdir(path)
if input(f"you will encrypt the following files: {array}. Are you sure you want to continue? y/n: ") =="y":
    pass
else:sys.exit("User raised exception")
files = []
directory = []

print(array)
for i in range(0, len(array)):
    if os.path.isfile(array[i]):
        files.append(array[i])
    else:
        print(directory.append(array[i]))
for f in directory:
    if f.startswith('.'):
        directory.remove(f)
        print("one file removed")
def backencrypt(filename, key):
    f = Fernet(key)
    try:
        with open(filename, "rb") as file:
            # read all file data
            file_data = file.read()
    except FileNotFoundError:
        print(
            f'There is no file named {filename}\n please make sure that the file exists and that you are including the file extention.')
        pass
    # encrypt data
    encrypted_data = f.encrypt(file_data)
    # write the encrypted file
    with open(filename, "wb") as file:
        file.write(encrypted_data)
def encrypt(key):
    for i in files:
        backencrypt(i, key)
    
    for g in directory:
        os.chdir(g)
        array = os.listdir()
        print("array!!!!!11111" ,array)
        filess = []
        directorys = []
        for i in range(0, len(array)):
            if os.path.isfile(array[i]):
                filess.append(array[i])
            else:
                print(directorys.append(array[i]))
        encrypt(load_key.open_key())


encrypt(load_key.open_key())
