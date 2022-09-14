# function overwrite
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Story telling class 2/2 
You can point to all kinds of things in C. 
Checkout our function pointers demo [program](https://github.com/jon-brandy/CTF-WRITE-UP/blob/47628a61a917b3ed17b6fa3cd5ea8543d4991c4f/Asset/function%20overwrite/vuln). You can view source [here](https://github.com/jon-brandy/CTF-WRITE-UP/blob/47628a61a917b3ed17b6fa3cd5ea8543d4991c4f/Asset/function%20overwrite/vuln.c). 
And connect with it using `nc saturn.picoctf.net 54712`
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

28. Now we got segmentation fault and notice we are in the `easy_checker()` function.
29. Means `-16` is the correct value, but if we try to run it again and enter the `num2` as the positive number -> example : 40.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/190180000-742795ee-45c3-4dfd-b1b6-c89232dff5a4.png)


30. We got segmentation vault and we are in the `hard_checker()` function. 
31. Now let's disass the offset.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/190181693-15c54e3f-b282-4e90-9588-4bd7ad3225e9.png)


![image](https://user-images.githubusercontent.com/70703371/190181740-32a7397d-584f-47f8-8132-2a572010811e.png)

32. If we analyze it, this one is the if statements/

![image](https://user-images.githubusercontent.com/70703371/190181951-6195fa1b-f841-4c66-9028-6664175280f7.png)

33. For `jne` stands for `JUMP NOT EQUAL` or `JUMP NOT ZERO`.

![image](https://user-images.githubusercontent.com/70703371/190182266-ea293f16-d085-47c6-ae4d-5aaa413b8a70.png)

34. I think for the second value might be **47**.
35. Let's run the program again using gdb and input the first number as 

> RESULT

![image](https://user-images.githubusercontent.com/70703371/190188968-4bbbe308-f8b4-4961-9661-ac8696262f27.png)

36. I think we got it!
37. Now let's run the netcat.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/190189864-af0a81c2-eaf8-4ef3-81d5-fbbb78d1a2ed.png)

38. Finally, we got the flag!

## FLAG

```
picoCTF{0v3rwrit1ng_P01nt3rs_698c2a26}
```

---


## EXTRA NOTES

1. Since my solution might be not the intended one, because i got it lucky to have 13371337.
2. Based from the scanf buffer -> 127, so it's impossible to go to 13371337, the possible value is `1337`.
3. So divide 1337 by 126 -> we got 10 (in integer, got rounded down). Means need 10 `~`, because `~` ascii is 126.
4. Next, to overwrite the `hard_checker` function to `easy_checker`.

![image](https://user-images.githubusercontent.com/70703371/190193955-7257ebc9-a5b9-4571-9461-b971fb751121.png)

```
hard_checker -> 0x08049436
easy_checker -> 0x080492fc

hard_checker - easy_checker -> 0x13A

-> -314. (value for num2)
```

5. To calculate the first string -> 1337 - (126 * 10) = 77. `M` is 77 ascii representatives.
6. Run the netcat using gdb.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/190196462-58ee3d43-792c-4c4b-8e89-26f38d87015c.png)

7. Got it.

## END OF EXTRA NOTES
