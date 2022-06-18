# Packets Primer
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Download the packet capture file and use packet analysis software to find the flag.
- [Download packet capture](https://github.com/jon-brandy/CTF-WRITE-UP/blob/e72f4d98ab9d736fde794f975315a6e5b11d8c85/Asset/Packets%20Primer/network-dump.flag.pcap)
## HINT:
1. Wireshark, if you can install and use it, is probably the most beginner friendly packet analysis software product.
## STEPS:
1. First, download the file given.
2. It is known that the extension is `.pcap` and based from the hint, we may try to use `wireshark`.
3. Next, open `wireshark` on your kali linux, then try to choose `open file` and choose the `network-dump.flag.pcap` file.
4. Here is how it looks after you opened the file.

![Screenshot (449)](https://user-images.githubusercontent.com/70703371/174423629-1f961666-7ea4-4204-970b-fb4a71c4031a.png)

5. Now try to check the number `4`.

![Screenshot (450)](https://user-images.githubusercontent.com/70703371/174423673-99e51c33-32af-4f5e-83ea-c47fa8131ddb.png)

6. Look to the packet bytes at below. Finally we got the flag!

![Screenshot (451)](https://user-images.githubusercontent.com/70703371/174423706-6b1b1f7f-9749-43ae-86d7-ae18913ad3e0.png)

```
p i c o C T F { p 4 c k 3 7 _ 5 h 4 r k _ 0 1 b 0 a 0 d 6 }
```

---

## FLAG:
```
picoCTF{p4ck37_5h4rk_01b0a0d6}
```
