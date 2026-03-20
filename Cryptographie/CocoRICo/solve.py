from pwn import *
import json
from zlib import crc32 as le_mac

p = remote("localhost", 4000, level = "debug")

p.recvuntil(b">>> ")
p.sendline(b"1")
p.sendline(b"y")
p.sendline("AAAA")

# Récupérer le token chiffré
p.recvuntil(b"Here is your token:\n")
hexData = p.recvline().strip().decode()

data = bytes.fromhex(hexData)

# Plain text correspondant au token chiffré
plain = json.dumps({"name": "AAAA","admin": False}).encode()
plain += int.to_bytes(le_mac(plain), 4)

# Récupérer le keystream en XORant le token chiffré avec le plain text
keystream = bytes(a ^ b for a, b in zip(data, plain))

# Construire un token chiffré pour l'utilisateur admin
plainAdmin = json.dumps({"name": "toto","admin": True}).encode()
plainAdmin += int.to_bytes(le_mac(plainAdmin), 4)
adminToken = bytes(a ^ b for a, b in zip(plainAdmin, keystream))

# Envoyer le token chiffré pour passer pour l'admin
p.sendline(b"1")
p.sendline(b"n")
p.sendline(adminToken.hex().encode())
p.interactive()

