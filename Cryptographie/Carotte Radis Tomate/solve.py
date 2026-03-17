from sympy.ntheory.modular import crt
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import unpad

vegetables = [392278890668246705, 4588810924820033807, 17164682861166542664, 12928514648456294931, 5973470563196845286]
mods = [17488856370348678479, 16548497022403653709, 17646308379662286151, 14933475126425703583, 17256641469715966189]

if __name__ == "__main__":
    key, _ = crt(mods, vegetables)
    print("key = ", key)
    E = AES.new(key.to_bytes(32, "big"), AES.MODE_ECB)
    enc = bytes.fromhex("2da1dbe8c3a739d9c4a0dc29a27377fe8abc1c0feacc9475019c5954bbbf74dcedce7ed3dc3ba34fa14a9181d4d7ec0133ca96012b0a9f4aa93c42c61acbeae7640dd101a6d2db9ad4f3b8ccfe285e0d")
    print("flag = ", unpad(E.decrypt(enc), 16).decode())

