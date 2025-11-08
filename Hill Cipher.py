import numpy as np

# Fungsi untuk cek apakah key matrix valid
def is_valid_key(key):
    n = int(len(key) ** 0.5)
    key_matrix = np.array(key).reshape(n, n)
    det = int(round(np.linalg.det(key_matrix)))
    det_mod = det % 26

    # Key valid jika determinan relatif prima dengan 26
    return np.gcd(det_mod, 26) == 1


# Fungsi enkripsi
def hill_encrypt(text, key):
    text = text.upper().replace(" ", "")
    n = int(len(key) ** 0.5)
    key = np.array(key).reshape(n, n)

    # Padding jika panjang text tidak kelipatan n
    while len(text) % n != 0:
        text += "X"

    result = ""
    for i in range(0, len(text), n):
        block = [ord(c) - 65 for c in text[i:i+n]]
        cipher = np.dot(key, block) % 26
        result += "".join(chr(c + 65) for c in cipher)
    return result


# Fungsi dekripsi
def hill_decrypt(cipher, key):
    cipher = cipher.upper().replace(" ", "")
    n = int(len(key) ** 0.5)
    key = np.array(key).reshape(n, n)

    # Invers matrix mod 26
    det = int(round(np.linalg.det(key)))
    det_mod = det % 26
    det_inv = pow(det_mod, -1, 26)
    adj = np.round(det * np.linalg.inv(key)).astype(int) % 26
    inv_key = (det_inv * adj) % 26

    result = ""
    for i in range(0, len(cipher), n):
        block = [ord(c) - 65 for c in cipher[i:i+n]]
        plain = np.dot(inv_key, block) % 26
        result += "".join(chr(int(p) + 65) for p in plain)
    return result


# MAIN PROGRAM
text = input("Masukkan teks: ").upper().replace(" ", "")
n = int(input("Masukkan ukuran matriks key (contoh: 2 untuk 2x2, 3 untuk 3x3): "))

# Input semua elemen key matrix dalam satu baris
key_input = input(f"Masukkan {n*n} elemen key matrix (pisahkan dengan spasi): ")
key = list(map(int, key_input.split()))

# Cek jumlah elemen
if len(key) != n * n:
    raise ValueError("❌ Jumlah elemen tidak sesuai ukuran matriks!")

# Validasi key matrix
if not is_valid_key(key):
    print("\n❌ Key tidak valid! Determinan tidak relatif prima dengan 26.")
    print("Silakan coba kombinasi angka lain.")
else:
    print("\n✅ Key valid! Lanjut ke proses enkripsi & dekripsi...")

    # Enkripsi & Dekripsi
    encrypted = hill_encrypt(text, key)
    decrypted = hill_decrypt(encrypted, key)

    # Hasil
    print("\n===== HASIL =====")
    print(f"Plaintext : {text}")
    print(f"Key Matrix:\n{np.array(key).reshape(n, n)}")
    print(f"Encrypt   : {encrypted}")
    print(f"Decrypt   : {decrypted}")