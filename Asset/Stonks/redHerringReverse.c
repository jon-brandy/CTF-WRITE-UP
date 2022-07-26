#include <stdio.h>
#include <string.h>

char *str = "ocip{FTC0l_I4_t5m_ll0m_y_y3n5406d06dÿ¥o}";

int main(void)
{
    int len = strlen(str);
    int x = len;
    int i = 0;
    int k = 0;
    int l = 0;
    char output[len + 1];
    char tmp[4];
    while (l < len)
    {
        k = 0;
        for (int j = 0 + i; j < 4 + i; j++)
        {
            tmp[k++] = str[j];
            x--;
            if (x < 1)
                break;
        }
        for (int j = k - 1; j >= 0; j--)
        {
            output[l++] = tmp[j];
        }
        i += 4;
    }
    output[len] = '\0';
    printf("%s\n", output);
}
