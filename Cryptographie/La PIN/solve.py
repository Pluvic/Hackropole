from Cryptodome.Cipher import AES
from Cryptodome.Protocol.KDF import scrypt
from Cryptodome.Util.number import long_to_bytes


with open("output.txt", "rb") as f:
    data = bytes.fromhex(f.read().decode())
    nonce = data[:16]
    c = data[16:-16]
    tag = data[-16:]

for pin in range(10000):
    k = scrypt(long_to_bytes(pin), b"FCSC", 32, N = 2 ** 10, r = 8, p = 1)
    aes = AES.new(k, AES.MODE_GCM, nonce=nonce)
    try:
        flag = aes.decrypt_and_verify(c, tag)
        print(flag.decode())
        break
    except ValueError:
        pass
