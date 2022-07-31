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
