# shark on wire 2
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
We found this [packet capture](). Recover the flag that was pilfered from the network.
## HINT:
- NONE
## STEPS:
1. First, download the file given.
2. Next, since it's a `.pcap` file, let's use wireshark.

![image](https://user-images.githubusercontent.com/70703371/180694259-28b8379a-2021-4998-b174-50019bdb5f2c.png)

3. Now, try to follow the `TCP Stream` in the first green traffic.

![image](https://user-images.githubusercontent.com/70703371/180694522-28bdb7b9-fef9-458a-925c-539afa4ca4d8.png)

4. Seems we got no clue.
5. Them, i tried to follow the `UDP Stream` in this traffic.

![image](https://user-images.githubusercontent.com/70703371/180694626-f4a31fe0-c194-4236-a17f-90be27d7d9dd.png)

> OUTPUT:

![image](https://user-images.githubusercontent.com/70703371/180694680-b1dc98e4-ad57-4428-8054-1a591a646783.png)

6. Still got no clue, now let's check every `stream` since it has 67 streams.

![image](https://user-images.githubusercontent.com/70703371/180694733-6c4540e6-5f80-4302-9dc8-5a4010eb56e3.png)

7. After checked every one of it, something caught my attention.
8. At the **Stream eq 32** and **Stream eq 60**

> STREAM EQ 32

![image](https://user-images.githubusercontent.com/70703371/180695037-94d1e0e8-6685-4936-bad2-ed5d59d32801.png)

> STREAM EQ 60

![image](https://user-images.githubusercontent.com/70703371/180695052-6ae789d8-3cf4-473b-8647-b752b9810f55.png)

9. 
