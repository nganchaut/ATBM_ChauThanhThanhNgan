p = 17
q = 23
e = 5
n = p * q  # 391

plaintext= "ChauThanhThanhNgan"
ciphertext = []

for char in plaintext:
    m = ord(char)
    c = pow(m, e, n)
    ciphertext.append(c)
print("Plaintext: ", plaintext)
print("Ciphertext:", ciphertext)
