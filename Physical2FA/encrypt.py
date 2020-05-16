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
        if array[i] == "encrypt.py":
            array.remove("encrypt.py")
    else:
        print(directory.append(array[i]))
for f in directory:
    if f.startswith('.'):
        directory.remove(f)
        print("one file removed")
def encrypt(filename, key):
    f = Fernet(key)
    try:
        with open(filename, "rb") as file:
            # read all file data
            file_data = file.read()
    except FileNotFoundError:
        print(
            f'There is no file named {filename}\n please make sure that the file exists and that you are including the file extention.')
        exit(1)
    # encrypt data
    encrypted_data = f.encrypt(file_data)
    # write the encrypted file
    with open(filename, "wb") as file:
        file.write(encrypted_data)

for i in files:
    encrypt(i, load_key.open_key())
while 1 < 100:
    for i in directory:
        os.chdir(i)
        array = os.listdir()
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
        print(files)
        print(directory)
        for i in files:
            encrypt(i, load_key.open_key())
        
        for i in directory:
            os.chdir(i)
            array = os.listdir()
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
            print(files)
            print(directory)
        