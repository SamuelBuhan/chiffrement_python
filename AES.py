"""
This file aims to implement the AES methode 

"""
import time 

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# create data 
data = b"Example of text encrypt with AES"


# return a random byte string of lenth 16
key = get_random_bytes(16)

# EAX mode provide authentification and privacy of the message simultaniously
# AES takes block of 16 Bytes and create a AES cipher
cipher_encrypt = AES.new(key, AES.MODE_EAX)

starting_time = time.time_ns()
ciphertext, tag = cipher_encrypt.encrypt_and_digest(data)
ending_time = time.time_ns()


print("-"*8 + "Encryption" + "-"*8)
print("Encrypt last:", ending_time - starting_time,"ns")
print("data:", data)
print("data encrypt:", ciphertext)
print("tag:", tag)

# write encrypt data in file 
#file_out = open("encrypted.bin", "wb")
#[ file_out.write(x) for x in (cipher_encrypt.nonce, tag, ciphertext) ]
#file_out.close()

# read file 
#file_in = open("encrypted.bin", "rb")
#nonce, tag, ciphertext = [ file_in.read(x) for x in (16, 16, -1) ]

print("-"*8 + "Decryption" + "-"*8)
# nonce is necessary to decrypt the cipher text
cipher_decrypt = AES.new(key, AES.MODE_EAX, cipher_encrypt.nonce)

starting_time = time.time_ns()
plaint_text = cipher_decrypt.decrypt_and_verify(ciphertext, tag)
ending_time = time.time_ns()
print("Decrypt last:", ending_time - starting_time,"ns")
print("Decrypt data:",plaint_text)

print("Encryption Done!")