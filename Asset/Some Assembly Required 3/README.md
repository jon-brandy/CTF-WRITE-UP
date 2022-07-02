# Some Assembly Required 3
## DESCRIPTION:
http://mercury.picoctf.net:12557/index.html
## HINT:
- NONE
## STEPS:
1. First open the following website -> `http://mercury.picoctf.net:12557/index.html`.
2. Open the page source and we can see the js file name, now redirect to the page by changing the url to this -> `http://mercury.picoctf.net:12557/rTEuOmSfG3.js`.

![image](https://user-images.githubusercontent.com/70703371/176987580-be828dfc-b188-4540-89a7-5db11c66b84c.png)


![image](https://user-images.githubusercontent.com/70703371/176987592-76af37d5-eb92-4888-ab84-617806f71069.png)

3. Beautify the `js` source-code using this [online](https://beautifier.io/) tools.

```js
const _0x143f = [
  'exports',
  '270328ewawLo',
  'instantiate',
  '1OsuamQ',
  'Incorrect!',
  'length',
  'copy_char',
  'value',
  '1512517ESezaM',
  'innerHTML',
  'check_flag',
  'result',
  '1383842SQRPPf',
  '924408cukzgO',
  'getElementById',
  '418508cLDohp',
  'input',
  'Correct!',
  '573XsMMHp',
  'arrayBuffer',
  '183RUQBDE',
  '38934oMACea',
];
const _0x187e = function (_0x3075b9, _0x2ac888) {
  _0x3075b9 = _0x3075b9 - 0x11d;
  let _0x143f7d = _0x143f[_0x3075b9];
  return _0x143f7d;
};
(function (_0x3379df, _0x252604) {
  const _0x1e2b12 = _0x187e;
  while (!![]) {
    try {
      const _0x5e2d0a =
        -parseInt(_0x1e2b12(0x122)) +
        -parseInt(_0x1e2b12(0x12f)) +
        -parseInt(_0x1e2b12(0x126)) * -parseInt(_0x1e2b12(0x12b)) +
        -parseInt(_0x1e2b12(0x132)) +
        parseInt(_0x1e2b12(0x124)) +
        -parseInt(_0x1e2b12(0x121)) * -parseInt(_0x1e2b12(0x11f)) +
        parseInt(_0x1e2b12(0x130));
      if (_0x5e2d0a === _0x252604) break;
      else _0x3379df['push'](_0x3379df['shift']());
    } catch (_0x289152) {
      _0x3379df['push'](_0x3379df['shift']());
    }
  }
})(_0x143f, 0xed04c);
let exports;
(async () => {
  const _0x484ae0 = _0x187e;
  let _0x487b31 = await fetch('./qCCYI0ajpD'),
    _0x5eebfd = await WebAssembly[_0x484ae0(0x125)](await _0x487b31[_0x484ae0(0x120)]()),
    _0x30f3ed = _0x5eebfd['instance'];
  exports = _0x30f3ed[_0x484ae0(0x123)];
})();

function onButtonPress() {
  const _0x271e58 = _0x187e;
  let _0x441124 = document[_0x271e58(0x131)](_0x271e58(0x11d))[_0x271e58(0x12a)];
  for (let _0x34c54a = 0x0; _0x34c54a < _0x441124[_0x271e58(0x128)]; _0x34c54a++) {
    exports[_0x271e58(0x129)](_0x441124['charCodeAt'](_0x34c54a), _0x34c54a);
  }
  exports[_0x271e58(0x129)](0x0, _0x441124[_0x271e58(0x128)]),
    exports[_0x271e58(0x12d)]() == 0x1 ? (document[_0x271e58(0x131)](_0x271e58(0x12e))[_0x271e58(0x12c)] = _0x271e58(0x11e)) : (document[_0x271e58(0x131)](_0x271e58(0x12e))['innerHTML'] = _0x271e58(0x127));
}

```

