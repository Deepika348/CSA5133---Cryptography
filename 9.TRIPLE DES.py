def process(text, key):
    result = ""
    for c in text:
        result += chr(ord(c) ^ key)
    return result

choice = input("Enter E for Encryption or D for Decryption: ")
text = input("Enter the text: ")

k1 = int(input("Enter Key 1: "))
k2 = int(input("Enter Key 2: "))
k3 = int(input("Enter Key 3: "))

if choice.upper() == "E":
    text = process(text, k1)
    text = process(text, k2)
    text = process(text, k3)
    print("Encrypted Text:", text)

elif choice.upper() == "D":
    text = process(text, k3)
    text = process(text, k2)
    text = process(text, k1)
    print("Decrypted Text:", text)

else:
    print("Invalid choice")
