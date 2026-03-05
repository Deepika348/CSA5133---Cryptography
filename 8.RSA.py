

# Simple RSA Algorithm
from math import gcd

# Function to find modular inverse
def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# User input for small primes (for demonstration)
p = int(input("Enter prime number p: "))
q = int(input("Enter prime number q: "))

n = p * q
phi = (p - 1) * (q - 1)

# Choose e such that 1 < e < phi and gcd(e, phi) = 1
e = int(input("Enter encryption key e (1<e<phi and coprime to phi): "))
if gcd(e, phi) != 1:
    raise ValueError("e must be coprime with phi(n)")

d = modinv(e, phi)
if d is None:
    raise ValueError("No modular inverse found for given e")

# Encryption
def encrypt(msg):
    return [pow(ord(char), e, n) for char in msg]

# Decryption
def decrypt(cipher):
    return ''.join([chr(pow(char, d, n)) for char in cipher])

# User interaction
choice = input("Type 'E' to encrypt or 'D' to decrypt: ").upper()

if choice == 'E':
    message = input("Enter message to encrypt: ")
    cipher = encrypt(message)
    print("Encrypted:", cipher)
elif choice == 'D':
    cipher_text = input("Enter cipher numbers separated by space: ")
    cipher = list(map(int, cipher_text.split()))
    print("Decrypted:", decrypt(cipher))
else:
    print("Invalid choice!")
