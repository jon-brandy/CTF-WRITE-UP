# waves over lambda
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
We made a lot of substitutions to encrypt this. Can you decrypt it? Connect with `nc jupiter.challenges.picoctf.org 13758`.
## HINT:
1. Flag is not in the usual flag format
## STEPS:
1. First, run the following netcat command -> `nc jupiter.challenges.picoctf.org 13758` at your kali linux terminal.

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/180772967-f74d6406-0e82-4bc3-8d4c-5f8bf488a542.png)

2. Since it's a substitution cipher text, i used [this](https://www.guballa.de/substitution-solver) website to decode it. 
3. Simply paste all the strings inside the `.txt` file, then press the `break` button.
4. Don't forget to change the language to `english`.

> OUTPUT:

```
congrats here is your flag - frequency_is_c_over_lambda_dnvtfrtayu
-------------------------------------------------------------------------------
between us there was, as i have already said somewhere, the bond of the sea. besides holding our hearts together throawyerthe best of old fellowshad, because of his many years and many virtues, the only cushion on deck, and was lying . marlow sat cross-legged right aft, leaning against the mizzen-mast. he had sunken cheeks, a yellow complexion, a st, satisfied the anchor had good hold, made his way aft and sat down amongst us. we exchanged a few words lazily. afteditative, and fit for nothing but placid staring. the day was ending in a serenity of still and exquisite brilliance.essex marsh was like a gauzy and radiant fabric, hung from the wooded rises inland, and draping the low shores in diaed by the approach of the sun.

```

5. Finally, we got the flag!

---

## FLAG

```
frequency_is_c_over_lambda_dnvtfrtayu
```
