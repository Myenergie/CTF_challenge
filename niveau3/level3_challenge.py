# Function pour encrypter en XOR
def xor_encrypt(plaintext, key):
    ciphertext = bytearray(len(plaintext))
    for i in range(len(plaintext)):
        ciphertext[i] = ord(plaintext[i]) ^ key[i % len(key)]
    return ciphertext

# fonction pour le caesar
def caesar_encrypt(plaintext, shift):
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext

# le flag en text clair
plaintext_flag = '01253{agent_compromised}'

# pour defenir la cle
key = bytearray([0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7, 0x8, 0x9]) 

# defenir le shift
caesar_shift = 4

# creer l'incription caesar
intermediate_text = caesar_encrypt(plaintext_flag, caesar_shift)

# creer l'incription XOR
encrypted_flag = xor_encrypt(intermediate_text, key)

print("Encrypted Flag: ", encrypted_flag)
