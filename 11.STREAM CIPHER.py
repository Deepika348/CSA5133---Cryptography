# RC4 Stream Cipher Implementation

def rc4(key, text):
    S = list(range(256))
    j = 0
    key = [ord(c) for c in key]

    # Key Scheduling Algorithm (KSA)
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    i = j = 0
    result = ""

    # Pseudo Random Generation Algorithm (PRGA)
    for char in text:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        k = S[(S[i] + S[j]) % 256]
        result += chr(ord(char) ^ k)

    return result


key = input("Enter key: ")
plaintext = input("Enter plaintext: ")

# Encryption
ciphertext = rc4(key, plaintext)
print("Encrypted text:", ciphertext)

# Decryption
decrypted = rc4(key, ciphertext)
print("Decrypted text:", decrypted)
