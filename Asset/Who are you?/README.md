# Who are you?
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Let me in. Let me iiiiiiinnnnnnnnnnnnnnnnnnnn 
http://mercury.picoctf.net:34588/
## HINT:
1. It ain't much, but it's an RFC https://tools.ietf.org/html/rfc2616
## STEPS:
1. First, open the link given.

![image](https://user-images.githubusercontent.com/70703371/182081010-82b3b6c2-355c-4310-84c7-588f05c1c680.png)

2. Seems we have to change the `user-agent` value.
3. For this solution i used `burpsuite`. So i paste the url using `burpsuite` browser.

> CHOOSE SEND TO REPEATER

![image](https://user-images.githubusercontent.com/70703371/182081571-109120dc-b5c2-438d-af16-00cf88ffa9cc.png)

> OPEN REPEATER TAB CLICK THE SEND BUTTON

![image](https://user-images.githubusercontent.com/70703371/182081623-6d47c5d2-3e70-436a-9769-187d65d1b82a.png)

4. Change the `user-agent` value to `PicoBrowser` then click the `send` button again.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/182081891-1f304a8d-a0c5-4605-9584-329e5117a5ee.png)

5. Since they don't trust us, now change the va
