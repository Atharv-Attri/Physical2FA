from cryptography.fernet import Fernet
import os
import sys
path = "./"
pubkey = open("D:\key.key", "rb").read()
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
        if array[i] == "lock.py":
            array.remove("lock.py")
    else:
        print(directory.append(array[i]))
for f in directory:
    if f.startswith('.') or f.startswith("_"):
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
    encrypt(i, pubkey)

for i in directory:
    os.chdir(i)
    array = os.listdir()
    files = []
    directory = []

    print(array)
    for i in array:
        if os.path.isfile(i):
            files.append(i)
            if i == "encrypt.py":
                array.remove("encrypt.py")
        else:
            print(directory.append(i))
    for f in directory:
        if f.startswith('.'):
            directory.remove(f)
            print("one file removed")
    print(files)
    print(directory)
    for j in files:
        encrypt(j, pubkey)
    for j in directory:
        os.chdir(j)
        array = os.listdir()
        files = []
        directory = []

        print(array)
        for j in array:
            if os.path.isfile(j):
                files.append(j)
                if j == "encrypt.py":
                    array.remove("encrypt.py")
            else:
                print(directory.append(i))
        for j in directory:
            if j.startswith('.'):
                directory.remove(j)
                print("one file removed")
        print(files)
        print(directory)
            #NEXT
        for k in files:
            encrypt(k, pubkey)
        for k in directory:
            os.chdir(k)
            array = os.listdir()
            files = []
            directory = []

            print(array)
            for k in array:
                if os.path.isfile(k):
                    files.append(k)
                    if k == "encrypt.py":
                        array.remove("encrypt.py")
                else:
                    print(directory.append(k))
            for k in directory:
                if k.startswith('.'):
                    directory.remove(k)
                    print("one file removed")
            print(files)
            print(directory)
        #NEXT
            for l in directory:
                os.chdir(l)
                array = os.listdir()
                files = []
                directory = []

                print(array)
                for l in array:
                    if os.path.isfile(l):
                        files.append(l)
                        if l == "encrypt.py":
                            array.remove("encrypt.py")
                    else:
                        print(directory.append(l))
                for f in directory:
                    if f.startswith('.'):
                        directory.remove(f)
                        print("one file removed")
                print(files)
                print(directory)
                for m in files:
                    encrypt(m, pubkey)
                for m in directory:
                    os.chdir(m)
                    array = os.listdir()
                    files = []
                    directory = []

                    print(array)
                    for m in array:
                        if os.path.isfile(m):
                            files.append(m)
                            if m == "encrypt.py":
                                array.remove("encrypt.py")
                        else:
                            print(directory.append(i))
                    for f in directory:
                        if f.startswith('.'):
                            directory.remove(f)
                            print("one file removed")
                    print(files)
                    print(directory)
                    for n in files:
                        encrypt(n, pubkey)
                    for n in directory:
                        os.chdir(n)
                        array = os.listdir()
                        files = []
                        directory = []
                    
                        print(array)
                        for i in array:
                            if os.path.isfile(i):
                                files.append(i)
                                if i == "encrypt.py":
                                    array.remove("encrypt.py")
                            else:
                                print(directory.append(i))
                        for f in directory:
                            if f.startswith('.'):
                                directory.remove(f)
                                print("one file removed")
                        print(files)
                        print(directory)
                    