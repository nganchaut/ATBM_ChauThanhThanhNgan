# plaintext = input("Nhap plaintext: ")
plaintext = "CHAU THANH THANH NGAN"
k = 1
ciphertext = ""

for ch in plaintext:
    if ch.isalpha():  
        base = ord('A') if ch.isupper() else ord('a')
        new_char = chr((ord(ch) - base + k) % 26 + base)
        ciphertext += new_char
    else:
        ciphertext += ch 

print("Ciphertext:", ciphertext)
