# substitution1
## DESCRIPTION:
A second message has come in the mail, and it seems almost identical to the first one. 
Maybe the same thing will work again. Download the message [here](https://github.com/jon-brandy/CTF-WRITE-UP/blob/c83ad1ad7a81e92be06402dd6d777dbc644ceda3/Asset/substitution1/message.txt).
## HINTS:
1. Try a frequency attack
2. Do the punctuation and the individual words help you make any substitutions?
## STEPS:
1. Download the file given.

```txt
OYAt (txwsy aws ompyksb yxb ajmf) msb m yupb wa owzpkybs tboksgyu owzpbygygwd. Owdybtymdyt msb psbtbdybr lgyx m tby wa oxmjjbdfbt lxgox ybty yxbgs osbmygegyu, yboxdgomj (mdr fwwfjgdf) tqgjjt, mdr pswhjbz-twjegdf mhgjgyu. Oxmjjbdfbt ktkmjju owebs m dkzhbs wa omybfwsgbt, mdr lxbd twjebr, bmox ugbjrt m tysgdf (omjjbr m ajmf) lxgox gt tkhzgyybr yw md wdjgdb towsgdf tbsegob. OYAt msb m fsbmy lmu yw jbmsd m lgrb mssmu wa owzpkybs tboksgyu tqgjjt gd m tmab, jbfmj bdegswdzbdy, mdr msb xwtybr mdr pjmubr hu zmdu tboksgyu fswkpt mswkdr yxb lwsjr aws akd mdr psmoygob. Aws yxgt pswhjbz, yxb ajmf gt: pgowOYA{AS3CK3DOU_4774OQ5_4S3_O001_6B0659AH}
```

3. Using [this](https://www.boxentriq.com/code-breaking/cipher-identifier) online tool, insert the `message.txt` file, so we can identify what type od ciphertext they gave.

![Screenshot (478)](https://user-images.githubusercontent.com/70703371/175464463-a004dd74-b892-499e-aa5f-a6f5352d8e4e.png)

4. The results obtained are as follows:

![Screenshot (479)](https://user-images.githubusercontent.com/70703371/175464567-258df69e-31d9-4ecb-bfcc-e6bab1248d62.png)

5. It can be concluded that the type of ciphertext given is monoalphabetic substitution.
6. Using this [website](https://www.dcode.fr/monoalphabetic-substitution) , we can auto decode the cipher text given.

![Screenshot (480)](https://user-images.githubusercontent.com/70703371/175464738-2976d12e-024c-4505-8f14-9b727c8f3195.png)

7. Choose decrypt automatically, and look at the left side.

![Screenshot (481)](https://user-images.githubusercontent.com/70703371/175464811-524e604c-3e61-4d3f-b775-bb6cab7a1cfe.png)

8. Finally we got the flag!
9. But when you submit the flag, it will says `"Sorry the flag is incorrect"`, based from the hint number 2, try to change the `J` alphabet from the flag to  `Q`
10. So from this `picoCTF{FR3JU3NCY_4774CK5_4R3_C001_6E0659FB}`, to this`picoCTF{FR3QU3NCY_4774CK5_4R3_C001_6E0659FB}`


---
## FLAG
```
picoCTF{FR3QU3NCY_4774CK5_4R3_C001_6E0659FB}
```
