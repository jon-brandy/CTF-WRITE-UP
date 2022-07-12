# Wireshark twoo twooo two twoo...
## DESCRIPTION:
Can you find the flag? [shark2.pcapng]().
## HINTS:
1. Did you really find _the_ flag?
2. Look for traffic that seems suspicious.
## STEPS:
1. First, open the file using wireshark.
2. When i tried to follow the tcp stream at `tcp.stream eq 5`. I found a clue.

![image](https://user-images.githubusercontent.com/70703371/178130750-4eed2bfa-4902-4082-81ed-995db59a9f27.png)

3. Then, when i followed the tcp stream at `tcp.stream eq 19`. I found a flag.

![image](https://user-images.githubusercontent.com/70703371/178130828-401135db-2369-48b2-a639-f6b4fa6910d9.png)

4. But the pico server reject it, means it's not the flag.
5. Based from the hint, let's check the dns traffic.
6. Change the wireshark query to -> `udp.port == 53`.
7. Then follow this udp stream.

![image](https://user-images.githubusercontent.com/70703371/178516999-e38fce35-fb1b-47b2-8bfb-e4aab80ab58d.png)

8. You can see there's a clue.

![image](https://user-images.githubusercontent.com/70703371/178517171-e7887654-b587-46da-b8ef-a314e32779ae.png)

> CLUE : reddshrimpandherring.com

9. Now let's access the website by type this command on your kali linux terminal:

```php
curl http://www.reddshrimpandherring.com
```

> OUTPUT:

```html
<html>
        <head>
                <script>
                        var forwardingUrl = "/page/bouncy.php?&bpae=GbhWt6smolx797uvwVkZt3kXTsk4y6o5kxYr9vEtHeCvozli8ejbu66RQjMt7Id%2F7sjqbfF2RWJS6uRJLVU6cM1l4JPz4jN%2BdEK08uU5XoZTutPs3nk6NJZHL7zrQL9jPzLObHYglnvQjCJOZRjSxzO%2FCVgogGfHMa%2BW9CIiUsvkxfYjbS%2BH7gPMad2eIkvK0lceLuxHaNFOS36EUftr9629OTdxBoJrH9vtM8OWk9YvsYJmsDtXNeyMnbc3jeGSUNaUpys%2FeBFPEBItGU5NvlHEiKjDoy%2B7ARshbjLab8QdkfzGpTdHwX2gAWtyM8aKXAOS%2BcdOaC3eXJW%2FN5mOCl5t%2BYc7uFiRbQz6%2FaOm1RLGwKDH9cpHdb%2BROQylniESiaa0aCJUDFzfFIDLuYHiGTf00Jc%3D&redirectType=js";
                        var destinationUrl = "/page/bouncy.php?&bpae=GbhWt6smolx797uvwVkZt3kXTsk4y6o5kxYr9vEtHeCvozli8ejbu66RQjMt7Id%2F7sjqbfF2RWJS6uRJLVU6cM1l4JPz4jN%2BdEK08uU5XoZTutPs3nk6NJZHL7zrQL9jPzLObHYglnvQjCJOZRjSxzO%2FCVgogGfHMa%2BW9CIiUsvkxfYjbS%2BH7gPMad2eIkvK0lceLuxHaNFOS36EUftr9629OTdxBoJrH9vtM8OWk9YvsYJmsDtXNeyMnbc3jeGSUNaUpys%2FeBFPEBItGU5NvlHEiKjDoy%2B7ARshbjLab8QdkfzGpTdHwX2gAWtyM8aKXAOS%2BcdOaC3eXJW%2FN5mOCl5t%2BYc7uFiRbQz6%2FaOm1RLGwKDH9cpHdb%2BROQylniESiaa0aCJUDFzfFIDLuYHiGTf00Jc%3D&redirectType=meta";
                        var addDetection = true;
                        if (addDetection) {
                                var inIframe = window.self !== window.top;
                                forwardingUrl += "&inIframe=" + inIframe;
                                var inPopUp = (window.opener !== undefined && window.opener !== null && window.opener !== window);
                                forwardingUrl += "&inPopUp=" + inPopUp;
                        }
                        window.location.replace(forwardingUrl);
                </script>
                <noscript>
                        <meta http-equiv="refresh" content="1;url=/page/bouncy.php?&bpae=GbhWt6smolx797uvwVkZt3kXTsk4y6o5kxYr9vEtHeCvozli8ejbu66RQjMt7Id%2F7sjqbfF2RWJS6uRJLVU6cM1l4JPz4jN%2BdEK08uU5XoZTutPs3nk6NJZHL7zrQL9jPzLObHYglnvQjCJOZRjSxzO%2FCVgogGfHMa%2BW9CIiUsvkxfYjbS%2BH7gPMad2eIkvK0lceLuxHaNFOS36EUftr9629OTdxBoJrH9vtM8OWk9YvsYJmsDtXNeyMnbc3jeGSUNaUpys%2FeBFPEBItGU5NvlHEiKjDoy%2B7ARshbjLab8QdkfzGpTdHwX2gAWtyM8aKXAOS%2BcdOaC3eXJW%2FN5mOCl5t%2BYc7uFiRbQz6%2FaOm1RLGwKDH9cpHdb%2BROQylniESiaa0aCJUDFzfFIDLuYHiGTf00Jc%3D&redirectType=meta" />
                </noscript>
        </head>
</html>                                         
```
10. Seems we got no clue.
11. 
12. 

