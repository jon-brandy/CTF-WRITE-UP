# Wireshark twoo twooo two twoo...
## DESCRIPTION:
Can you find the flag? [shark2.pcapng]().
## HINTS:
1. Did you really find _the_ flag?
2. Look for traffic that seems suspicious.
## STEPS:
1. First, open the file using wireshark.
2. When i tried to follow the tcp stream at `tcp.stream eq 5`. I found a clue.

![image](https://user-images.githubusercontent.com/70703371/178130750-4eed2bfa-4902-4082-81ed-995db59a9f27.png)

3. Then, when i followed the tcp stream at `tcp.stream eq 19`. I found a flag.

![image](https://user-images.githubusercontent.com/70703371/178130828-401135db-2369-48b2-a639-f6b4fa6910d9.png)

4. But the pico server reject it, means it's not the flag.
