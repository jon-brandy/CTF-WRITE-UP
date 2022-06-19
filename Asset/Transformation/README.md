# Search Source
#### Write-up author : [PlasmaRing](https://github.com/PlasmaRing)
## DESCRIPTION:
I wonder what this really is... [enc](https://mercury.picoctf.net/static/a757282979af14ab5ed74f0ed5e2ca95/enc) ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])  
## HINT:
1. You may find some decoders online  
## STEPS:
1. Analisa file `enc` yang berisi: `灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彤㔲挶戹㍽`
2. Gunakan online decoder seperti CyberChef
3. Gunakan Magic & Intensive Mode pada Cyber Chef
![image](https://user-images.githubusercontent.com/92077284/174487475-945bbb78-1445-4980-a895-335a348e2a82.png)  
4.  FLAG DIPEROLEH 

---

## FLAG
```
picoCTF{16_bits_inst34d_of_8_d52c6b93}
```

