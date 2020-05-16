from cryptography.fernet import Fernet
import os
array = os.listdir()
files = []
directory = []
print(array)
for i in range(0, len(array)):
    if os.path.isfile(array[i]):
        files.append(array[i])
    else:
        print(directory.append(array[i]))
