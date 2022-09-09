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

6. Seems, there's few important clues.

> CLUES

![image](https://user-images.githubusercontent.com/70703371/189390610-a0927167-c226-47cb-8027-8e3db011a487.png)


8. Because the chars always shuffled, so the dictionary does the same.

> DICTIONARY

![image](https://user-images.githubusercontent.com/70703371/189391210-f0b2196f-a325-4c95-b84c-a3bfd132ed35.png)

9. Luckily there's an online [tools](https://quipqiup-com.translate.goog/?_x_tr_sl=auto&_x_tr_tl=id&_x_tr_hl=en&_x_tr_pto=op,wapp) that can help us to solve this type of cryptography.

> THE WEBSITE

![image](https://user-images.githubusercontent.com/70703371/189392957-c8662905-fc06-496f-b5d2-aff067e95448.png)

10. To use this, print the `dictionary` at the python script.
11. Copy the output and paste it on the website as `CLUES`.
12. For the puzzle, simply paste the output from the `flag.txt` strings.
13. Don't forget to remove the semicolon `{` , `}` and change `a = x` not `:` & `'`.

![image](https://user-images.githubusercontent.com/70703371/189394445-daa1f957-cca3-4912-b36c-d622a9b4fd8d.png)

14. Press the solve button.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/189394544-1442d9f5-03b9-48c4-89b9-53fab5dc5211.png)


15. Finally, we got the flag! 
16. Wrap the flag with `picoCTF{}`.

## FLAG

```
picoCTF{perhaps_the_dog_jumped_over_was_just_tired}
```


