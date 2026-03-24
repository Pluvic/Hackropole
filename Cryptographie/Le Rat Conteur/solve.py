from Cryptodome.Cipher import AES
from Cryptodome.Util import Counter
from Cryptodome.Util.number import long_to_bytes

key = bytes.fromhex("00112233445566778899aabbccddeeff")

ctr = Counter.new(128, initial_value=0)

aes = AES.new(key, AES.MODE_CTR, counter=ctr)

with open("flag.jpg.enc", "rb") as f:
    ciphertext = f.read()
    plaintext = aes.decrypt(ciphertext)
    

    with open("flag.jpg", "wb") as out:
        out.write(plaintext)
