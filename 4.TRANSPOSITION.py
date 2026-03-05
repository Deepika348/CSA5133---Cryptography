

# Transposition Cipher
def encrypt(text, key):
    ciphertext = [''] * key
    for i, char in enumerate(text):
        ciphertext[i % key] += char
    return ''.join(ciphertext)

def decrypt(cipher, key):
    n = len(cipher)
    cols = key
    rows = n // cols + (n % cols != 0)
    extra = (cols * rows) - n
    plaintext = [''] * rows
    index = 0
    for col in range(cols):
        length = rows - 1 if col >= cols - extra else rows
        for row in range(length):
            plaintext[row] += cipher[index]
            index += 1
    return ''.join(plaintext)

# User input
choice = input("Type 'E' to encrypt or 'D' to decrypt: ").upper()
text = input("Enter your text: ")
key = int(input("Enter numeric key (number of columns): "))

if choice == 'E':
    print("Encrypted:", encrypt(text, key))
elif choice == 'D':
    print("Decrypted:", decrypt(text, key))
else:
    print("Invalid choice!")
