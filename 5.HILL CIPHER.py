

import numpy as np

# Key matrix
key = np.array([[3, 3],
                [2, 5]])

def mod_inverse(a):
    for i in range(26):
        if (a * i) % 26 == 1:
            return i

def encrypt(text):
    text = text.upper().replace(" ", "")
    if len(text) % 2 != 0:
        text += 'X'
    result = ""
    for i in range(0, len(text), 2):
        p = [[ord(text[i]) - 65], [ord(text[i+1]) - 65]]
        r = np.dot(key, p) % 26
        result += chr(r[0][0] + 65) + chr(r[1][0] + 65)
    return result

def decrypt(cipher):
    det = int(np.linalg.det(key)) % 26
    inv_det = mod_inverse(det)
    adj = np.array([[key[1][1], -key[0][1]],
                    [-key[1][0], key[0][0]]])
    key_inv = (inv_det * adj) % 26
    result = ""
    for i in range(0, len(cipher), 2):
        c = [[ord(cipher[i]) - 65], [ord(cipher[i+1]) - 65]]
        r = np.dot(key_inv, c) % 26
        result += chr(int(r[0][0]) + 65) + chr(int(r[1][0]) + 65)
    return result

# Main program
choice = input("Enter E to Encrypt or D to Decrypt: ")
text = input("Enter text: ")

if choice.upper() == 'E':
    print("Encrypted Text:", encrypt(text))
elif choice.upper() == 'D':
    print("Decrypted Text:", decrypt(text))
else:
    print("Invalid choice")
