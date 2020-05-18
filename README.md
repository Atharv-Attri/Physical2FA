# Physical2FA
 
 Install using ```python
 pip install Physical2FA```
 
 **Please read the entire file to prevent data loss**
 **Physical2FA currently only supports Windows 7 and newer**
 Physical2FA encrypts and decrypts your files using an external drive.
 
 It can all be done in 2 lines of code, no more wasting time encrypting and decrypting!
 ```python
 from Physical2FA import encrypt
 encrypt
 ```
 
 It's as easy as that!
 
 #### First time run
 Make sure that you also have cryptography installed. You can install it using 
 ```python
 pip install cryptography
 ```
 When you first run the program, you will need to create a key. You can do this by running
 
 ```Python
 from Physical2FA import write_key
 
 write_key 
 ```
 This will create a file called 'key.key' in your external drive. For this to work, make sure that your external drive has the letter 'D'. you can find out how to change your drive's letter on [Microsoft docs](https://docs.microsoft.com/en-us/windows-server/storage/disk-management/change-a-drive-letter). I highly recommend that you check the specifications section at the end of this doc. 
 
 #### Encryption
 
 Physical2FA will encrypt all the files and subdirectories in the directory that you run the program in. However, it will not encrypt the python file in which you run the program in as long as the file is named 'lock.py'. Physical2FA will only encrypt upto 5 subdirectories, but support for more is in development. What this means that if you look at the following model of a sample directory:
 
 ![Encryption_explanation](https://github.com/Atharv2/Physical2FA/blob/master/encryption_explanation.png?raw=true "Image")
 
Things underlined in green are encrypted. So you can see that files that are nested upto 5 subdirectories are encrypted. 
 
 Here is how to encrypt in steps:
 
1. Create a file named lock.py in the directory that you want to encrypt. It is very important that you name it lock.py, or else you will not be able to decrypt the directory.
2. Now add the following code in the file: 
```python 
from Physical2FA import encrypt

encrypt
```
If it is your first time encrypting, you should also import write_key and add 'write_key' before you encrypt. Once you have a key, it is very important that you **_NEVER_** run write_key again. It will rewrite your key, and you will not be able to recover your files if they are encrypted.

3. Execute the file, and your files/subdirectories should be encrypted.

The encryption is as secure as your external drive is!
#### Decrypt
To decrypt, you run the same code as encryption, but you replace all instaces of 'encrypt' with 'decrypt'. So it would be:
```python
from Physical2FA import decrypt

decrypt
```
#### Using the fail_safe
You can download the file called fail_safe.py from https://github.com/Atharv2/Physical2FA. It will guide you through encrypting or decrypting your files one at a time.

### Very Important Things that you should go through or else you will most likely lose your files!
##### The following lines are a matter of life or death for your files. (No pressure).
+ Make sure that your file is named 'lock.py'. Case does matter! If you don't you will get half decrypted files when you try to decrypt.
+ Make sure that your external drive is the letter 'D'. If it does not, go change it. 
+ Take very good care of your external drive. Physical2FA uses a fernet encryption, and there is no way to recover your key if you lose it. Your key is not stored anywhere other than your drive, so if I were you, I would keep a copy of the key on the cloud. 
+ There is a file on https://github.com/Atharv2/Physical2FA called fail_safe.py which will allow you to encrypt or decrypt single files that the regular program may not have encrypted or decrypted. You will still need your external drive plugged in.
+ I highly recommend that you do not use this to encrypt any important files, although the chances are slim, you may still ruin the files. You can still try to recover it using fail_safe.py, but that is also not a garuntee. 

### Disclaimer
This software does not come with a warranty. I am not responsable if you encrypt some important files and then can't decrypt them. The chances of this happening is very slim, but you should still exercise caution while using this software. I will not be held responsable for any damage that occures from using this software. If you use this program, you understand that You are using it on your own will and you understand the risks. 

#### Physical2FA is licensed under the GNU Lesser General Public License V.3.0
