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

8. 
