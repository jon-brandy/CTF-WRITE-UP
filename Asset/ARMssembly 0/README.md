# ARMssembly 0
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
What integer does this program print with arguments `4112417903` and `1169092511`? 
File: [chall.S]() Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})
## HINT:
1. Simple compare
## STEPS:
1. First, download the file given.
2. Let's check the file type first.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/189480628-fcd3c2d6-c800-4379-b81d-e21f4c01a0bf.png)

3. Looks like inside is an assembly code.
4. Now let's analyze the code.

> OUTPUT:

```asm
.arch armv8-a
	.file	"chall.c"
	.text
	.align	2
	.global	func1
	.type	func1, %function
func1:
	sub	sp, sp, #16
	str	w0, [sp, 12]
	str	w1, [sp, 8]
	ldr	w1, [sp, 12]
	ldr	w0, [sp, 8]
	cmp	w1, w0
	bls	.L2
	ldr	w0, [sp, 12]
	b	.L3
.L2:
	ldr	w0, [sp, 8]
.L3:
	add	sp, sp, 16
	ret
	.size	func1, .-func1
	.section	.rodata
	.align	3
.LC0:
	.string	"Result: %ld\n"
	.text
	.align	2
	.global	main
	.type	main, %function
main:
	stp	x29, x30, [sp, -48]!
	add	x29, sp, 0
	str	x19, [sp, 16]
	str	w0, [x29, 44]
	str	x1, [x29, 32]
	ldr	x0, [x29, 32]
	add	x0, x0, 8
	ldr	x0, [x0]
	bl	atoi
	mov	w19, w0
	ldr	x0, [x29, 32]
	add	x0, x0, 16
	ldr	x0, [x0]
	bl	atoi
	mov	w1, w0
	mov	w0, w19
	bl	func1
	mov	w1, w0
	adrp	x0, .LC0
	add	x0, x0, :lo12:.LC0
	bl	printf
	mov	w0, 0
	ldr	x19, [sp, 16]
	ldp	x29, x30, [sp], 48
	ret
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 7.5.0-3ubuntu1~18.04) 7.5.0"
	.section	.note.GNU-stack,"",@progbits
```

3. At the main function, notice the program called `atoi()` function twice and called `func1`. 
4. If we check the `func1`, we can see there's two parameters `w0` & `w1`.

![image](https://user-images.githubusercontent.com/70703371/190620591-c7d0754c-a440-42f0-a5bc-e6bf30d6578e.png)


6. At the `func1` value of `w1` & `w0` compared.

![image](https://user-images.githubusercontent.com/70703371/190620610-10236525-65ae-4002-b57b-2543c2c4f56d.png)


8. If one of them is **lower than or same**. 

![image](https://user-images.githubusercontent.com/70703371/190620627-6e3f32cc-04bc-4721-b365-99a3c849d40e.png)

9. Then do `.L2`, which based from the assembly code `w0` added `sp -8`. But if it's bigger , then load the `.L3`, which will return the value.

![image](https://user-images.githubusercontent.com/70703371/190621530-2e1533c2-e00a-4eaa-a6c9-de39fbcc2b8c.png)

10. From this point, now we know that the program wants us to give which is the bigger value from these decimal value -> `4112417903 and 1169092511`.
11. Since `4112417903` is bigger, let's convert it to hex value:

```py
a = 4112417903
print(hex(a))
```

> OUTPUT

![image](https://user-images.githubusercontent.com/70703371/190623448-9d0bb223-eaa4-4c2e-aa89-289658dee424.png)

12. Remove the `0x` and wrap it around with `picoCTF{}`.
13. Finally we got the flag!

## FLAG

```
picoCTF{F51E846F}
```
