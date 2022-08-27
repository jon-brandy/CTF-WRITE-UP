# Keygenme


#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Can you get the flag? 
Reverse engineer this [binary]().
## HINT:
- NONE
## STEPS:
1. First, download the file given then check the file type.

![image](https://user-images.githubusercontent.com/70703371/187009192-0946031f-6269-4b30-9c28-7ec74ac56c56.png)

> NOTES

```
The file is stripped so we can't see the functions name.
```

2. Since it's an ELF 64 bit file, let's make it executeable by run -> `chmod +x keygenme`.
3. Now, let's run the program.

![image](https://user-images.githubusercontent.com/70703371/183235724-cd305486-62c1-43dd-b442-fdfe5be70baf.png)

4. Hmm.. Let's open it using IDA Freeware.

![image](https://user-images.githubusercontent.com/70703371/183235787-e14b4c4f-8c8d-4a27-8d34-843f53d36f2e.png)

5. At the `main` function, press `f5` to decompile it.

![image](https://user-images.githubusercontent.com/70703371/183235867-b82da72c-e8aa-4ea1-a8c2-d79bc129078d.png)

6. Notice there's a canary to prevent buffer overflows there.

![image](https://user-images.githubusercontent.com/70703371/187009348-09d65a36-ba4e-480c-b0d7-95caa8b8da1c.png)

8. At the if statements, notice there's a function called `sub_1209`. Now let's open that function.

> FUNCTION sub_1209

![image](https://user-images.githubusercontent.com/70703371/183235909-a09d185e-70d0-4005-8d2b-381e31064cde.png)

```c
__int64 __fastcall sub_1209(const char *a1)
{
  size_t v1; // rax
  size_t v2; // rax
  int v4; // [rsp+18h] [rbp-C8h]
  int v5; // [rsp+18h] [rbp-C8h]
  int i; // [rsp+1Ch] [rbp-C4h]
  int j; // [rsp+20h] [rbp-C0h]
  int k; // [rsp+24h] [rbp-BCh]
  int m; // [rsp+28h] [rbp-B8h]
  char v10[18]; // [rsp+2Eh] [rbp-B2h] BYREF
  char v11[16]; // [rsp+40h] [rbp-A0h] BYREF
  char s[32]; // [rsp+50h] [rbp-90h] BYREF
  char v13[18]; // [rsp+70h] [rbp-70h] BYREF
  char v14; // [rsp+82h] [rbp-5Eh]
  char v15; // [rsp+89h] [rbp-57h]
  char v16; // [rsp+8Ah] [rbp-56h]
  char v17[72]; // [rsp+90h] [rbp-50h] BYREF
  unsigned __int64 v18; // [rsp+D8h] [rbp-8h]

  v18 = __readfsqword(0x28u);
  strcpy(s, "picoCTF{br1ng_y0ur_0wn_k3y_");
  strcpy(v10, "}");
  v1 = strlen(s);
  MD5(s, v1, &v10[2]);
  v2 = strlen(v10);
  MD5(v10, v2, v11);
  v4 = 0;
  for ( i = 0; i <= 15; ++i )
  {
    sprintf(&v13[v4], "%02x", (unsigned __int8)v10[i + 2]);
    v4 += 2;
  }
  v5 = 0;
  for ( j = 0; j <= 15; ++j )
  {
    sprintf(&v17[v5], "%02x", (unsigned __int8)v11[j]);
    v5 += 2;
  }
  for ( k = 0; k <= 26; ++k )
    v17[k + 32] = s[k];
  v17[59] = v14;
  v17[60] = v16;
  v17[61] = v15;
  v17[62] = v13[0];
  v17[63] = v16;
  v17[64] = v14;
  v17[65] = v13[12];
  v17[66] = v16;
  v17[67] = v10[0];
  if ( strlen(a1) != 36 )
    return 0LL;
  for ( m = 0; m <= 35; ++m )
  {
    if ( a1[m] != v17[m + 32] )
      return 0LL;
  }
  return 1LL;
}
```

7. If you look carefully, there's half piece of the flag.

![image](https://user-images.githubusercontent.com/70703371/183235949-5b320bf7-457a-4790-b72d-dc520949c2b4.png)

> HALF PIECE 

```
picoCTF{br1ng_y0ur_0wn_k3y_
```

8. 
