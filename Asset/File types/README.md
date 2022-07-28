# File types
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTON:
This file was found among some files marked confidential but my pdf reader cannot read it, maybe yours can. 
You can download the file from [here](https://github.com/jon-brandy/CTF-WRITE-UP/blob/416b570fde0e5bf242967417270ad0ac07517041/Asset/File%20types/Flag.pdf).
## HINT:
1. Remember that some file types can contain and nest other files
## STEPS:
1. First, download the file given.
2. Next, run `file` command to see what is the intended file type.

> RESULT:

![image](https://user-images.githubusercontent.com/70703371/181430145-f99a7b33-ee8f-451c-81d1-7340b93214df.png)

3. Hm let's open it on vscode.

```sh
#!/bin/sh
# This is a shell archive (produced by GNU sharutils 4.15.2).
# To extract the files from this archive, save it to some FILE, remove
# everything before the '#!/bin/sh' line above, then type 'sh FILE'.
#
lock_dir=_sh00046
# Made on 2022-03-15 06:50 UTC by <root@75622702a7ec>.
# Source directory was '/app'.
#
# Existing files will *not* be overwritten, unless '-c' is specified.
#
# This shar contains:
# length mode       name
# ------ ---------- ------------------------------------------
#   1092 -rw-r--r-- flag
#
MD5SUM=${MD5SUM-md5sum}
f=`${MD5SUM} --version | egrep '^md5sum .*(core|text)utils'`
test -n "${f}" && md5check=true || md5check=false
${md5check} || \
  echo 'Note: not verifying md5sums.  Consider installing GNU coreutils.'
if test "X$1" = "X-c"
then keep_file=''
else keep_file=true
fi
echo=echo
save_IFS="${IFS}"
IFS="${IFS}:"
gettext_dir=
locale_dir=
set_echo=false

for dir in $PATH
do
  if test -f $dir/gettext \
     && ($dir/gettext --version >/dev/null 2>&1)
  then
    case `$dir/gettext --version 2>&1 | sed 1q` in
      *GNU*) gettext_dir=$dir
      set_echo=true
      break ;;
    esac
  fi
done

if ${set_echo}
then
  set_echo=false
  for dir in $PATH
  do
    if test -f $dir/shar \
       && ($dir/shar --print-text-domain-dir >/dev/null 2>&1)
    then
      locale_dir=`$dir/shar --print-text-domain-dir`
      set_echo=true
      break
    fi
  done

  if ${set_echo}
  then
    TEXTDOMAINDIR=$locale_dir
    export TEXTDOMAINDIR
    TEXTDOMAIN=sharutils
    export TEXTDOMAIN
    echo="$gettext_dir/gettext -s"
  fi
fi
IFS="$save_IFS"
if (echo "testing\c"; echo 1,2,3) | grep c >/dev/null
then if (echo -n test; echo 1,2,3) | grep n >/dev/null
     then shar_n= shar_c='
'
     else shar_n=-n shar_c= ; fi
else shar_n= shar_c='\c' ; fi
f=shar-touch.$$
st1=200112312359.59
st2=123123592001.59
st2tr=123123592001.5 # old SysV 14-char limit
st3=1231235901

if   touch -am -t ${st1} ${f} >/dev/null 2>&1 && \
     test ! -f ${st1} && test -f ${f}; then
  shar_touch='touch -am -t $1$2$3$4$5$6.$7 "$8"'

elif touch -am ${st2} ${f} >/dev/null 2>&1 && \
     test ! -f ${st2} && test ! -f ${st2tr} && test -f ${f}; then
  shar_touch='touch -am $3$4$5$6$1$2.$7 "$8"'

elif touch -am ${st3} ${f} >/dev/null 2>&1 && \
     test ! -f ${st3} && test -f ${f}; then
  shar_touch='touch -am $3$4$5$6$2 "$8"'

else
  shar_touch=:
  echo
  ${echo} 'WARNING: not restoring timestamps.  Consider getting and
installing GNU '\''touch'\'', distributed in GNU coreutils...'
  echo
fi
rm -f ${st1} ${st2} ${st2tr} ${st3} ${f}
#
if test ! -d ${lock_dir} ; then :
else ${echo} "lock directory ${lock_dir} exists"
     exit 1
fi
if mkdir ${lock_dir}
then ${echo} "x - created lock directory ${lock_dir}."
else ${echo} "x - failed to create lock directory ${lock_dir}."
     exit 1
fi
# ============= flag ==============
if test -n "${keep_file}" && test -f 'flag'
then
${echo} "x - SKIPPING flag (file already exists)"

else
${echo} "x - extracting flag (text)"
  sed 's/^X//' << 'SHAR_EOF' | uudecode &&
begin 600 flag
M(3QA<F-H/@IF;&%G+R`@("`@("`@("`@,"`@("`@("`@("`@,"`@("`@,"`@
M("`@-C0T("`@("`Q,#(T("`@("`@8`K'<6D`(;RD@0`````!````,&)!-P4`
M```%`F9L86<``$)::#DQ05DF4UEQ&N,Y```E____?^_KW\K_KZ__Z_K__3ME
M_^_>MZG.]_EU_`Q./]9Y![`!&VH(`:-#0T`T:-&AH``-#1H:&AB::`T`T`R-
M`Q!HTQ&C(:!D,3330,U-#U#:(T;1$&AH&30-&3(T-`9!D#"&FF0R``]0`#(!
MI@"9J-!ZAH`TR-!HTQ-&0T`&0!53]4`TT-`TQ-#30`TT-`::!HR`!A-&30!D
M&@&C1B&0-,@R&AH#0:#)B:-``"`(`!MH%Z`<#PI/<?3`25WK("'P(/@-2@>=
M?.C"PYR]C^H<;B@3A:7T;B8LKCKQJY*4NS1_5'1C\"WL,3VECJ$V%,XK[7`Q
MWS)Y>+C?-X+B3:K!;A*H=&0>XT=`)=A<NVLD_HOZL$LO4'@UG2&3]RXY>"+8
M<::Z4V#-X*5,O(I/)K%D)6)?/-2W4*!L-OGR^V``/IG'Z8IP<,%6LD?*[\VF
MWOA@M[`B=-U:5YU?R+_T$,6CL-IUFC8-$(+%&9$"X`:M!_V9:[X*'V$K4+AL
M!++CMS&D_1&Y\%#9C'AJ!)`(Y])]10^#R23#^1C2R`&4AYU\`F0Q'J.1-Q`L
M5&.0C<D"CZ/W6.AJF`2NF1*;N$B0R&@XKWA4YF%P@O$P-Y_QV2<?S=TZ:H%H
M9LP?2D9WJ>%6*!;;)W8V92/7II[_B[DBG"A(.(UQG(``QW$`````````````
M`0`````````+``````!44D%)3$52(2$A````````````````````````````
M````````````````````````````````````````````````````````````
M````````````````````````````````````````````````````````````
M````````````````````````````````````````````````````````````
M````````````````````````````````````````````````````````````
M````````````````````````````````````````````````````````````
M````````````````````````````````````````````````````````````
M````````````````````````````````````````````````````````````
M````````````````````````````````````````````````````````````
M````````````````````````````````````````````````````````````
,````````````````
`
end
SHAR_EOF
  (set 20 22 03 15 06 50 41 'flag'
   eval "${shar_touch}") && \
  chmod 0644 'flag'
if test $? -ne 0
then ${echo} "restore of flag failed"
fi
  if ${md5check}
  then (
       ${MD5SUM} -c >/dev/null 2>&1 || ${echo} 'flag': 'MD5 check failed'
       ) << \SHAR_EOF
1d760a914484498ec0d7734ad2e194e2  flag
SHAR_EOF

else
test `LC_ALL=C wc -c < 'flag'` -ne 1092 && \
  ${echo} "restoration warning:  size of 'flag' is not 1092"
  fi
fi
if rm -fr ${lock_dir}
then ${echo} "x - removed lock directory ${lock_dir}."
else ${echo} "x - failed to remove lock directory ${lock_dir}."
     exit 1
fi
exit 0

```

4. Looks like it's a `shell` file.
5. Based from this clue:

```
# everything before the '#!/bin/sh' line above, then type 'sh FILE'.
```

Let's run it by type this command -> `sh ./Flag.pdf` at your kali linux terminal.

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/181431331-c3db665a-5ac9-42df-89ce-7b8762318725.png)

6. Great! Now we have another file to check.

![image](https://user-images.githubusercontent.com/70703371/181431442-1e686bb1-f7c2-40b0-90b6-e6bd2ea490be.png)

7. Let's check the `flag` file type.

![image](https://user-images.githubusercontent.com/70703371/181431604-fc3e95da-300d-428e-87d6-0b3a0628fdee.png)

8. Since it's an `ar` archive, let's extract it by run -> `ar xv flag`.

> NOTES

```
Run [man ar] , to see all the ar commands / payloads available.
```

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/181431957-a70d6bad-fc82-428f-b0a6-89a527dc1f56.png)

9. It extracted a fila named `flag`, run `file` again to check the file type.

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/181432122-489f3e68-52b2-47bd-a778-1f6666fdb8c0.png)

10. Let's extract the `.cpio` file , but first, rename it to `.cpio` to avoid collision. Run -> `mv flag flag.cpio`.

![image](https://user-images.githubusercontent.com/70703371/181432655-c4f14061-b92e-452a-afd1-b23c6bb02334.png)

11. Let's extract it by run -> `cpio --file flag.cpio --extract`.

> NOTES

```
Run [man cpio] to see all the commands / payloads available.
```

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/181432808-1a24d1f3-6561-4e2d-b409-3b9b74e95879.png)

12. It's a bzip file.

![image](https://user-images.githubusercontent.com/70703371/181433212-8e686b06-609c-4b1f-8ae6-2bf463e59624.png)

13. Now run -> `bunzip2 flag` to extract it.

![image](https://user-images.githubusercontent.com/70703371/181433635-3299d2db-2d4b-4d5e-b47b-982ec4bf6fa2.png)

14. Check the newly extracted file.

![image](https://user-images.githubusercontent.com/70703371/181433727-0d68e6db-6dab-4135-9532-58b5c1172cce.png)

15. It's a gzip file. Rename it by run -> `mv flag.out flag.gz`.
16. Then extract it by run -> `gunzip flag.gz`.

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/181434107-884a7a8c-767e-4a4c-beb6-79035296e3e7.png)

17. Run `file` to check the file type.

![image](https://user-images.githubusercontent.com/70703371/181434200-689a19cf-6771-4fb0-b537-55b70b639932.png)

18. It's an `lzip` file. Extract it by run -> `lzip -d flag`.
19. We got another file type now!

![image](https://user-images.githubusercontent.com/70703371/181434595-2fa1878e-dad0-4cb8-959f-48ee92ee4a11.png)

20. Since `lz4` need a file output when extract it, run this command then -> `lz4 -d flag.out outputfile`.

![image](https://user-images.githubusercontent.com/70703371/181435156-3d7c4bc6-a5e8-4c61-aa9c-9fe6f6e2220a.png)

![image](https://user-images.githubusercontent.com/70703371/181435207-6da002e7-9825-4812-80e1-5e0c9b6e632f.png)


