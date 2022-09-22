# Torrent Analyze
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
SOS, someone is torrenting on our network. 
One of your colleagues has been using torrent to download some files on the company’s network.
Can you identify the file(s) that were downloaded? 
The file name will be the flag, like picoCTF{filename}. [Captured traffic](https://artifacts.picoctf.net/c/206/torrent.pcap).
## HINTS:
1. Download and open the file with a packet analyzer like [Wireshark](https://www.wireshark.org/).
2. You may want to enable BitTorrent protocol (BT-DHT, etc.) on Wireshark. Analyze -> Enabled Protocols.
3. Try to understand peers, leechers and seeds. [Article](https://www.techworm.net/2017/03/seeds-peers-leechers-torrents-language.html).
4. The file name ends with `.iso`.
## STEPS:
1. First, download the file given.
2. Next, let's check the file type.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/191528031-d8178022-a7a9-4992-aa28-a359b91d7cf4.png)


3. Since it's a `.pcap` file, let's open it using wireshark.

![image](https://user-images.githubusercontent.com/70703371/191532494-4d6ec357-b9db-4e90-a1c3-d09fc869de08.png)

4. Based from the hint, let's enable BitTorrent protocol on wireshark.
5. Open the `analyze` tab then go to click the `Enabled Protocols`.

![image](https://user-images.githubusercontent.com/70703371/191762488-37a8f70b-c09b-4624-99b2-b4aa28e71208.png)

6. Search `bit`.

![image](https://user-images.githubusercontent.com/70703371/191762697-dd7ff271-f22d-4676-bb97-70e6a0922d79.png)

7. Tick the `bittorent_dht_udp` and `bt_utp_udp`, then click `ok`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/191762971-5f0db854-19dd-458d-8257-d0dfe9ab2b9a.png)

8. Now open the `statistics` tab , then choose `protocol hierarchy`.

![image](https://user-images.githubusercontent.com/70703371/191763483-27f9d01c-d98c-41c0-91c6-572ac03eb410.png)

9. Notice here, we can actually see **uTorrent Transport Protocol** and **BitTorrent DHT Protocol**.
10. Next, right click at the **BitTorrent DHT Protocol**.

![image](https://user-images.githubusercontent.com/70703371/191763896-a3701f6d-f6da-432b-b7b0-ee408c56e4b6.png)

11. Choose `apply as filter` then choose `selected`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/191764109-bbb971b8-c49b-4744-b0d3-81b78f69b544.png)

12. I tried to follow the **udp** streams and found words like -> `torrent.ubuntu.com`. Which does not give us any clue.
13. i checked random packet and at the `transaction ID`, right click at the `value` then choose `apply as column`.

![image](https://user-images.githubusercontent.com/70703371/191768539-e2735089-2439-47f4-b081-103db9dc4c2c.png)

> RESULT

![image](https://user-images.githubusercontent.com/70703371/191769711-ba4dda95-17f7-4d18-a63c-d5421342ae32.png)


14. The info hash caught my attention here.

![image](https://user-images.githubusercontent.com/70703371/191768904-ad843ee9-7825-4f55-a9f1-4ddeec292abb.png)

15. Let's filter it again -> `bt-dht.bencoded.string == "info_hash"`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/191769103-0258c36e-6843-462c-aa2c-ac3f180b9f27.png)

16. 

