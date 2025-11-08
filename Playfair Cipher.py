def generate_table(key):
    key = key.upper().replace("J","I")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    table = ""

    for c in key + alphabet:
        if c not in table:
            table += c

    return [table[i:i+5] for i in range(0,25,5)]


def format_plaintext(text):
    text = text.upper().replace(" ", "").replace("J","I")
    result = ""
    
    i = 0
    while i < len(text):
        result += text[i]
        if i+1 == len(text):
            result += "X"
            break
        if text[i] == text[i+1]:
            result += "X"
            i += 1
        else:
            result += text[i+1]
            i += 2
    return result


def find_position(table, char):
    for r in range(5):
        for c in range(5):
            if table[r][c] == char:
                return r, c


def playfair_encrypt(plain, table):
    cipher = ""
    for i in range(0, len(plain), 2):
        a, b = plain[i], plain[i+1]
        r1, c1 = find_position(table, a)
        r2, c2 = find_position(table, b)

        if r1 == r2: # same row
            cipher += table[r1][(c1+1)%5] + table[r2][(c2+1)%5]
        elif c1 == c2: # same column
            cipher += table[(r1+1)%5][c1] + table[(r2+1)%5][c2]
        else: # rectangle
            cipher += table[r1][c2] + table[r2][c1]

    return cipher


def playfair_decrypt(cipher, table):
    plain = ""
    for i in range(0, len(cipher), 2):
        a, b = cipher[i], cipher[i+1]
        r1, c1 = find_position(table, a)
        r2, c2 = find_position(table, b)

        if r1 == r2: # same row
            plain += table[r1][(c1-1)%5] + table[r2][(c2-1)%5]
        elif c1 == c2: # same column
            plain += table[(r1-1)%5][c1] + table[(r2-1)%5][c2]
        else: # rectangle
            plain += table[r1][c2] + table[r2][c1]

    return plain

# MAIN PROGRAM
plaintext = input("Masukkan teks: ")
key = input("Masukkan key: ")

table = generate_table(key)
formatted = format_plaintext(plaintext)
cipher = playfair_encrypt(formatted, table)
decrypt = playfair_decrypt(cipher, table)

print(f"\nMATRIX  KEY      : {key.upper()}\n")
for row in table:
    print(' '.join(row))

print("\n===== HASIL =====")
print(f"Plaintext            : {formatted}")
print(f"Key                  : {key}")
print(f"Encrypt              : {cipher}")
print(f"Decrypt              : {decrypt}")