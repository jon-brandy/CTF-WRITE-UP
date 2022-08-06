# Bbbbloat
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Can you get the flag? 
Reverse engineer this [binary](https://github.com/jon-brandy/CTF-WRITE-UP/blob/6e1e5b252b5e91cbfe28202f7f5ab9a07ead19b7/Asset/Bbbbloat/bbbbloat).
## HINT:
- NONE
## STEPS:
1. First, download the file given.
2. Next, check the file type by run -> `file bbbbloat`.

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/183069126-8ffd109a-deb0-44a9-8501-5a6c407dfc0c.png)

3. Since it's an `ELF 64-Bit` file, let's make it executeable by run -> `chmod +x bbbbloat`.
4. Now let's run the file.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/183069348-37832e35-984d-4300-a5bc-5d7ae2c840ac.png)

5. I input `15`.

![image](https://user-images.githubusercontent.com/70703371/183069399-966d7e66-caee-4921-a036-eb2b739985c9.png)

6. It seems we need to guess the number in order to get the flag.
7. Based from the description, to decompile it i use `IDA Freeware`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/183071120-7aa5bb8a-7886-4e15-96da-ead579d95db1.png)

8. Now press `f5` to see the `psuedocode` pov.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/183080157-f01dafb5-000f-4ea2-a0ee-2b9ea7e1ffd2.png)

```c
__int64 __fastcall main(int a1, char **a2, char **a3)
{
  int v4; // [rsp+10h] [rbp-40h] BYREF
  int v5; // [rsp+14h] [rbp-3Ch]
  char *s; // [rsp+18h] [rbp-38h]
  char v7[40]; // [rsp+20h] [rbp-30h] BYREF
  unsigned __int64 v8; // [rsp+48h] [rbp-8h]

  v8 = __readfsqword(0x28u);
  strcpy(v7, "A:4@r%uL4Ff0f9b03=_cf0cc7fc2e_N");
  printf("What's my favorite number? ");
  v5 = 863305;
  __isoc99_scanf("%d", &v4);
  v5 = 863305;
  if ( v4 == 549255 )
  {
    v5 = 863305;
    s = (char *)sub_1249(0LL, v7);
    fputs(s, stdout);
    putchar(10);
    free(s);
  }
  else
  {
    puts("Sorry, that's not it!");
  }
  return 0LL;
}
```

9. There's something caught my attention, if you try to analyze the if statements, we can conclude that the secret number might be -> `549255`.
10. Let's run the program again and input the secret number as `549255`.

![image](https://user-images.githubusercontent.com/70703371/183080546-077dd23c-edb0-4537-be48-dfcb9ce350cf.png)

11. Finally we got the flag!

---

## FLAG

```
picoCTF{cu7_7h3_bl047_44f74a60}
```
