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

4. Now, the next clue is not inside the const char variables again, it's different from the 2 previous challenge.
5. Try to this function algorithm:

```js
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
```

6. Looks like there's a clue -> `('./qCCYI0ajpD')`.
7. Try to go there by changing the url to -> `http://mercury.picoctf.net:12557/qCCYI0ajpD/`.
8. And we got this:

![image](https://user-images.githubusercontent.com/70703371/176987758-489c5f4a-53aa-400d-8d29-9f68baeb9afe.png)

9. It looks like a `wasm` file, download the file by changing the url to this -> `mercury.picoctf.net:12557/qCCYI0ajpD`.
10. For this solution i decode the file by run this command at kali linux terminal.

```bash
wasm-decompile qCCYI0ajpD
```

> OUTPUT:

```go
export memory memory(initial: 2, max: 0);

global g_a:int = 66864;
export global input:int = 1072;
export global key:int = 1067;
export global dso_handle:int = 1024;
export global data_end:int = 1328;
export global global_base:int = 1024;
export global heap_base:int = 66864;
export global memory_base:int = 0;
export global table_base:int = 1;

table T_a:funcref(min: 1, max: 1);

data d_nAfab23d(offset: 1024) =
  "\9dn\93\c8\b2\b9A\8b\c2\97\d4f\c7\93\c4\d4a\c2\c6\c9\ddb\94\9e\c2\892\91"
  "\90\c1\dd3\91\91\97\8bd\c1\92\c4\90\00\00";
data d_b(offset: 1067) = "\f1\a7\f0\07\ed";

export function wasm_call_ctors() {
}

export function strcmp(a:int, b:int):int {
  var c:int = g_a;
  var d:int = 32;
  var e:int = c - d;
  e[6]:int = a;
  e[5]:int = b;
  var f:int = e[6]:int;
  e[4]:int = f;
  var g:int = e[5]:int;
  e[3]:int = g;
  loop L_b {
    var h:ubyte_ptr = e[4]:int;
    var i:int = 1;
    var j:int = h + i;
    e[4]:int = j;
    var k:int = h[0];
    e[11]:byte = k;
    var l:ubyte_ptr = e[3]:int;
    var m:int = 1;
    var n:int = l + m;
    e[3]:int = n;
    var o:int = l[0];
    e[10]:byte = o;
    var p:int = e[11]:ubyte;
    var q:int = 255;
    var r:int = p & q;
    if (r) goto B_c;
    var s:int = e[11]:ubyte;
    var t:int = 255;
    var u:int = s & t;
    var v:int = e[10]:ubyte;
    var w:int = 255;
    var x:int = v & w;
    var y:int = u - x;
    e[7]:int = y;
    goto B_a;
    label B_c:
    var z:int = e[11]:ubyte;
    var aa:int = 255;
    var ba:int = z & aa;
    var ca:int = e[10]:ubyte;
    var da:int = 255;
    var ea:int = ca & da;
    var fa:int = ba;
    var ga:int = ea;
    var ha:int = fa == ga;
    var ia:int = 1;
    var ja:int = ha & ia;
    if (ja) continue L_b;
  }
  var ka:int = e[11]:ubyte;
  var la:int = 255;
  var ma:int = ka & la;
  var na:int = e[10]:ubyte;
  var oa:int = 255;
  var pa:int = na & oa;
  var qa:int = ma - pa;
  e[7]:int = qa;
  label B_a:
  var ra:int = e[7]:int;
  return ra;
}

export function check_flag():int {
  var a:int = 0;
  var b:int = 1072;
  var c:int = 1024;
  var d:int = strcmp(c, b);
  var e:int = d;
  var f:int = a;
  var g:int = e != f;
  var h:int = -1;
  var i:int = g ^ h;
  var j:int = 1;
  var k:int = i & j;
  return k;
}

function copy(a:int, b:int) {
  var c:int = g_a;
  var d:int = 16;
  var e:int_ptr = c - d;
  e[3] = a;
  e[2] = b;
  var f:int = e[3];
  if (eqz(f)) goto B_a;
  var g:int = 4;
  var h:int = e[2];
  var i:int = 5;
  var j:int = h % i;
  var k:ubyte_ptr = g - j;
  var l:int = k[1067];
  var m:int = 24;
  var n:int = l << m;
  var o:int = n >> m;
  var p:int = e[3];
  var q:int = p ^ o;
  e[3] = q;
  label B_a:
  var r:int = e[3];
  var s:byte_ptr = e[2];
  s[1072] = r;
}


```

