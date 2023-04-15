# FindAndOpen
> Write-up author: vreshco
## DESCRIPTION:
Someone might have hidden the password in the trace file. Find the key to unlock this file. This tracefile might be good to analyze.
## HINT:
- Download the pcap and look for the password or flag.
- Don't try to use a password cracking tool, there are easier ways here.
## STEPS:
1. Given 2 files -> pcap and zip files.
2. Based from the description, it seems we need to find the password to unzip the zipped flag.
3. Let's analyzing the pcap file.

![image](https://user-images.githubusercontent.com/70703371/232222277-04c9470f-3528-4f84-b0b0-358ffc22054a.png)


4. The protocol names caught my attention, after decode all the hex values, got this -> `he1CLKsa1M`.
5. But after entered the value we got, it says incorrect.
6. Remembering there's 1 protocol that are not redundant.

![image](https://user-images.githubusercontent.com/70703371/232222799-9674cbd8-64a0-47a7-a36c-a49c58afa1ac.png)


7. Let's check the data.

![image](https://user-images.githubusercontent.com/70703371/232222876-3b106b12-3977-453a-984e-3dfabe38561c.png)


8. Retrieve the values.

![image](https://user-images.githubusercontent.com/70703371/232223103-184a9460-03cb-401e-9260-a14d2283b636.png)


9. Hmm it holds value that looks like a base64 encoded text.
10. Let's decode that.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/232223223-bb49a3ef-6169-4b3d-8265-5083a398d133.png)


11. Got the key! Let's use it.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/232223256-b526b193-684c-4cb8-a120-16800553b5d3.png)


12. Got the flag!

## FLAG

```
picoCTF{R34DING_LOKd_fil56_succ3ss_419835ef}
```


