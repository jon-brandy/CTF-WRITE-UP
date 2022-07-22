# sharks on wire 1
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
We found this [packet capture](https://github.com/jon-brandy/CTF-WRITE-UP/blob/53def509075156862ddf59a0695ad6e960aff299/Asset/sharks%20on%20wire%201/capture.pcap). Recover the flag.
## HINTS:
1. Try using a tool like Wireshark
2. What are streams?
## STEPS:
1. First, download the `.pcap` file given.
2. Next, since it's a `.pcap` file, we may open it using wireshark.

![image](https://user-images.githubusercontent.com/70703371/180363626-d8d0802a-4ad6-4c5c-893d-acd1661196c2.png)

3. Since there's no `TCP` stream to follow, i tried to randomly pick any `UDP` stream to follow.

![image](https://user-images.githubusercontent.com/70703371/180363770-0dd21fee-6bb5-4184-b67e-eb35c4b68a68.png)

![image](https://user-images.githubusercontent.com/70703371/180363723-3ba3a8e9-8f4a-47c1-af13-ed2b4fdbcbd3.png)

4. For `udp.stream eq 4` i got no clue.
5. Then i tried to change the `eq` value.
6. Finally at `udp.stream eq 6` we got the flag!

![image](https://user-images.githubusercontent.com/70703371/180364005-a998e642-7195-499f-89b3-9be3937d36d6.png)

---
## FLAG

```
picoCTF{StaT31355_636f6e6e}
```
