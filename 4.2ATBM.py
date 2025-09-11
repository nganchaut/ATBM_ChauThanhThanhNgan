plaintext = "Chau Thanh Thanh Ngan"
ciphertext = ""
k = 1  

for char in plaintext:
    if char.isalpha():  
        base = ord('A') if char.isupper() else ord('a')
        p = ord(char) - base  
        c = (p + k) % 26 
        ciphertext += chr(c + base) 
    else:
        ciphertext += char 

print("Plaintext: ", plaintext)
print("Ciphertext:", ciphertext)
