from cryptography.fernet import Fernet
import os
import sys
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
