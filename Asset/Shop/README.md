# Shop
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Best Stuff - Cheap Stuff, Buy Buy Buy... Store Instance: [source](https://github.com/jon-brandy/CTF-WRITE-UP/blob/99ff48d928990503eb7ceaeb39ca31875b3a24ab/Asset/Shop/source). The shop is open for business at `nc mercury.picoctf.net 24851`.
## HINT:
- Always check edge cases when programming
## STEPS:
1. First, download the file given.
2. Now, let's check the file type.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/189481826-67c7af56-d10a-474b-be2a-ee2c97e6ca09.png)

3. Since it's an executable file and **not stripped**.
4. Let's run the file in gdb, but make it executable first by run -> `chmod +x source`.

> GDB

![image](https://user-images.githubusercontent.com/70703371/189481878-5eee7a22-7306-4703-a953-6b942582f8dd.png)

5. It seems, somehow we need to manipulate the money so we can buy the fruitful flag.

![image](https://user-images.githubusercontent.com/70703371/189481944-0e9d8efb-dbd3-4f6d-9138-08882d1c13ba.png)

6. So i tried to enter **minus** value.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/189482259-85344c47-d557-42e6-80d2-132d38fbb5b5.png)

![image](https://user-images.githubusercontent.com/70703371/189482317-3f490dd8-2697-486f-ad63-39e9ff865c98.png)


7. Looks like it is just simple reverse engineering challenge.
8. Now let's run the netcat and do the same method.

> NETCAT

![image](https://user-images.githubusercontent.com/70703371/189482332-ece11a42-1948-4fa2-b7a5-6e82b4ec1b50.png)

9. Convert the list of ascii into characters.

```c
#include <stdio.h>

int main(void)
{
    char flag[] = {112, 105, 99, 111, 67, 84, 70, 123, 98, 52, 100, 95, 98, 114, 111, 103, 114, 97, 109, 
    109, 101, 114, 95, 53, 51, 50, 98, 99, 100, 57, 56, 125};
    
    for(int i = 0; i < strlen(flag); i++)
    {
        printf("%c", flag[i]);
    }

    return 0;
}
```

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/189483484-2a73bb20-6517-40da-80fa-21e235809ac0.png)


## FLAG

```
picoCTF{b4d_brogrammer_532bcd98}
```
