# spelling-quiz
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
I found the flag, but my brother wrote a program to encrypt all his text files. 
He has a spelling quiz study guide too, but I don't know if that helps.

[public.zip](https://github.com/jon-brandy/CTF-WRITE-UP/blob/17f15926335683e999edce684ecd75e0c71e49cb/Asset/spelling-quiz/public.zip)

## HINT:
- NONE
## STEPS:
1. First, download the `.zip` file given.
2. Next, unzip the `.zip` file.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/189383293-540e14ee-860e-49cb-8f1d-4d9b0f9e7d8d.png)

3. Go to the `public` folder.

> INSIDE

![image](https://user-images.githubusercontent.com/70703371/189383630-e14aa95d-1a99-4e43-8371-282b7693cb94.png)

4. Let's see what's inside the `flag.txt` file.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/189384048-4eb3ea2e-87f2-4ad3-a692-b1babcb7f3bb.png)

5. Anyway, let's dive to the python script.

> ENCRYPT.PY

```py
import random
import os

files = [
    os.path.join(path, file)
    for path, dirs, files in os.walk('.')
    for file in files
    if file.split('.')[-1] == 'txt'
]

alphabet = list('abcdefghijklmnopqrstuvwxyz')
random.shuffle(shuffled := alphabet[:])
dictionary = dict(zip(alphabet, shuffled))

for filename in files:
    text = open(filename, 'r').read()
    encrypted = ''.join([
        dictionary[c]
        if c in dictionary else c
        for c in text
    ])
    open(filename, 'w').write(encrypted)

```
