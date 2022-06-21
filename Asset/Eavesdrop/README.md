# Eavesdrop
#### Write-up author: [jon-brandy]()
## DESCRIPTION:
Download this packet capture and find the flag.
[Download packet capture](https://github.com/jon-brandy/CTF-WRITE-UP/blob/5bc7981002eb27cd6455e1d959c163ecef624188/Asset/Eavesdrop/capture.flag.pcap)
## HINT:
1. All we know is that this packet capture includes a chat conversation and a file transfer.
## STEPS:
1. Open wireshark, then choose the source number 12.

![Screenshot (454)](https://user-images.githubusercontent.com/70703371/174713860-3435f312-8b49-4d6b-b9eb-2cf77d63059a.png)

2. We chose that, because, if you see at the packet content, we captured the first conversation.
3. Next click the `analyze` tab, choose `follow` then choose `TCP Stream`.

![Screenshot (455)](https://user-images.githubusercontent.com/70703371/174714100-14ceb15c-fb67-44d7-9d6e-37ab75f61c1d.png)

4. Based from the conversation, we can conclude the command to decrypt the ciphertext is `openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123`.
5. Then, we got information too that the blue guy transferred the file at port `9002` to the red guy.
6. At the display filter specification bar, type `tcp.port == 9002` so we can filtered every port 9002.

![Screenshot (456)](https://user-images.githubusercontent.com/70703371/174715837-7f7ba915-458f-44b2-be7f-f49f5093fe65.png)

7. Next, open the source number 57.

![Screenshot (457)](https://user-images.githubusercontent.com/70703371/174715927-35363b2f-dcc7-47b0-9182-843211a1cddd.png)

8. Now try to search the text given at the packet header area.

![Screenshot (457)](https://user-images.githubusercontent.com/70703371/174716171-50616d57-0ef3-4e7e-9016-d9d770f488ed.png)

9. At the `data` header, we can see there are 48 bytes of character.

![Screenshot (458)](https://user-images.githubusercontent.com/70703371/174716498-4977ddd7-dab7-43ae-9b73-c3f12c8efd48.png)

10. Export the packets into a `raw` file and rename it to `eavesdrop.des3` or any name you like.
11. Then in your kali linux terminal type `openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123`.
12. 



openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123
