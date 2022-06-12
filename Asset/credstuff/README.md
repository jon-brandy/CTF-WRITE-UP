# credstuff
#### Write-up Author = Q
## DESCRIPTION:
We found a leak of a blackmarket website's login credentials. 
Can you find the password of the user `cultiris` and successfully decrypt it? Download the leak [here](https://github.com/jon-brandy/CTF-WRITE-UP/blob/aa4795076e2461d272f9188cc8327ae0ef8885af/Asset/credstuff/leak.tar). 
The first user in `usernames.txt` corresponds to the first password in 
`passwords.txt`. The second user corresponds to the second password, and so on.
## HINT:
Maybe other passwords will have hints about the leak?

## STEPS:
1. Download the file and extract it
2. Open all the files inside the folder
3. Based from the hint, the first username corespond to the first password and so on
4. Now try to search `cultiris` in the `username.txt` file and look at the line

![image](https://user-images.githubusercontent.com/89120989/173223765-89691dd7-7fee-4e79-add7-131b382abe03.png)

5. And then now try to search line 378 in the `password.txt` file
6. As you can see there, there is a ROT13 text. But, how can i know there is a ROT13 text? Try to search `pico` on the `password.txt` file and you will see something on line 204
8. it says `pICo7rYpiCoU51N6PicOr0t13`

![image](https://user-images.githubusercontent.com/89120989/173223774-95b673ac-932c-4869-ac77-159be234be27.png)

9. Now you have to copy the flag and put it in the code

```py
import codecs
import os

os.system("cls")
val = codecs.decode('cvpbPGS{P7e1S_54I35_71Z3}', 'rot_13')
print(val)
```

10. Wala, you have the flag!

---


## FLAG:
```
picoCTF{C7r1F_54V35_71M3}
```
