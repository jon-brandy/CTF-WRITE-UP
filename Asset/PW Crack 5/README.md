# PW Crack 5
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Can you crack the password to get the flag? 
Download the password checker [here](https://github.com/jon-brandy/CTF-WRITE-UP/blob/e3c973166d9c560e0d30662a42b69f4baded6c2e/Asset/PW%20Crack%205/level5.py) and you'll need the encrypted [flag](https://github.com/jon-brandy/CTF-WRITE-UP/blob/e3c973166d9c560e0d30662a42b69f4baded6c2e/Asset/PW%20Crack%205/level5.flag.txt.enc) and the [hash](https://github.com/jon-brandy/CTF-WRITE-UP/blob/e3c973166d9c560e0d30662a42b69f4baded6c2e/Asset/PW%20Crack%205/level5.hash.bin) in the same directory too. 
Here's a [dictionary](https://github.com/jon-brandy/CTF-WRITE-UP/blob/e3c973166d9c560e0d30662a42b69f4baded6c2e/Asset/PW%20Crack%205/dictionary.txt) with all possible passwords based on the password conventions we've seen so far.
## HINTS:
1. Opening a file in Python is crucial to using the provided dictionary.
2. You may need to trim the whitespace from the dictionary word before hashing. Look up the Python string function, `strip`.
3. The `str_xor` function does not need to be reverse engineered for this challenge.
## STEPS:
1. First, download all the files given in the same directory.
2. Then open the python code.

```

```



https://play.picoctf.org/practice/challenge/249?category=5&page=3

