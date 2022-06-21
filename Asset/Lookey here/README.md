# Lookey here
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Attackers have hidden information in a very large mass of data in the past, maybe they are still doing it. 
Download the data [here](https://github.com/jon-brandy/CTF-WRITE-UP/blob/51ba47abead27b99186ef748aeef4976dc364994/Asset/Lookey%20here/anthem.flag.txt).
## HINT:
1. Download the file and search for the flag based on the known prefix.
## STEPS:
1. First, download the file given.
2. At your kali linux terminal , type this command `cat anthem.flag.txt`, then press enter.

![Screenshot (463)](https://user-images.githubusercontent.com/70703371/174806524-1c3abc97-cbb6-471f-81d6-4cba0b2c20d5.png)

3. It is known, the contents of the file consist of many sentences. It will be very difficult to search for flags manually.
4. Now type this command at your kali linux terminal `cat anthem.flag.txt | grep 'pico`, then press enter.

![Screenshot (464)](https://user-images.githubusercontent.com/70703371/174807072-5ae85920-6347-4d03-b37f-07dfab3f9b15.png)

5. Finally, we got the flag!


---

## FLAG
```
picoCTF{gr3p_15_@w3s0m3_2116b979}
```
