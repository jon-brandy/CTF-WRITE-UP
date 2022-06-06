# Nice netcat...
## Steps:
1. Run this command `nc mercury.picoctf.net 7449` on your linux terminal.
2. After that we will get this output:
---
![Terminal](https://user-images.githubusercontent.com/98648342/169433940-d4b1338f-6e65-4268-af07-d8082055d65d.png)

3. We can guess that the output are ascii codes.
4. We can do it manually or using code to solve it. In this case i made a python program to convert ascii to text.
5. Below are the source code.
## Source-Code:
![Source-Code](https://user-images.githubusercontent.com/98648342/169433831-0aaed967-712a-4335-832a-d8959bb7e3df.png)

6. After we run the code, finally we can see the flag!
### [SOURCE-CODE](https://github.com/jon-shel/CTF-WRITE-UP/blob/1761e2f5502509a94642030932ef3ccf48fcf03f/Asset/Nice%20netcat.../asciiConverter.py)

```py
import os
def asciiConvert(intArr):
    os.system("cls") 
    string = "" 
    for item in intArr:
        string += chr(item)
    print(string)

intArr = [112, 105, 99, 111, 67, 84, 70, 123, 103, 48, 48, 100,
          95, 107, 49, 116, 116, 121, 33, 95, 110, 49, 99, 51, 
          95, 107, 49, 116, 116, 121, 33, 95, 102, 50, 100, 55, 99, 
          97, 102, 97, 125, 10]

asciiConvert(intArr)
```

---

## FLAG
```
picoCTF{g00d_k1tty!_n1c3_k1tty!_f2d7cafa}
```
