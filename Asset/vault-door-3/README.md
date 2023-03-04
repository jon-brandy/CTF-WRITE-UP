# vault-door-3
> Write-up author: jon-brandy
## DESCRIPTION:
This vault uses for-loops and byte arrays. The source code for this vault is here: VaultDoor3.java
## HINT:
- NONE
## STEPS:
1. Given a .java source code.

```java
import java.util.*;

class VaultDoor3 {
    public static void main(String args[]) {
        VaultDoor3 vaultDoor = new VaultDoor3();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
	String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
	if (vaultDoor.checkPassword(input)) {
	    System.out.println("Access granted.");
	} else {
	    System.out.println("Access denied!");
        }
    }

    // Our security monitoring team has noticed some intrusions on some of the
    // less secure doors. Dr. Evil has asked me specifically to build a stronger
    // vault door to protect his Doomsday plans. I just *know* this door will
    // keep all of those nosy agents out of our business. Mwa ha!
    //
    // -Minion #2671
    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        char[] buffer = new char[32];
        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
        String s = new String(buffer);
        return s.equals("jU5t_a_sna_3lpm18g947_u_4_m9r54f");
    }
}
```

2. Analyzing the `checkPassword` function, seems like we can get the flag by following the loop manually or simply write the same script in javascript.

> JAVASCRIPT

```js
var password = "jU5t_a_sna_3lpm18g947_u_4_m9r54f"
var i;
var buffer = Array(32);
for (i = 0; i < 8; i++) 
{
    buffer[i] = password.charAt(i);
}

for (; i < 16; i++) 
{
    buffer[i] = password.charAt(23-i);
}

for (; i < 32; i += 2) {
    buffer[i] = password.charAt(46-i);
}

for (i = 31; i >= 17; i -= 2) 
{
    buffer[i] = password.charAt(i);
}
//wrap the result with the flag prefix
console.log("picoCTF{" + buffer.join("") + "}");
```

> RESULT

![image](https://user-images.githubusercontent.com/70703371/222884887-b0e56354-27f3-4911-aa23-207c09afa262.png)


3. Got the flag!

## FLAG

```
picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_79958f}
```

