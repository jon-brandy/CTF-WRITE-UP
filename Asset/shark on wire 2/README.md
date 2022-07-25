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

9. Seems like at **Stream eq 32** it has different source.

![image](https://user-images.githubusercontent.com/70703371/180695235-e5565ad4-fbd3-4977-b247-4f35159e69fd.png)

10. Let's filter the ip by type this at the filter area -> `ip.addr == 10.0.0.66`.

![image](https://user-images.githubusercontent.com/70703371/180695398-a3b77a23-25fd-4c51-a710-db6bccab389d.png)

11. Notice at the `start` packet it srouce port value is **5000**. Then the next stream `eq` has different value.

![image](https://user-images.githubusercontent.com/70703371/180696689-5aa14c25-277c-4bc9-bead-e517e54c03f1.png)

![image](https://user-images.githubusercontent.com/70703371/180696654-f6a443bc-ec56-43f3-bd82-d778588be998.png)

![image](https://user-images.githubusercontent.com/70703371/180696719-bf9e18bf-63ed-46a1-af60-0e702aca1d52.png)

12. And so on.
13. I think the clue we are looking for is the `source port` value between **stream eq** and **stream eq 60**.

![image](https://user-images.githubusercontent.com/70703371/180696914-24b3a29b-13d7-4e08-881f-edc2d90b40cd.png)


> RESULT:

**NOTES** : 5000 - [CURR_SOURCE-PORT_VALUE]

```
112 105 99 111 67 84 70 123 112 49 76 76 102 51 114 51 100 95 100 95 100 97 116 97 95 118 49 97 95 115 116 51 103 48 125
```

14. I think it's a ASCII code, let's convert it to strings.
15. For this solution i used this `c` code.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    system("cls");
    char asciiCode[] = {112, 105, 99, 111, 67, 84, 70, 123, 112, 49, 76, 76, 102, 51, 114, 51,
           100, 95, 100, 95, 100, 97, 116, 97, 95, 118, 49, 97, 95, 115, 116, 51, 103, 48, 125};

    for(int i = 0; i < sizeof(asciiCode); i++)
    {
        printf("%c", asciiCode[i]);
    }
}


```

> OUTPUT:

![image](https://user-images.githubusercontent.com/70703371/180697978-11d2fbf1-c5fd-42b7-a57b-0ea3aa1bc30f.png)

16. Remove these extra characters:

![image](https://user-images.githubusercontent.com/70703371/180698311-438f983a-7920-41aa-a856-28e5fdc5fca9.png)

17. Finally we got the flag!
---
## FLAG

```
picoCTF{p1LLf3r3d_data_v1a_st3g0}
```
