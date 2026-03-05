 

# Simple Diffie-Hellman

p = int(input("Enter prime number (p): "))
g = int(input("Enter primitive root (g): "))

a = int(input("Enter private key of A: "))
b = int(input("Enter private key of B: "))

# Public keys
A = pow(g, a, p)
B = pow(g, b, p)

# Shared key
key = pow(B, a, p)

print("Shared Secret Key:", key)

choice = input("Enter E for Encryption or D for Decryption: ").upper()

if choice == 'E':
    msg = input("Enter message: ")
    enc = ''.join(chr(ord(i) + key) for i in msg)
    print("Encrypted:", enc)

elif choice == 'D':
    msg = input("Enter encrypted message: ")
    dec = ''.join(chr(ord(i) - key) for i in msg)
    print("Decrypted:", dec)

else:
    print("Invalid choice")
