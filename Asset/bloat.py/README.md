# bloat.py
## DESCRIPTION:
Can you get the flag? 
Run this [Python program](https://github.com/jon-brandy/CTF-WRITE-UP/blob/94559f3372a32f8f0d4a84e1608715859c6e2286/Asset/bloat.py/bloat.flag.py) in the same directory as this [encrypted flag](https://github.com/jon-brandy/CTF-WRITE-UP/blob/891a9d6b4149b4bc406347fb5ddb32d7570407d7/Asset/bloat.py/flag.txt.enc).
## HINT:
- NONE
## STEPS:
1. First download the two given files.
2. Now try to run the python file. It will ask you to input a password.

![Screenshot (498)](https://user-images.githubusercontent.com/70703371/175916512-d1c64333-e57f-438e-a7b3-1a08481c4d60.png)

3. Since, we don't know what the password is, now open the python file.

```py
import sys
a = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
            "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ "
def arg133(arg432):
  if arg432 == a[71]+a[64]+a[79]+a[79]+a[88]+a[66]+a[71]+a[64]+a[77]+a[66]+a[68]:
    return True
  else:
    print(a[51]+a[71]+a[64]+a[83]+a[94]+a[79]+a[64]+a[82]+a[82]+a[86]+a[78]+\
a[81]+a[67]+a[94]+a[72]+a[82]+a[94]+a[72]+a[77]+a[66]+a[78]+a[81]+\
a[81]+a[68]+a[66]+a[83])
    sys.exit(0)
    return False
def arg111(arg444):
  return arg122(arg444.decode(), a[81]+a[64]+a[79]+a[82]+a[66]+a[64]+a[75]+\
a[75]+a[72]+a[78]+a[77])
def arg232():
  return input(a[47]+a[75]+a[68]+a[64]+a[82]+a[68]+a[94]+a[68]+a[77]+a[83]+\
a[68]+a[81]+a[94]+a[66]+a[78]+a[81]+a[81]+a[68]+a[66]+a[83]+\
a[94]+a[79]+a[64]+a[82]+a[82]+a[86]+a[78]+a[81]+a[67]+a[94]+\
a[69]+a[78]+a[81]+a[94]+a[69]+a[75]+a[64]+a[70]+a[25]+a[94])
def arg132():
  return open('flag.txt.enc', 'rb').read()
def arg112():
  print(a[54]+a[68]+a[75]+a[66]+a[78]+a[76]+a[68]+a[94]+a[65]+a[64]+a[66]+\
a[74]+a[13]+a[13]+a[13]+a[94]+a[88]+a[78]+a[84]+a[81]+a[94]+a[69]+\
a[75]+a[64]+a[70]+a[11]+a[94]+a[84]+a[82]+a[68]+a[81]+a[25])
def arg122(arg432, arg423):
    arg433 = arg423
    i = 0
    while len(arg433) < len(arg432):
        arg433 = arg433 + arg423[i]
        i = (i + 1) % len(arg423)        
    return "".join([chr(ord(arg422) ^ ord(arg442)) for (arg422,arg442) in zip(arg432,arg433)])
arg444 = arg132()
arg432 = arg232()
arg133(arg432)
arg112()
arg423 = arg111(arg444)
print(arg423)
sys.exit(0)

```

5. If you try to analyze the source code, you will come to a conclusion that if user input the following value from these indexes `a[71]+a[64]+a[79]+a[79]+a[88]+a[66]+a[71]+a[64]+a[77]+a[66]+a[68]`, it will return true which means we might get the flag.
6. Because I want to know the value of each index, so I created a new python file with the following code contents

```py
import os
os.system("cls")
a = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
            "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ "

print(a[71]+a[64]+a[79]+a[79]+a[88]+a[66]+a[71]+a[64]+a[77]+a[66]+a[68])
```

7. Next, i run the code and got this output:

![Screenshot (499)](https://user-images.githubusercontent.com/70703371/175917735-46e5e18a-2a78-447c-a1f3-db48ee9c1226.png)

8. So now we know that the password is `happychance`.
9. Run the `bloat.py` file again and input the password as `happychance`.

![Screenshot (500)](https://user-images.githubusercontent.com/70703371/175918208-65587d2d-db0c-4ab5-83f3-8d2f2472deec.png)

10. Finally we got the flag!


---
## FLAG
```
picoCTF{d30bfu5c4710n_f7w_5e14b257}
```

