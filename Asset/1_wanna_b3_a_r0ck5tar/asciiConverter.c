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
