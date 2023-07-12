# Bit-O-Asm-1
> Write-up author: jon-brandy
## DESCRIPTION:
Can you figure out what is in the eax register? Put your answer in the picoCTF flag format: picoCTF{n} where n is 
the contents of the eax register in the decimal number base. 
If the answer was 0x11 your flag would be picoCTF{17}. Download the assembly dump here.
## HINT:
- As with most assembly, there is a lot of noise in the instruction dump. Find the one line that pertains to this question and don't second guess yourself!
## STEPS:
1. Given a .txt file with a asm instruction written on it.

```asm
<+0>:     endbr64 
<+4>:     push   rbp
<+5>:     mov    rbp,rsp
<+8>:     mov    DWORD PTR [rbp-0x4],edi
<+11>:    mov    QWORD PTR [rbp-0x10],rsi
<+15>:    mov    eax,0x30
<+20>:    pop    rbp
<+21>:    ret
```

2. Based from the description, we just need to find the value stored in the eax, well if you noticed, there's `mov` instruction which stored 0x30 (48) to eax.
3. Hence the flag is 48

## FLAG:

```
picoCTF{48}
```
