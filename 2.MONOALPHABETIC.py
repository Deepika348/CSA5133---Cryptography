

import string

# Monoalphabetic substitution key
key = "QWERTYUIOPASDFGHJKLZXCVBNM"
plain = string.ascii_uppercase
encrypt_dict = {plain[i]: key[i] for i in range(26)}
decrypt_dict = {key[i]: plain[i] for i in range(26)}

# User input
choice = input("Type 'E' to encrypt or 'D' to decrypt: ").upper()
text = input("Enter your text: ").upper()

# Encryption/Decryption
if choice == 'E':
    result = ''.join(encrypt_dict.get(c, c) for c in text)
elif choice == 'D':
    result = ''.join(decrypt_dict.get(c, c) for c in text)
else:
    result = "Invalid choice!"

print("Result:", result)
