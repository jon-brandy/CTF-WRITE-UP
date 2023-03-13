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

7. 
