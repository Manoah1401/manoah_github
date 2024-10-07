def KSA(key):
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]  # Swap values
    return S

def PRGA(S):
    i = j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]  # Swap values
        yield S[(S[i] + S[j]) % 256]

def RC4(key, text):
    key = [ord(c) for c in key]
    S = KSA(key)
    keystream = PRGA(S)
    return ''.join([chr(ord(c) ^ next(keystream)) for c in text])

# User Input for RC4
key = input("Enter the key for RC4: ")
plaintext = input("Enter the plaintext for RC4: ")
ciphertext = RC4(key, plaintext)
print("Encrypted RC4:", ciphertext)

decrypted = RC4(key, ciphertext)
print("Decrypted RC4:", decrypted)
