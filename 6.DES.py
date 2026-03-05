from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

key = b'8bytekey'
cipher = DES.new(key, DES.MODE_ECB)

choice = input("Enter E for Encryption or D for Decryption: ")

if choice.upper() == "E":
    msg = input("Enter message: ")
    enc = cipher.encrypt(pad(msg.encode(), DES.block_size))
    print("Encrypted:", enc)

elif choice.upper() == "D":
    msg = input("Enter encrypted message: ")
    dec = cipher.decrypt(eval(msg))
    print("Decrypted:", unpad(dec, DES.block_size).decode())

else:
    print("Invalid choice")
