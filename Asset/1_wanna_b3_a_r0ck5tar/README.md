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

5. `right` -> `true` , `wrong` -> `false` , `a six string` -> `a: 1` , `six: 3` , `string: 6`.
