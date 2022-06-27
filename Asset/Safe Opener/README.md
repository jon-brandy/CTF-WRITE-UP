# Safe Opener
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Can you open this safe? 
I forgot the key to my safe but this [program]() is supposed to help me with retrieving the lost key. 
Can you help me unlock my safe? 
Put the password you recover into the picoCTF flag format like: 
`picoCTF{password}`
## HINT:
- NONE
## STEPS:
1. First, download the file given.

```java
import java.io.*;
import java.util.*;  
public class SafeOpener {
    public static void main(String args[]) throws IOException {
        BufferedReader keyboard = new BufferedReader(new InputStreamReader(System.in));
        Base64.Encoder encoder = Base64.getEncoder();
        String encodedkey = "";
        String key = "";
        int i = 0;
        boolean isOpen;
        

        while (i < 3) {
            System.out.print("Enter password for the safe: ");
            key = keyboard.readLine();

            encodedkey = encoder.encodeToString(key.getBytes());
            System.out.println(encodedkey);
              
            isOpen = openSafe(encodedkey);
            if (!isOpen) {
                System.out.println("You have  " + (2 - i) + " attempt(s) left");
                i++;
                continue;
            }
            break;
        }
    }
    
    public static boolean openSafe(String password) {
        String encodedkey = "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz";
        
        if (password.equals(encodedkey)) {
            System.out.println("Sesame open");
            return true;
        }
        else {
            System.out.println("Password is incorrect\n");
            return false;
        }
    }
}
```

2. If you try to analyze the source-code, you will see that there is an encoded base64 strings at line 31.

![Screenshot (496)](https://user-images.githubusercontent.com/70703371/175909369-7c6c3365-8de7-403a-8506-e896dff1d902.png)

3. Encoded base64 strings -> `cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz`.
4. Now to decode it, i opened my kali linux terminal then type this command:

```bash
echo cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz | base64 -d
```

![Screenshot (497)](https://user-images.githubusercontent.com/70703371/175910574-e93d7fc2-35cf-4efe-b712-7a405d9776d7.png)

5. Finally, we just have to wrap the decoded text with `picoCTF{}`.

---
## FLAG
```
picoCTF{pl3as3_l3t_m3_1nt0_th3_saf3}
```
