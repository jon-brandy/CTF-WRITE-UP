# WebNet0
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
We found this [packet capture](https://github.com/jon-brandy/CTF-WRITE-UP/blob/b9a222fbaff00d8cfc64e1d2e4d56748c1e16e35/Asset/WebNet0/capture.pcap) and [key](https://github.com/jon-brandy/CTF-WRITE-UP/blob/f5b89a2f26a92622a26827e63c0180d843760dae/Asset/WebNet0/picopico.key). Recover the flag.
## HINTS:
1. Try using a tool like Wireshark.
2. How can you decrypt the TLS stream?
## STEPS:
1. First, download both file given.
2. Open the `.pcap` file using wireshark.

![image](https://user-images.githubusercontent.com/70703371/180606074-f74008ef-34cb-47be-b449-998940a9205f.png)

3. Let's follow this TCP stream and TLS stream.

![image](https://user-images.githubusercontent.com/70703371/180606089-38b9d4f9-ed03-4b67-aeed-1405758e046f.png)

> OUTPUT TCP STREAM:

```pcap
................>..}............O]Ee.d..N....r.0.,.(.$...
.......k.i.h.9.7.6.2...*.&.......=.5./.+.'.#...	.......g.?.>.3.1.0.1.-.).%.......<./.........
.
...
.....a...7.5..2ec2-18-223-184-200.us-east-2.compute.amazonaws.com.........
.....................
.....	.
.#...
. ..........................................................................................................................................................................................................................................................5...1...*...^...r.g!.x.y.._.!Uw.f...U	......	......#.................0...0..........R..&j.....>Lf....$..0
.	*.H..
.....0\1.0	..U....US1.0...U....Michigan1.0...U...	Kalamazoo1.0...U.
..Pico CTF1.0...U...
Wiresharky0..
190812154129Z.
200811154129Z0\1.0	..U....US1.0...U....Michigan1.0...U...	Kalamazoo1.0...U.
..Pico CTF1.0...U...
Wiresharky0.."0
.	*.H..
..........0..
......*QO4..x.y...S.w.w... {..(...V.v..8K:.9....G.(.-.......pi7.?c....qD`....0...a..+..D..l..eE5.e...!.C.A{.OZ._}.0.dA$.[..e.m...;d.pC....BQe.	..]...(.1.......p..0..q.^.....y#......].....g.....!..A&...w.8.t....s.#...I....I...O..l
......H7P....&...4.......$..&xo......S0Q0...U......!..8...<.....`%z.l(.0...U.#..0...!..8...<.....`%z.l(.0...U.......0....0
.	*.H..
..........ip.su.x..'8{.z...es.../.HL....Ij..Q..L&........%.	.r..gJ6.29.T".*8..n	...n.~+*...J.6.....yG...".7}...oO...k..G[3.-.8.(.gq."..(......
.....9=7T..t}Zf.p..[m.b...zq........:
mo...E...yN.d..
.....0&..9s...C.p....~.Qv............y.E...A]... \.D.2=C.c. ..B..m.r&....................m%......H........z..
..g'\S.G#(.....t.(1Z9.PMB...;p.^#...PS..]....y|......mc.Vb..N....B[...._...nES....
.;p.0.|O..f.u..F.5id4..1 g..\.....X.f........C....2=eH.J&.ib.G.9....k;G.-.M.9 ..c#H.R..&.n..~.L.4.Hk........g.{rv....~_.....j..-..4vJ..h......_.CA..%7g...........(...B.r..zZ)..w.PRFD..:..z.DC.X>.O...F.#J............,..NVDI62.........}.Ja#.Fx.7.Z..G.!..o.F..;..^T.L...K..8.....i.E...=F. .P......j...."$...7.#.g.dd..s.=...V._.....I0R.....9|..........#=,..xI.K..Qx.[v.__c...
........w........(
.-3..s...xTM..q.*............(..5.]fc....s.
.F.O.........7s...~....-..........B.r...._.....0p...e{.217..<}.7....[?..+.k....J.P...Y....m....
;E.....*.+*.<.B.1.n..sG+N........}.W.
.@(.k.....N%.......k ...v........y.Q.K&.i.s..
"!.O%
..=`Z....
.b.`.i..Z/...`wpY.H...<.]W=.....@...L(O<.2-1aou.:.r...-....2!.Vv.`.D.YR..1y.
=W...f.|.$...A......eZ-G...G	#e..[.w6-U..O.P&..&.......H..9..[......3g.e...~.[...4
t_.Z.r...7......../e.g<.....%.&>..C..p3.M.:..Z....,u........8>..P..9.K.$..8.*.....?..~2|p..i=e,..a..i..l...fHDMg.*7Z...uK..S........5.]fc.....G.....W.j.I..x..;.*.D~X.lX.9eY.@f...XG.f...|.k.l....$3..:g..Y..)e}.	..?K'	......J...]X.;7..cw.....$.PX..._)7...P]..B..$........xK..O...3..~G..G..Tz...c6.O...*.5....QT...f...s.h....[B.~..|...G..a.L.8.u..@.2....<9.J...r#.......5:i.Y .fG. .._...d..."*.1([^..........K....6"..Y....v...........v.3iL....0E..z~#....b|..]%P.o.
M..l......6..XkCw.i..........O...;..A.....1b...................:..gp....v4.5......Kf.......QK.--.~X...6...@..`..$..v......9.'scC?.5k
U.....\.....;L".w.nebd	V%......"....+m......o...B.r....._aa.....M..&.M..o..
.y=*y.....5.L.lm4......-.*.'H3H..OQS...'.._.:5".L.. 4)
.;.c...p.g?....5.9..3.'.l........%.=............=
4..Nt.e.6.....NO..X.^.>.hA.:.
J~HH9.......`m..*.G...RdA....`vOo.^...#	..~.X.......v../z....]/*L..]-..GX.... .E...-4.......K........R.*.w...w.........&..\
f.
]@ns.....	.\...M2...geM.)
...tN.....D.....|...{...P..entoxo...%..po.O..Z{
....6..5.]fc....,.T=..u..v..0G.?....!am...+.g(5O].4\.o..(.|G...X....	.Hr...._...j5..{..j..W.!.,}7.....w.u0Y...
p..g.y.~m....%...m.wv@O .o
7.....)....U...T1.8r..#..$Zx.q.r..1?.b...`.;..0..h...I..t.d.V......&..-.S6(.3....q.B..t%...... ..LkpN..\B.FH(=JW....w..N..8.[`.:.Z....YxK..#..f....r.W......\....w..^....$.O.....T..KGW..O...`0..t.....J.lIMq...0D.......5............5!...|.)...G..............b!]...)N..,..i.zbn.=S.1@.E.^*FYT.*....;....?>.
gaOO....F.....:........(j.uZU....F	.I..LK.q)Ex..........U?.th.w. g...u8.6.y.'.gV..z.UO.}E
'..7...s....a......n......9.F...Q1...}..
```

> TLS STREAM OUTPUT:

![image](https://user-images.githubusercontent.com/70703371/180606120-23e9c96e-fa1e-4b16-84bd-5dcd25d80cd2.png)

4. Seems we got no clue from both stream.
5. Then, i check what's inside the `picopico.key` file.

![image](https://user-images.githubusercontent.com/70703371/180606219-fce469b7-fc38-4fe4-a95b-04148f690fcc.png)

6. It's a **private key**.
7. Based from the hint number 2, we need to find a way to decrypt TLS stream. So i did a small research.

> RESEARCH REFERENCES:

```
https://blog.didierstevens.com/2020/12/14/decrypting-tls-streams-with-wireshark-part-1/
```

8. Now, open `edit` , go to `preferences` and choose `protocols`, then scroll down until you find `TLS`.
9. Next, choose `edit`.

![image](https://user-images.githubusercontent.com/70703371/180606373-6eca8654-6a2d-45a9-be66-0bdd468dcaf2.png)

10. Then press the `+` button.

![image](https://user-images.githubusercontent.com/70703371/180606397-7217f690-1e68-46fa-b975-8f6c864e94c1.png)

11. Insert the `picopico.key` file and press `ok` afterwards.

![image](https://user-images.githubusercontent.com/70703371/180606412-b76d44a5-60ba-4aa4-b817-3cb1a18f93ac.png)

12. Now scroll down until you see a `green` traffic.

![image](https://user-images.githubusercontent.com/70703371/180606461-476f6d4a-0581-4024-aeea-b28de7c44488.png)

13. Follow this `TLS Stream`.

![image](https://user-images.githubusercontent.com/70703371/180606544-f475ad40-0c46-4210-86ee-6defd1dea4cd.png)

> TLS STREAM OUTPUT:

```pcap
GET / HTTP/1.1
Host: ec2-18-223-184-200.us-east-2.compute.amazonaws.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Pragma: no-cache
Cache-Control: no-cache

HTTP/1.1 200 OK
Date: Fri, 23 Aug 2019 15:56:36 GMT
Server: Apache/2.4.29 (Ubuntu)
Last-Modified: Mon, 12 Aug 2019 16:50:05 GMT
ETag: "5ff-58fee50dc3fb0-gzip"
Accept-Ranges: bytes
Vary: Accept-Encoding
Content-Encoding: gzip
Pico-Flag: picoCTF{nongshim.shrimp.crackers}
Content-Length: 821
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive
Content-Type: text/html

...........T]s.:.|N~...........$4.g(.#@.&l..+KB...._...f.N.\^,.-G.{..."..B`...v....(b.oafu...R..ra...
.x.&.G ......l.m.*.).
k.Z..n[.....om..
...B.4f..%.N..oH....
.F4A.V!..w..J%a?l...h.q..D..s..D..O&'F...HL}K..b.bl.M%.}+.Z.. T..?....<6	#..<....p...C.N5''...e.j.H..sL.....$.b\#...`../..Q.1.^F=...V...f..I0.=..p.[..`..........o$W.K...[.qV.|....._+.sp..b..N.....".?.p.l.J..}....6.h.&..N.S....K.]x.P,......<*:.g^D6 .H).*g.....2.g?..f.......cjF.....L.Aa...l.u...cKj..6g.7M....AqB4`.X.....&.f.....zP|`.
.RI..l.........B.......I(..'.K@6ZcY..H...t0.O\.,.L...r.|..:4S2<.4..v.U....ai..`:....c..8.....o.....&.-.|l..D....Y2...r..U.x...x..]..RO..O...=.}.=x..'.....R..b...%{....d..8:.].m8-...c....._..v/z.h...i.....H.S..g7.....t.
....V................R..n.....k9A6.gI..D],.\9&...........5g2..E.1d..}...UqcW....w.V6......>T.	U...).?.....
```

15. Finally we got the flag!

![image](https://user-images.githubusercontent.com/70703371/180606574-e2a81c38-73e2-465a-a3bd-5c6e508d064b.png)


---
## FLAG

```
picoCTF{nongshim.shrimp.crackers}
```
