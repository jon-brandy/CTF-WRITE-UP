# not-crypto
> Write-up author: jon-brandy
## DESCRIPTION:
there's crypto in here but the challenge is not crypto... 🤔
## HINT:
-
## STEPS:
1. Given a stripped 64 bit binary file.

![image](https://user-images.githubusercontent.com/70703371/222663411-3edf45fc-d717-4807-b16b-bc5e4d49f456.png)


2. Let's try to run the binary in gdb.

> CHECKING ALL THE FUNCS AVAIL

![image](https://user-images.githubusercontent.com/70703371/222663997-a2ab4da9-7a64-47d1-81c0-16efad500a91.png)


3. Notice the symbols address is an offset, which means we need to at least run the binary once to get the actual address.
4. Let's set a random breakpoint first (note the breakpoint shall not interfere with the symbols) so we can check the addresses again.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/222664362-56f0cf0d-ff0c-442d-9023-c300ba9a3cfc.png)


![image](https://user-images.githubusercontent.com/70703371/222664407-df9f0299-cae6-4c32-a583-392d2224fbcf.png)


5. Great, let's start by set a breakpoint at the `memcmp` functions to see any leaked comparing values.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/222664907-8962d3d3-c5de-45e8-95d7-1656b7130d81.png)

> Let's enter any strings.

![image](https://user-images.githubusercontent.com/70703371/222665056-06a07490-fb1e-4855-bc4d-83b82540570a.png)


> RESULT 

![image](https://user-images.githubusercontent.com/70703371/222665105-8cb9417f-bb30-4bfb-8a50-ac84173c60d6.png)


6. Notice at the **RDI** register, the flag is leaked.
7. Got the flag!

## FLAG

```
picoCTF{c0mp1l3r_0pt1m1z4t10n_15_pur3_w1z4rdry_but_n0_pr0bl3m?}
```




