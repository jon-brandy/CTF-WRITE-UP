# GDB Test Drive
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Can you get the flag? Download this [binary]().
Here's the test drive instructions:

```sh
$ chmod +x gdbme
$ gdb gdbme
(gdb) layout asm
(gdb) break *(main+99)
(gdb) run
(gdb) jump *(main+104)
```

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

5. Based from the instructions given, type `layout asm`, then press enter.

![image](https://user-images.githubusercontent.com/70703371/182019582-cdcade41-d0cd-4059-9cb1-3b6ad93b35db.png)

6. Then type `break *(main+99)`.

![image](https://user-images.githubusercontent.com/70703371/182019641-a2643c66-ed64-4f25-ac12-42bd8bfe6f12.png)

7. Type `run` then press enter.

![image](https://user-images.githubusercontent.com/70703371/182019656-0ba92f41-9150-43bb-bff0-f81b64b9a793.png)

8. Simply followed the last instruction by type `jump *(main+104)` then press enter.

![image](https://user-images.githubusercontent.com/70703371/182019696-46ab7111-3dfc-47d4-b71e-3fa492fae342.png)

9. We found the flag!

---

## FLAG

```
picoCTF{d3bugg3r_dr1v3_7776d758}
```
