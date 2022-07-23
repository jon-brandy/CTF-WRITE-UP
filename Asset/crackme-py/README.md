# crackme-py
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
[crackme.py]()
## HINT:
- NONE
## STEPS:
1. First, download the file given.
2. Next, try to view the source-code.

```py
# Hiding this really important number in an obscure piece of code is brilliant!
# AND it's encrypted!
# We want our biggest client to know his information is safe with us.
bezos_cc_secret = "A:4@r%uL`M-^M0c0AbcM-MFE02fh3e4a5N"

# Reference alphabet
alphabet = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"+ \
            "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"



def decode_secret(secret):
    """ROT47 decode

    NOTE: encode and decode are the same operation in the ROT cipher family.
    """

    # Encryption key
    rotate_const = 47

    # Storage for decoded secret
    decoded = ""

    # decode loop
    for c in secret:
        index = alphabet.find(c)
        original_index = (index + rotate_const) % len(alphabet)
        decoded = decoded + alphabet[original_index]

    print(decoded)



def choose_greatest():
    """Echo the largest of the two numbers given by the user to the program

    Warning: this function was written quickly and needs proper error handling
    """

    user_value_1 = input("What's your first number? ")
    user_value_2 = input("What's your second number? ")
    greatest_value = user_value_1 # need a value to return if 1 & 2 are equal

    if user_value_1 > user_value_2:
        greatest_value = user_value_1
    elif user_value_1 < user_value_2:
        greatest_value = user_value_2

    print( "The number with largest positive magnitude is "
        + str(greatest_value) )



choose_greatest()
```

3. Then i tried to run it and follow what's the program asks me.

> OUTPUT:

![image](https://user-images.githubusercontent.com/70703371/180608353-b26171e6-45fc-4d16-b808-65ef88be2af6.png)

4. Then i'm curious what if i run the `decode_secret` function and put the paramter as `bezos_cc_secret` variable.

```py
decode_secret(bezos_cc_secret)
```

5. Finally we got the flag!

![image](https://user-images.githubusercontent.com/70703371/180608421-44babdc2-daa9-4e97-b2a2-a5a0a20c9a3a.png)


---
## FLAG

```
picoCTF{1|\/|_4_p34|\|ut_a79b6c2d}
```
