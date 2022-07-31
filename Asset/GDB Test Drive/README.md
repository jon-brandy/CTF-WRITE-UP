# GDB Test Drive
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Can you get the flag? Download this [binary]().
Here's the test drive instructions:

    $ chmod +x gdbme
    $ gdb gdbme
    (gdb) layout asm
    (gdb) break *(main+99)
    (gdb) run
    (gdb) jump *(main+104)

## HINT:
- NONE
## STEPS:
1. First, download the file given.
2. Next check the file type by run -> `file gdbme`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/182019448-e5b53aeb-cb5c-4c77-badf-c3ada045cd38.png)

3. Since it's a `ELF 64 Bit` , we can make it executeable by run -> `chmod +x gdbme`.
4. Based from the title, we may use `gdb` command to run this file -> `gdb gdbme`.

![image](https://user-images.githubusercontent.com/70703371/182019516-1c8da663-a7cb-4206-8ffe-1b934dd128b8.png)

5. 
