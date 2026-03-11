# Simple RC5 Implementation (32-bit word)

def RC5_encrypt(A, B, K, r=12, w=32):
    mod = 2 ** w
    S = [0] * (2 * (r + 1))

    # Constants for RC5
    P = 0xB7E15163
    Q = 0x9E3779B9

    # Key expansion
    S[0] = P
    for i in range(1, 2*(r+1)):
        S[i] = (S[i-1] + Q) % mod

    A = (A + S[0]) % mod
    B = (B + S[1]) % mod

    for i in range(1, r+1):
        A = ((A ^ B) << (B % w) | (A ^ B) >> (w - (B % w))) % mod
        A = (A + S[2*i]) % mod

        B = ((B ^ A) << (A % w) | (B ^ A) >> (w - (A % w))) % mod
        B = (B + S[2*i+1]) % mod

    return A, B


def RC5_decrypt(A, B, K, r=12, w=32):
    mod = 2 ** w
    S = [0] * (2 * (r + 1))

    P = 0xB7E15163
    Q = 0x9E3779B9

    S[0] = P
    for i in range(1, 2*(r+1)):
        S[i] = (S[i-1] + Q) % mod

    for i in range(r, 0, -1):
        B = (B - S[2*i+1]) % mod
        B = ((B >> (A % w)) | (B << (w - (A % w)))) % mod
        B = B ^ A

        A = (A - S[2*i]) % mod
        A = ((A >> (B % w)) | (A << (w - (B % w)))) % mod
        A = A ^ B

    B = (B - S[1]) % mod
    A = (A - S[0]) % mod

    return A, B


# Input
A = int(input("Enter first block: "))
B = int(input("Enter second block: "))
K = int(input("Enter key: "))

# Encryption
encA, encB = RC5_encrypt(A, B, K)
print("Encrypted blocks:", encA, encB)

# Decryption
decA, decB = RC5_decrypt(encA, encB, K)
print("Decrypted blocks:", decA, decB)
