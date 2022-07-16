# Mind your Ps and Qs
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
In RSA, a small e value can be problematic, but what about N? Can you decrypt this? [values](https://github.com/jon-brandy/CTF-WRITE-UP/blob/5eaa47528ad039a89549be944444270c59725eca/Asset/Mind%20your%20Ps%20and%20Qs/values)
## HINT:
1. Bits are expensive, I used only a little bit over 100 to save money
## STEPS:
1. First, download the file given.
2. Then, check the file type by run `file values`.

![image](https://user-images.githubusercontent.com/70703371/179344921-f9a3a22a-be04-4bfb-af65-a9ef04feec5f.png)

3. Since the file type is `ASCII text`, let's see what's inside by run `cat values`.

![image](https://user-images.githubusercontent.com/70703371/179344951-c7df30c6-521c-4baf-a735-5e79a379f6de.png)

4. Now to decode it, we need the P and Q first, which are the prime numbers that multiplied in order to get the N values.
5. Now to factorize the N values, we can use [this](http://factordb.com/) website.
6. Paste the `N` values there and click `factorize`.

![image](https://user-images.githubusercontent.com/70703371/179345063-3f4c9f81-4466-42ef-9ee6-145163f5047b.png)

> OUTPUT:

```
P : 1461849912200000206276283741896701133693
Q : 431899300006243611356963607089521499045809
```
7. 

