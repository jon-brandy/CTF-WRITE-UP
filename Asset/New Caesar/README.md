# New Caesar
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
We found a brand new type of encryption, can you break the secret code? (Wrap with picoCTF{}) 
`apbopjbobpnjpjnmnnnmnlnbamnpnononpnaaaamnlnkapndnkncamnpapncnbannaapncndnlnpna`
[new_caesar.py](https://github.com/jon-brandy/CTF-WRITE-UP/blob/a9cc252bf66287d2f6ddd7103c02a7c458f81c24/Asset/New%20Caesar/new_caesar.py)
## HINTS:
1. How does the cipher work if the alphabet isn't 26 letters?
2. Even though the letters are split up, the same paradigms still apply
## STEPS:
1. First, download the `.py` script given.
2. Next, let's analyze the script.

> NEW_CAESAR.PY

```py
import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
	return enc

def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]

flag = "redacted"
key = "redacted"
assert all([k in ALPHABET for k in key])
assert len(key) == 1

b16 = b16_encode(flag)
enc = ""
for i, c in enumerate(b16):
	enc += shift(c, key[i % len(key)])
print(enc)
```

3. 
