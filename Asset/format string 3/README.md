# format string 3
> Write-up author: jon-brandy

## DESCRIPTION:
<p align="justify">This program doesn't contain a win function. How can you win? Download the binary here. Download the source here. Download libc here, download the interpreter here. Run the binary with these two files present in the same directory.

Additional details will be available after launching your challenge instance.</p>

## HINT:
Is there any way to change what a function points to?

## STEPS:
1. In this challenge we're given both the source code and the binary.
2. The binary is 64 bit LSB, dynamically linked, and not stripped.

![image](https://github.com/jon-brandy/CTF-WRITE-UP/assets/70703371/aeb18692-e6df-4e6e-8fb3-2a58970dfce1)

> BINARY PROTECTIONS

![image](https://github.com/jon-brandy/CTF-WRITE-UP/assets/70703371/501481c6-f188-47a8-88f1-381af3a42538)

3. Upon reviewing the source code, the challenge is very straightforward.
4. The binary is **Partial RELRO** and there's a **printf()** usage which missing it's format specifier, hence introducing FSB (Format String Bug).
5. At next LOC, a **puts()** called and `/bin/sh` string used as the argument.
6. Our objective is to overwrite `puts@got` with `libc.sym.system`. It shall gets us a shell --> `system("/bin/sh")`.
7. Now let's identify which `function@got` can be overwritten.

> IN GDB


