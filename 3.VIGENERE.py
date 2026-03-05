

# Vigenère Cipher
def encrypt(text, key):
    text = text.upper()
    key = key.upper()
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            key_index += 1
        else:
            result += char
    return result

def decrypt(cipher, key):
    cipher = cipher.upper()
    key = key.upper()
    result = ""
    key_index = 0
    for char in cipher:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            result += chr((ord(char) - ord('A') - shift + 26) % 26 + ord('A'))
            key_index += 1
        else:
            result += char
    return result

# User input
choice = input("Type 'E' to encrypt or 'D' to decrypt: ").upper()
text = input("Enter your text: ")
key = input("Enter the key: ")

if choice == 'E':
    print("Encrypted:", encrypt(text, key))
elif choice == 'D':
    print("Decrypted:", decrypt(text, key))
else:
    print("Invalid choice!")
