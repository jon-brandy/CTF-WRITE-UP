# 1_wanna_b3_a_r0ck5tar
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
I wrote you another [song](https://github.com/jon-brandy/CTF-WRITE-UP/blob/c897cbec3902572de751af39e254054130adbec5/Asset/1_wanna_b3_a_r0ck5tar/lyrics.txt). Put the flag in the picoCTF{} flag format.
## HINT:
- NONE
## STEPS:
1. First, download the file given.

> lyrics.txt

```
Rocknroll is right              
Silence is wrong                
A guitar is a six-string        
Tommy's been down               
Music is a billboard-burning razzmatazz!
Listen to the music             
If the music is a guitar                  
Say "Keep on rocking!"                
Listen to the rhythm
If the rhythm without Music is nothing
Tommy is rockin guitar
Shout Tommy!                    
Music is amazing sensation 
Jamming is awesome presence
Scream Music!                   
Scream Jamming!                 
Tommy is playing rock           
Scream Tommy!       
They are dazzled audiences                  
Shout it!
Rock is electric heaven                     
Scream it!
Tommy is jukebox god            
Say it!                                     
Break it down
Shout "Bring on the rock!"
Else Whisper "That ain't it, Chief"                 
Break it down 
```

2. Next i did the same steps as the `mus1c` challenge by paste the strings to [this](https://codewithrockstar.com/online) website.

> RESULTS

![image](https://user-images.githubusercontent.com/70703371/182017070-7d770cda-577d-4941-ae73-2345db7be14f.png)

3. Well, it seems we must figure out another way.
4. For this solution, i convert it to `.c` code.

> BEFORE

```
Rocknroll is right              
Silence is wrong                
A guitar is a six-string        
Tommy's been down               
Music is a billboard-burning razzmatazz!
Listen to the music             
If the music is a guitar                  
Say "Keep on rocking!" 
```

> AFTER

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    bool rocknroll = true;
    bool silence = false;
    int aGuitar = 136;
    int tommy = 4;
    int music = 1970;
    int theMusic;
    scanf("%d", &theMusic);
    getchar();
    if(theMusic == aGuitar)
    {
        printf("Keep on rocking!");
    }

    return 0;
}
```

> NOTES

```
Words with 10 or more characters are count as 0.
Since -> razzmatazz! -> are <= 10, so it will count as 0.
```

5. `right` -> `true` , `wrong` -> `false` , `a six string` -> `a: 1` , `six: 3` , `string: 6`.
6. `a billboard-burning razzmatazz!` -> `1970`.
7. `Listen` -> `scanf` , `if` -> `if`.
8. Now for these lines.

> BEFORE

```
Listen to the rhythm
If the rhythm without Music is nothing
Tommy is rockin guitar
Shout Tommy!                    
Music is amazing sensation 
Jamming is awesome presence
Scream Music!                   
Scream Jamming!                 
Tommy is playing rock           
Scream Tommy!       
They are dazzled audiences                  
Shout it!
Rock is electric heaven                     
Scream it!
Tommy is jukebox god            
Say it!                                     
Break it down
Shout "Bring on the rock!"
Else Whisper "That ain't it, Chief"                 
Break it down 
```

> AFTER (CONCATE THE PREVIOUS LINES)

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    bool rocknroll = true;
    bool silence = false;
    int aGuitar = 136;
    int tommy = 4;
    int music = 1970;
    int theMusic;
    scanf("%d", &theMusic);
    getchar();
    if(theMusic == aGuitar)
    {
        printf("Keep on rocking!\n");
    }
    int rhytm;
    scanf("%d", &rhytm);
    getchar();
    if(rhytm - music == 0)
    {
        tommy = 66; // rockin guitar
        printf("%d\n", tommy);
        music = 79; // amazing sensation
        int jamming = 78; // awesome presence
        printf("%d\n", music);
        printf("%d\n", jamming);
        tommy = 74; // playing rock
        printf("%d\n", tommy);
        int they = 79;// They are dazzled audiences
        printf("it\n"); // refers to print the int they
        printf("%d\n", they);
        int rock = 86; // electric heaven
        printf("it\n"); //refers to print the int rock
        printf("%d\n", rock);
        tommy = 73; // jukebox god
        puts("it"); // refers to print the int tommy
        printf("%d\n", tommy);
        //break;
        puts("Bring on the rock!");
    }
    else
    {
        printf("That ain't it, Chief!");
        //break;
    }

    return 0;
}
```

9. Run the final code.

> FIRST INPUT

```
136
```

> SECOND INPUT

```
1970
```

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/182018557-9dfd4423-edc2-4530-a24c-b2edec5b1536.png)

10. Now take all the ASCII code and convert it to a char.

> CODE

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    int ascii[] = {66,79,78,74,79,86,73};
    for(int i = 0; i < 7; i++)
    {
        printf("%c", ascii[i]);
    }

    return 0;
}
```

> OUTPUT


![image](https://user-images.githubusercontent.com/70703371/182018740-09d80312-7035-484b-b382-32cd9663b57a.png)

11. Finally we got the flag!

> WRAP THE FLAG WITH picoCTF{}

---

## FLAG

```
picoCTF{BONJOVI}
```


