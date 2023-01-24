import secrets
import random
import sys
from Crypto.Cipher import AES
from Crypto import Random
import hybrid 
from hybrid import *
import ast 

def decrypt(pk, ciphertext):
    d, n = pk
    m = [chr((int(char) ** d) % n) for char in ciphertext]
    return m

def decryptAES(cipherAESd,cipherText):
    dec= cipherAESd.decrypt(cipherText).decode('utf-8')
    return dec

def unpad(entry):
    up=entry.find('[')
    return entry[:up]



print('Welcome to Student Nest Platform, Please enter the details to decrypt the file')
print()
pri=input("Enter the Private Key: ")
liste = pri.split(', ')
list1 = []
list1.append(int(liste[0]))
list1.append(int(liste[1]))
priv=(list1[0], list1[1])

cipherKey=input("Enter the AES Symmetric Key: ")   # "[1,2,3]"


cipherText=b'\xe3\t\x13\xb6\xfe9.\xd4/\xac\x19&k\xca\x98\x0cw\xdb\x82\xd2DQV\xf7\x82\x08\xfb\xef\xba\xde\x018'
listed = ast.literal_eval(cipherKey)


decriptedKey=''.join(decrypt(priv,listed))
print()
print("Decrypting the AES Symmetric Key...")

cipherAESd = AES.new(decriptedKey.encode(), AES.MODE_ECB)
decrypted=decryptAES(cipherAESd,cipherText)
decrypted=unpad(decrypted)
print()
print("Decrypting the message using the AES symmetric key.....")
print("decrypted message: ", decrypted)