from cryptography.fernet import Fernet
import os
import sys
path = "./"
pubkey = open("D:\key.key", "rb").read()
array = os.listdir(path)
if input(f"you will decrypt the following files: {array}. Are you sure you want to continue? y/n: ") == "y":
    pass
else:
    sys.exit("User raised exception")
files = []
directory = []


print(array)
for i in range(0, (len(array)-1)):
    if os.path.isfile(array[i]):
        files.append(array[i])
        if array[i] == "lock.py":
            array.remove("lock.py")
            files.remove("lock.py")
    else:
        print(directory.append(array[i]))
for f in directory:
    if f.startswith('.') or f.startswith("_"):
        directory.remove(f)
        print("one file removed")


def decrypt(filename, key):
    f = Fernet(key)
    try:
        with open(filename, "rb") as file:
            # read the encrypted data
            encrypted_data = file.read()
    except FileNotFoundError:
        print(f'File {filename} not decrypted')
        pass
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)


for i in files:
    decrypt(i, pubkey)

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
        decrypt(j, pubkey)
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
            decrypt(k, pubkey)
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
            for l in files:
                decrypt(l, pubkey)
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
                    decrypt(m, pubkey)
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
                        decrypt(n, pubkey)
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
