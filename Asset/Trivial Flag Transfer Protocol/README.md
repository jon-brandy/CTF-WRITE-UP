# Trivial Flag Transfer Protocol
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Figure out how they moved the [flag]().
## HINT:
1. What are some other ways to hide data?
## STEPS:
1. Since the file given has `.pcap` extension, means we should open it using `wireshark`.

![image](https://user-images.githubusercontent.com/70703371/179132445-9aa22276-0a9a-455b-893a-ec69387615bc.png)

2. Actually the file name does give us a hint (TFTP).
3. Next, let's export it.

> STEPS:

```
file -> export objects -> TFTP
```

![image](https://user-images.githubusercontent.com/70703371/179132721-385ed745-c8bd-4c98-b353-22f088f8fa22.png)

4. Then, choose  `save all` to save them.
5. Next, let's open each one of them.
6. First, i open the `instruction.txt` file.

![image](https://user-images.githubusercontent.com/70703371/179133456-ddcbe1b9-23a1-4498-8b39-a75ee78aca58.png)

7. Paste the text at this [website]() to analyze what cipher text type is this.

![image](https://user-images.githubusercontent.com/70703371/179133531-135c773c-50cc-4995-8cd7-5ac825ade017.png)

8. Then i decoded the text using [this](https://www.dcode.fr/caesar-cipher) website.

> OUTPUT:

```
TFTPDOESNTENCRYPTOURTRAFFICSOWEMUSTDISGUISEOURFLAGTRANSFER.FIGUREOUTAWAYTOHIDETHEFLAGANDIWILLCHECKBACKFORTHEPLAN
```
