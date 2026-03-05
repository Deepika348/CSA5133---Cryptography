

def caesar(text, shift):
    result = ""
    for c in text:
        if c.isalpha():
            base = 'A' if c.isupper() else 'a'
            result += chr((ord(c) - ord(base) + shift) % 26 + ord(base))
        else:
            result += c
    return result

# User input
text = input("Enter text: ")
key = int(input("Enter key (shift value): "))
choice = input("Encrypt or Decrypt? (E/D): ").strip().lower()

if choice in ['encrypt', 'e']:
    print("Result:", caesar(text, key))
elif choice in ['decrypt', 'd']:
    print("Result:", caesar(text, -key))
else:
    print("Invalid choice!")
