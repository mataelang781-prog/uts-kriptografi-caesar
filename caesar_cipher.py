# Program Kriptografi Caesar Cipher

def enkripsi(teks, shift):
    hasil = ""

    for huruf in teks:

        # Mengecek apakah karakter berupa huruf
        if huruf.isalpha():

            # Menentukan huruf besar atau kecil
            dasar = ord('A') if huruf.isupper() else ord('a')

            # Proses enkripsi menggunakan modulo 26
            karakter_baru = chr((ord(huruf) - dasar + shift) % 26 + dasar)

            hasil += karakter_baru

        else:
            hasil += huruf

    return hasil


def dekripsi(teks, shift):
    hasil = ""

    for huruf in teks:

        if huruf.isalpha():

            dasar = ord('A') if huruf.isupper() else ord('a')

            # Proses dekripsi
            karakter_baru = chr((ord(huruf) - dasar - shift) % 26 + dasar)

            hasil += karakter_baru

        else:
            hasil += huruf

    return hasil


# Input pengguna
plaintext = input("Masukkan teks : ")
shift = int(input("Masukkan nilai shift : "))

# Proses enkripsi
ciphertext = enkripsi(plaintext, shift)
print("Hasil Enkripsi :", ciphertext)

# Proses dekripsi
plaintext_awal = dekripsi(ciphertext, shift)
print("Hasil Dekripsi :", plaintext_awal)