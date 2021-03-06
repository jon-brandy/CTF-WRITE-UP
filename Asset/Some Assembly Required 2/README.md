# Some Assembly Required 2
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
http://mercury.picoctf.net:44570/index.html
## HINT:
- NONE
## STEPS:
1. First, open the following website -> `http://mercury.picoctf.net:44570/index.html`.

![image](https://user-images.githubusercontent.com/70703371/176900866-7605950c-5685-493e-9f5e-b9848fa23ffa.png)

2. If we try to input any strings, it gave the same response as the previous challenge -> `Some Assembly Required 1`.
3. Next, open the page source.

![image](https://user-images.githubusercontent.com/70703371/176901066-9495428e-156d-4739-8ab5-4f1bb61ca527.png)

3. Go to the javascript file by changing the url to this `http://mercury.picoctf.net:44570/Y8splx37qY.js` and beautify it by using [this](https://beautifier.io/) website

```javascript
const _0x6d8f = [
  'copy_char',
  'value',
  '207aLjBod',
  '1301420SaUSqf',
  '233ZRpipt',
  '2224QffgXU',
  'check_flag',
  '408533hsoVYx',
  'instance',
  '278338GVFUrH',
  'Correct!',
  '549933ZVjkwI',
  'innerHTML',
  'charCodeAt',
  './aD8SvhyVkb',
  'result',
  '977AzKzwq',
  'Incorrect!',
  'exports',
  'length',
  'getElementById',
  '1jIrMBu',
  'input',
  '615361geljRK',
];
const _0x5c00 = function (_0x58505a, _0x4d6e6c) {
  _0x58505a = _0x58505a - 0xc3;
  let _0x6d8fc4 = _0x6d8f[_0x58505a];
  return _0x6d8fc4;
};
(function (_0x12fd07, _0x4e9d05) {
  const _0x4f7b75 = _0x5c00;
  while (!![]) {
    try {
      const _0x1bb902 =
        -parseInt(_0x4f7b75(0xc8)) * -parseInt(_0x4f7b75(0xc9)) +
        -parseInt(_0x4f7b75(0xcd)) +
        parseInt(_0x4f7b75(0xcf)) +
        parseInt(_0x4f7b75(0xc3)) +
        -parseInt(_0x4f7b75(0xc6)) * parseInt(_0x4f7b75(0xd4)) +
        parseInt(_0x4f7b75(0xcb)) +
        -parseInt(_0x4f7b75(0xd9)) * parseInt(_0x4f7b75(0xc7));
      if (_0x1bb902 === _0x4e9d05) break;
      else _0x12fd07['push'](_0x12fd07['shift']());
    } catch (_0x4f8a) {
      _0x12fd07['push'](_0x12fd07['shift']());
    }
  }
})(_0x6d8f, 0x4bb06);
let exports;
(async () => {
  const _0x835967 = _0x5c00;
  let _0x1adb5f = await fetch(_0x835967(0xd2)),
    _0x355961 = await WebAssembly['instantiate'](await _0x1adb5f['arrayBuffer']()),
    _0x5c0ffa = _0x355961[_0x835967(0xcc)];
  exports = _0x5c0ffa[_0x835967(0xd6)];
})();

function onButtonPress() {
  const _0x50ea62 = _0x5c00;
  let _0x5f4170 = document[_0x50ea62(0xd8)](_0x50ea62(0xda))[_0x50ea62(0xc5)];
  for (let _0x19d3ca = 0x0; _0x19d3ca < _0x5f4170['length']; _0x19d3ca++) {
    exports[_0x50ea62(0xc4)](_0x5f4170[_0x50ea62(0xd1)](_0x19d3ca), _0x19d3ca);
  }
  exports['copy_char'](0x0, _0x5f4170[_0x50ea62(0xd7)]),
    exports[_0x50ea62(0xca)]() == 0x1 ? (document['getElementById'](_0x50ea62(0xd3))[_0x50ea62(0xd0)] = _0x50ea62(0xce)) : (document[_0x50ea62(0xd8)](_0x50ea62(0xd3))['innerHTML'] = _0x50ea62(0xd5));
}

```

4. If you look carefully at the value from an const char variable _0x402c. There's a string that caught my attention -> `'/aD8SvhyVkb'`.
5. Now change the url to this ->  `http://mercury.picoctf.net:44570/aD8SvhyVkb/`.

![image](https://user-images.githubusercontent.com/70703371/176902945-2b9a7fa0-a13a-4846-a010-ffed2026d7bc.png)

6. At the bottom, if you pay attention, there is a string that resembles XOR cipher text -> `+xakgK\Ns><m:i1>1991:nkjl<ii1j0n=mm09;<i:u`.
7. I can identify it's a XOR cipertext, because the strings starts with `+`.
8. You can decode it either by using [online](https://www.dcode.fr/xor-cipher) tools or manual code.
9. For this solution i used online decoder, simply paste the strings then press the `decrypt` button.

![image](https://user-images.githubusercontent.com/70703371/176987298-f4324b1d-546b-4cda-9b0a-48fe2fae0c54.png)

10. At the result tab, scroll down and you will find the flag.

![image](https://user-images.githubusercontent.com/70703371/176987354-ebcefcf4-8e02-4643-b764-8c931015de95.png)

11. Finally we got the flag!

---
## FLAG
```
picoCTF{64e2a9691192fcbd4aa9b8f5ee8134a2}
```


