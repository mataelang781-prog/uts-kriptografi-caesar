# Program Caesar Cipher

def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():

            base = ord('A') if char.isupper() else ord('a')

            encrypted_char = chr((ord(char) - base + shift) % 26 + base)

            result += encrypted_char
        else:
            result += char

    return result


def decrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():

            base = ord('A') if char.isupper() else ord('a')

            decrypted_char = chr((ord(char) - base - shift) % 26 + base)

            result += decrypted_char
        else:
            result += char

    return result


plaintext = input("Masukkan teks: ")
shift = int(input("Masukkan nilai shift: "))

ciphertext = encrypt(plaintext, shift)
print("Hasil Enkripsi :", ciphertext)

decrypted = decrypt(ciphertext, shift)
print("Hasil Dekripsi :", decrypted)