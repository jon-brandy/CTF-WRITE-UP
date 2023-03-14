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
17. To make it clear, let's try to run it with gdb and set few breakpoints.

> RESULT




