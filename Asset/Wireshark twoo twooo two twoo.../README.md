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
5. Based from the hint, let's check the dns traffic.
6. Change the wireshark query to -> `udp.port == 53`.
7. Then follow this udp stream.

![image](https://user-images.githubusercontent.com/70703371/178516999-e38fce35-fb1b-47b2-8bfb-e4aab80ab58d.png)

8. You can see there's a clue.

![image](https://user-images.githubusercontent.com/70703371/178517171-e7887654-b587-46da-b8ef-a314e32779ae.png)

> CLUE : reddshrimpandherring.com

9. Now let's access the website by type this command on your kali linux terminal:

```php
curl http://www.reddshrimpandherring.com
```
10. Seems we got no clue.
11. 

