import json
from Cryptodome.Cipher import AES
from Cryptodome.Hash import HMAC, SHA256

with open("output.txt", "r") as f:
    r = json.loads(f.read())
    iv = bytes.fromhex(r["iv"])
    c  = bytes.fromhex(r["c"])
    h  = r["h"]

    with open("rockyou.txt", "r", encoding="latin-1") as f:
        for line in f:
            password = line.strip().encode()
            h2 = HMAC.new(password, digestmod = SHA256)
            h2.update(b"FCSC2022")
            if h2.hexdigest() == h:
                print(f"Password found: {password.decode()}")
                break

    k  = SHA256.new(password).digest()
    cipher = AES.new(k, AES.MODE_CBC, iv = iv)
    flag = cipher.decrypt(c)
    print(flag.decode())