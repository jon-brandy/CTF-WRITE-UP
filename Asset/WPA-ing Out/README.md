# WPA-ing Out
> Write-up author: vreshco
## DESCRIPTION:
I thought that my password was super-secret, but it turns out that passwords passed over the AIR can be CRACKED, 
especially if I used the same wireless network password as one in the rockyou.txt credential dump. 
Use this 'pcap file' and the rockyou wordlist. The flag should be entered in the picoCTF{XXXXXX} format.
## HINT:
1. Finding the IEEE 802.11 wireless protocol used in the wireless traffic packet capture is easier with wireshark, the JAWS of the network. 
2. Aircrack-ng can make a pcap file catch big air...and crack a password.
## STEPS:
1. First, download the `.pcap` file given and check the packets.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/217513510-5258c615-458b-4f92-86d4-43c0f0f3a81f.png)


2. Hmm.. All the packets seems used the same protocols, IEEE 802.11 is a wireless protocol used in the wireless traffic packer capture.
3. Based from the hint we can use `aircrack-ng` to crack the key/password, or simply do wifi hacking.
4. For example, to check if there's any malicious act like handshake attempt, we can run:

```
aircrack-ng wpa-ing_out.pcap
```

> RESULT

![image](https://user-images.githubusercontent.com/70703371/217514619-0ad8e864-210a-44f8-82a2-b82d7133bfc0.png)


5. Got 1, means there's a malicious act and we can decrypt the encryption using wordlists.
6. Based from the description, we should use `rockyou.txt` let's use the `-w` flag to add the wordlists.

```
aircrack-ng -w /usr/share/wordlists/rockyou.txt  wpa-ing_out.pcap
```

> RESULT

![image](https://user-images.githubusercontent.com/70703371/217515084-82a7fcff-ea4d-4774-9427-b26fcbef32b2.png)


7. Got it, let's wrap the key found with `picoCTF{}`.

## FLAG

```
picoCTF{mickeymouse} 
```
