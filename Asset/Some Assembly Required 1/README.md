# Some Assembly Required 1
## DESCRIPTION:
http://mercury.picoctf.net:40226/index.html
## HINT:
- NONE
## STEPS:
1. First, open the following website -> http://mercury.picoctf.net:40226/index.html
2. Next, try to input any strings at the textarea, then click the `submit` button.
3. It said, "Incorrect".

![image](https://user-images.githubusercontent.com/70703371/176897073-047e6154-dab2-434a-b91b-f028a71949a7.png)

4. Now let's open the page source.

![image](https://user-images.githubusercontent.com/70703371/176897167-99fa0d46-0749-43a0-bb1f-608711e287b5.png)

5. Try to view the JavaScript source-code by change the url to `http://mercury.picoctf.net:40226/G82XCw5CX3.js`.

![image](https://user-images.githubusercontent.com/70703371/176897365-a92a480e-cf5b-47e2-b002-c7f4788ad100.png)

6. Turns out it's an obfuscated JavaScript.
7. Now let's beautify it by using [this](https://beautifier.io/) website. Paste the JavaScript code there, then press `ctrl + enter` to beautify it.

```js
const _0x402c = [
  'value',
  '2wfTpTR',
  'instantiate',
  '275341bEPcme',
  'innerHTML',
  '1195047NznhZg',
  '1qfevql',
  'input',
  '1699808QuoWhA',
  'Correct!',
  'check_flag',
  'Incorrect!',
  './JIFxzHyW8W',
  '23SMpAuA',
  '802698XOMSrr',
  'charCodeAt',
  '474547vVoGDO',
  'getElementById',
  'instance',
  'copy_char',
  '43591XxcWUl',
  '504454llVtzW',
  'arrayBuffer',
  '2NIQmVj',
  'result',
];
const _0x4e0e = function (_0x553839, _0x53c021) {
  _0x553839 = _0x553839 - 0x1d6;
  let _0x402c6f = _0x402c[_0x553839];
  return _0x402c6f;
};
(function (_0x76dd13, _0x3dfcae) {
  const _0x371ac6 = _0x4e0e;
  while (!![]) {
    try {
      const _0x478583 =
        -parseInt(_0x371ac6(0x1eb)) +
        parseInt(_0x371ac6(0x1ed)) +
        -parseInt(_0x371ac6(0x1db)) * -parseInt(_0x371ac6(0x1d9)) +
        -parseInt(_0x371ac6(0x1e2)) * -parseInt(_0x371ac6(0x1e3)) +
        -parseInt(_0x371ac6(0x1de)) * parseInt(_0x371ac6(0x1e0)) +
        parseInt(_0x371ac6(0x1d8)) * parseInt(_0x371ac6(0x1ea)) +
        -parseInt(_0x371ac6(0x1e5));
      if (_0x478583 === _0x3dfcae) break;
      else _0x76dd13['push'](_0x76dd13['shift']());
    } catch (_0x41d31a) {
      _0x76dd13['push'](_0x76dd13['shift']());
    }
  }
})(_0x402c, 0x994c3);
let exports;
(async () => {
  const _0x48c3be = _0x4e0e;
  let _0x5f0229 = await fetch(_0x48c3be(0x1e9)),
    _0x1d99e9 = await WebAssembly[_0x48c3be(0x1df)](await _0x5f0229[_0x48c3be(0x1da)]()),
    _0x1f8628 = _0x1d99e9[_0x48c3be(0x1d6)];
  exports = _0x1f8628['exports'];
})();

function onButtonPress() {
  const _0xa80748 = _0x4e0e;
  let _0x3761f8 = document['getElementById'](_0xa80748(0x1e4))[_0xa80748(0x1dd)];
  for (let _0x16c626 = 0x0; _0x16c626 < _0x3761f8['length']; _0x16c626++) {
    exports[_0xa80748(0x1d7)](_0x3761f8[_0xa80748(0x1ec)](_0x16c626), _0x16c626);
  }
  exports['copy_char'](0x0, _0x3761f8['length']),
    exports[_0xa80748(0x1e7)]() == 0x1 ? (document[_0xa80748(0x1ee)](_0xa80748(0x1dc))[_0xa80748(0x1e1)] = _0xa80748(0x1e6)) : (document[_0xa80748(0x1ee)](_0xa80748(0x1dc))[_0xa80748(0x1e1)] = _0xa80748(0x1e8));
}

```

8. If you look carefully at the value from an const char variable `_0x402c`. There's a string that caught my attention -> `'./JIFxzHyW8W'`.

