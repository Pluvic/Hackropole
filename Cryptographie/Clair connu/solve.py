from Cryptodome.Util.strxor import strxor

with open("output.txt", "r") as f:
    c = bytes.fromhex(f.read().strip())

    plainKnown = b"FCSC"
    key = strxor(c[:len(plainKnown)], plainKnown)
    print(f"Key: {key.hex()}")

    key = key * 20

    flag = strxor(c, key[:len(c)])
    print(flag.decode())