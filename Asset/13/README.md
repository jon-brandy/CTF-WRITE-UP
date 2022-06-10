# 13
## DESCRIPTION:
Cryptography can be easy, do you know what ROT13 is? **cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}**
## HINT:
This can be solved online if you don't want to do it by hand!
## STEPS:
1. You can try either manually using online [website](https://rot13.com/) or using python code, both result are the same
```py
import codecs
import os

os.system("cls")
val = codecs.decode('cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}', 'rot_13')
print(val)
```
2. Finally we got the flag!

![Screenshot (441)](https://user-images.githubusercontent.com/70703371/173089624-56e518e8-033c-427e-a978-6235cfc23512.png)

---

## FLAG:
```
picoCTF{not_too_bad_of_a_problem}
```
