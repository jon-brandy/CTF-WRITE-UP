# miniRSA
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Let's decrypt this: [ciphertext](https://github.com/jon-brandy/CTF-WRITE-UP/blob/c59551a545e2834314df5344ab22821e5e9dd8dc/Asset/miniRSA/ciphertext)? Something seems a bit small.
## HINTS:
1. RSA [tutorial](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
2. How could having too small an e affect the security of this 2048 bit key?
3. Make sure you don't lose precision, the numbers are pretty big (besides the e value)
## STEPS:
1. First, download the file given.

> INSIDE THE FILE:

![image](https://user-images.githubusercontent.com/70703371/180776678-10849a01-2507-45f4-96ff-90296b065d83.png)

```
N:293319224997949857827359760455911649366830593805589503865601601057403432015133699390063075311659227089496191626986644733509404865074517712234358352601689712100874708944484607455939568405865305279158025414500929465746948095848808966661831206214072463985180989811064312192076978702934121764404829001835504673751902398984552011708314104604838294486034
e: 3
ciphertext (c): 2205316413931134031074603746928247799030155221252519872649649212867614751848436763801274360463406171247185741761825125
```
