# sharks on wire 1
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
We found this [packet capture](). Recover the flag.
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

4. For 
