# Client-side-again
#### Write-up author : [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
Can you break into this super secure portal? 
https://jupiter.challenges.picoctf.org/problem/6353/ [(link)](https://jupiter.challenges.picoctf.org/problem/6353/) or http://jupiter.challenges.picoctf.org:6353
## HINT:
1. What is obfuscation?
## STEPS:
1. First, try to open the website source code and check what's inside the `<script>` tag.
2. We can see there are confusing (obfuscating) javascript.

![Screenshot (434)](https://user-images.githubusercontent.com/70703371/172983180-60a4d3ff-bf11-4906-a462-ceae69b2d416.png)

```js
var _0x5a46=['0a029}','_again_5','this','Password\x20Verified','Incorrect\x20password','getElementById','value','substring','picoCTF{','not_this'];(function(_0x4bd822,_0x2bd6f7){var _0xb4bdb3=function(_0x1d68f6){while(--_0x1d68f6){_0x4bd822['push'](_0x4bd822['shift']());}};_0xb4bdb3(++_0x2bd6f7);}(_0x5a46,0x1b3));var _0x4b5b=function(_0x2d8f05,_0x4b81bb){_0x2d8f05=_0x2d8f05-0x0;var _0x4d74cb=_0x5a46[_0x2d8f05];return _0x4d74cb;};function verify(){checkpass=document[_0x4b5b('0x0')]('pass')[_0x4b5b('0x1')];split=0x4;if(checkpass[_0x4b5b('0x2')](0x0,split*0x2)==_0x4b5b('0x3')){if(checkpass[_0x4b5b('0x2')](0x7,0x9)=='{n'){if(checkpass[_0x4b5b('0x2')](split*0x2,split*0x2*0x2)==_0x4b5b('0x4')){if(checkpass[_0x4b5b('0x2')](0x3,0x6)=='oCT'){if(checkpass[_0x4b5b('0x2')](split*0x3*0x2,split*0x4*0x2)==_0x4b5b('0x5')){if(checkpass['substring'](0x6,0xb)=='F{not'){if(checkpass[_0x4b5b('0x2')](split*0x2*0x2,split*0x3*0x2)==_0x4b5b('0x6')){if(checkpass[_0x4b5b('0x2')](0xc,0x10)==_0x4b5b('0x7')){alert(_0x4b5b('0x8'));}}}}}}}}else{alert(_0x4b5b('0x9'));}}
```

3. If you pay attention, it looks like a partition of a flag, so if we know the pattern, we can concate the flag.
4. Next, we must beautify the JavaScript code, so it can be more readable. Paste the `js` code to this [website](https://beautifier.io/) then press enter.
5. Then we got the beautified JavaScript code.

```js
(function(_0x4bd822, _0x2bd6f7) {
    var _0xb4bdb3 = function(_0x1d68f6) {
        while (--_0x1d68f6) {
            _0x4bd822['push'](_0x4bd822['shift']());
        }
    };
    _0xb4bdb3(++_0x2bd6f7);
}(_0x5a46, 0x1b3));
var _0x4b5b = function(_0x2d8f05, _0x4b81bb) {
    _0x2d8f05 = _0x2d8f05 - 0x0;
    var _0x4d74cb = _0x5a46[_0x2d8f05];
    return _0x4d74cb;
};

function verify() {
    checkpass = document[_0x4b5b('0x0')]('pass')[_0x4b5b('0x1')];
    split = 0x4;
    if (checkpass[_0x4b5b('0x2')](0x0, split * 0x2) == _0x4b5b('0x3')) {
        if (checkpass[_0x4b5b('0x2')](0x7, 0x9) == '{n') {
            if (checkpass[_0x4b5b('0x2')](split * 0x2, split * 0x2 * 0x2) == _0x4b5b('0x4')) {
                if (checkpass[_0x4b5b('0x2')](0x3, 0x6) == 'oCT') {
                    if (checkpass[_0x4b5b('0x2')](split * 0x3 * 0x2, split * 0x4 * 0x2) == _0x4b5b('0x5')) {
                        if (checkpass['substring'](0x6, 0xb) == 'F{not') {
                            if (checkpass[_0x4b5b('0x2')](split * 0x2 * 0x2, split * 0x3 * 0x2) == _0x4b5b('0x6')) {
                                if (checkpass[_0x4b5b('0x2')](0xc, 0x10) == _0x4b5b('0x7')) {
                                    alert(_0x4b5b('0x8'));
                                }
                            }
                        }
                    }
                }
            }
        }
    } else {
        alert(_0x4b5b('0x9'));
    }
}
```

6. We see that `_0x4b5b` is a function used to obfuscate different values. Now, use the browser's Javascript console ("Developer Tools") in order to evaluate `_0x4b5b` and read it's values:

![Screenshot (435)](https://user-images.githubusercontent.com/70703371/172985208-0b91d5df-c388-4782-a5f6-9c85dc1cdad2.png)

```bash
>>> _0x4b5b
function _0x4b5b()

>>> _0x4b5b("0x0")
"getElementById"
>>> _0x4b5b("0x1")
"value"
>>> _0x4b5b("0x2")
"substring"
>>> _0x4b5b("0x3")
"picoCTF{"
>>> _0x4b5b("0x4")
"not_this"
>>> _0x4b5b("0x5")
"0a029}"
>>> _0x4b5b("0x6")
"_again_5"
>>> _0x4b5b("0x7")
"this"
>>> _0x4b5b("0x8")
"Password Verified"
>>> _0x4b5b("0x9")
"Incorrect password"
```

7. Finally, replace the function calls with hardcoded values.

```js
function verify() {
  checkpass = document['getElementById']('pass')['value'];
  /** @type {number} */
  split = 4;
  if (checkpass['substring'](0, split * 2) == 'picoCTF{') {
    if (checkpass['substring'](7, 9) == '{n') {
      if (checkpass['substring'](split * 2, split * 2 * 2) == 'not_this') {
        if (checkpass['substring'](3, 6) == 'oCT') {
          if (checkpass['substring'](split * 3 * 2, split * 4 * 2) == '0a029}') {
            if (checkpass['substring'](6, 11) == 'F{not') {
              if (checkpass['substring'](12, 16) == 'this') {
                if (checkpass['substring'](split * 2 * 2, split * 3 * 2) == '_again_5') {
                  alert('Password Verified');
                }
              }
            }
          }
        }
      }
    }
  } else {
    alert('Incorrect password');
  }
}

```

8. Last step, try to concate the flag using the same pattern as the `don't-use-client-side` challenge. 
```bash
0, split * 2 -> split *2 , split *2 *2 -> etc.
```


---

## FLAG:
```
picoCTF{not_this_again_50a029}
```
