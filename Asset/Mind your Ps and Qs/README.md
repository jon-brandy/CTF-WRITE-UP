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

> NOTES:

```
C : Cipher text
P : Factor prime 1
Q : Factor prime 2
E : Public key E
N : Public key value
D : Private key value

```

6. Paste the `N` values there and click `factorize`.

![image](https://user-images.githubusercontent.com/70703371/179345063-3f4c9f81-4466-42ef-9ee6-145163f5047b.png)

> OUTPUT:

```
P : 1461849912200000206276283741896701133693
Q : 431899300006243611356963607089521499045809
```

7. Next, to get the private key value, we need to find the `phi` value first.
8. We can get the `phi` value by using this following formula:

```bash
(p - 1) * (q - 1)
```

```python
import os

os.system('cls')
n = 631371953793368771804570727896887140714495090919073481680274581226742748040342637
e = 65537
c = 421345306292040663864066688931456845278496274597031632020995583473619804626233684
P = 1461849912200000206276283741896701133693
Q = 431899300006243611356963607089521499045809

# get the phi values -> (p - 1) * (q - 1)
phi = (P - 1) * (Q - 1)
print(phi)

```

> OUTPUT:

```
phi : 631371953793368771804570727896887140714061729769155038068711341335911329840163136
```

9. Now, get the private key value by follow this formula:

```python
d = pow(e, -1, phi) # -1 means inverse
```

> OUTPUT:

```
d : 86820026055294556838164569629472617179839240561509150603097892917271661878321409
```

10. Last, we need to get the bytes by follow this formula:

```python
result = pow(c, d, n)
```

> OUTPUT:

```
13016382529449106065927291425342535437996222135352905256639647889241102700065917
```

11. Finally we just have to decode it to an ascii text by using this formula:

```python
print(bytearray.fromhex(hex(result)[2:]).decode('ascii'))
```

> OUTPUT:

```
picoCTF{sma11_N_n0_g0od_55304594}
```

12. Finally we got the flag!

---
## FLAG

```
picoCTF{sma11_N_n0_g0od_55304594}
```

