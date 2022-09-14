# function overwrite
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Story telling class 2/2 
You can point to all kinds of things in C. 
Checkout our function pointers demo [program](https://github.com/jon-brandy/CTF-WRITE-UP/blob/47628a61a917b3ed17b6fa3cd5ea8543d4991c4f/Asset/function%20overwrite/vuln). You can view source [here](https://github.com/jon-brandy/CTF-WRITE-UP/blob/47628a61a917b3ed17b6fa3cd5ea8543d4991c4f/Asset/function%20overwrite/vuln.c). 
And connect with it using `nc saturn.picoctf.net 54627`
## HINT:
1. Don't be so negative
## STEPS:
1. First, download both files given.
2. Next, let's check the file type of the `program`.

> RESULT


![image](https://user-images.githubusercontent.com/70703371/189645861-3bf1b93a-dbc4-453a-84ab-25efe35503ab.png)


3. It's an ELF 32 bit and **not stripped** , means we can see the functions name.
4. Now let's check the file protector.

> RESULT


![image](https://user-images.githubusercontent.com/70703371/189645915-39435f02-0d7e-4655-aeca-074aac836f33.png)


5. **No canary** and **no pie**.
6. Let's make the program executeable by run ->  `chmod +x vuln`.
7. Now let's run the program without the gdb.
8. Let's input values the program want.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/189645969-8fe297d5-7054-4a6b-8b37-a9ddd0fc1ee1.png)


9. Let's analyze the source code then.

> VULN.C

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <wchar.h>
#include <locale.h>

#define BUFSIZE 64
#define FLAGSIZE 64

int calculate_story_score(char *story, size_t len)
{
  int score = 0;
  for (size_t i = 0; i < len; i++)
  {
    score += story[i];
  }

  return score;
}

void easy_checker(char *story, size_t len)
{
  if (calculate_story_score(story, len) == 1337)
  {
    char buf[FLAGSIZE] = {0};
    FILE *f = fopen("flag.txt", "r");
    if (f == NULL)
    {
      printf("%s %s", "Please create 'flag.txt' in this directory with your",
                      "own debugging flag.\n");
      exit(0);
    }

    fgets(buf, FLAGSIZE, f); // size bound read
    printf("You're 1337. Here's the flag.\n");
    printf("%s\n", buf);
  }
  else
  {
    printf("You've failed this class.");
  }
}

void hard_checker(char *story, size_t len)
{
  if (calculate_story_score(story, len) == 13371337)
  {
    char buf[FLAGSIZE] = {0};
    FILE *f = fopen("flag.txt", "r");
    if (f == NULL)
    {
      printf("%s %s", "Please create 'flag.txt' in this directory with your",
                      "own debugging flag.\n");
      exit(0);
    }

    fgets(buf, FLAGSIZE, f); // size bound read
    printf("You're 13371337. Here's the flag.\n");
    printf("%s\n", buf);
  }
  else
  {
    printf("You've failed this class.");
  }
}

void (*check)(char*, size_t) = hard_checker;
int fun[10] = {0};

void vuln()
{
  char story[128];
  int num1, num2;

  printf("Tell me a story and then I'll tell you if you're a 1337 >> ");
  scanf("%127s", story);
  printf("On a totally unrelated note, give me two numbers. Keep the first one less than 10.\n");
  scanf("%d %d", &num1, &num2);

  if (num1 < 10)
  {
    fun[num1] += num2;
  }

  check(story, strlen(story));
}
 
int main(int argc, char **argv)
{

  setvbuf(stdout, NULL, _IONBF, 0);

  // Set the gid to the effective gid
  // this prevents /bin/sh from dropping the privileges
  gid_t gid = getegid();
  setresgid(gid, gid, gid);
  vuln();
  return 0;
}

```

10. Looks like we found the vuln here.

![image](https://user-images.githubusercontent.com/70703371/189648245-1b5fe43f-3fda-4677-9cb7-0d308dfa87a7.png)

11. Since the `fun` has 10 buffer and the if statements validate that the input for num1 must be less than 10.
12. Then the number will be the index of the `fun` buffer.
13. Notice here, we can input **minus** integer value.
14. Basically the goal is to overwrite this check function pointer.

![image](https://user-images.githubusercontent.com/70703371/190168375-4957f653-d29e-445e-a09a-c4a82d1d1007.png)

15. Because we want to call the `easy_check()` function not the `hard_check()`. Because it is impossible to reach this value.

![image](https://user-images.githubusercontent.com/70703371/190168914-3ee69ec1-3218-48cd-9156-7ec3263e0cd9.png)


16. Let's run the program using gdb.

> GDB


![image](https://user-images.githubusercontent.com/70703371/189650104-86302580-36a1-4064-a999-bd07563f102b.png)


17. Let's open the program using cutter.

![image](https://user-images.githubusercontent.com/70703371/190163409-077c7bdb-a6e3-47a3-975a-2707a87ba92c.png)


18. Let's open the `vuln()` function, because we need to identify what's the correct value for the `num1` and the correct value for the `num2`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/190163822-79067ba4-00c3-4117-b733-f72ae1158174.png)


19. This must be the `strlen()` function, because there's strlen to call.

> STRLEN FUNCTION'S OFFSET

![image](https://user-images.githubusercontent.com/70703371/190164211-bc914826-c881-4d9b-9145-b0c3cabd1111.png)

20. And this must be the `check()` function.

> CHECK FUNCTION'S OFFSET

![image](https://user-images.githubusercontent.com/70703371/190164461-c2d786c9-6ef8-496f-96f3-95d8beace5f2.png)

21. Also this must be the if statements, because there's a `cmp` which stands for comparing and `jg` which stands for **jump if greater than**.

> THE IF STATMENTS'S OFFSET

![image](https://user-images.githubusercontent.com/70703371/190164970-198e2960-4068-4f64-a082-384ed64e88e3.png)

22. To define the correct **minus** value for `num1` is count from the stack of index 1 until the offset of the `check()` function.

> START OF FUN[0] -> FUN INDEX 0

![image](https://user-images.githubusercontent.com/70703371/190165738-9a1206f6-81fe-4b64-978e-a5c1bde38d4d.png)

> INDEX OF 1

![image](https://user-images.githubusercontent.com/70703371/190166209-3284eea2-56ca-48ee-ae7e-1135687c3de9.png)

> COUNT == 16

![image](https://user-images.githubusercontent.com/70703371/190166392-cabe1f41-322a-4e90-a4ed-61e5a4d2f391.png)

23. For the `num1` must be 16.
24. Now for the `num2`, since i didn't know how to get the number, so maybe i will try a bruteforce way.
25. But let's make sure the first number are the correct one.
26. So i tried to input **-12** as the first number and **-40** as the second number.

> RUN THE PROGRAM USING GDB

![image](https://user-images.githubusercontent.com/70703371/190174893-287dc949-01f1-4a1c-80d1-a529960ddc8e.png)

27. It exited normally, now let's run again but this time add 4 bytes -> `-16`.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/190175056-3c9d362d-b095-4c50-b875-b4092ab6821d.png)

28. Now we got segmentation fault.
29. Means `-16` is the correct value, but notice they don't specify wheter the `num2` are positive or negative.
30. 
```
