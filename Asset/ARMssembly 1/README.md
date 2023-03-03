# ARMssembly 1
#### Write-up author: [jon-brandy](https://github.com/jon-brandy)
## DESCRIPTION:
For what argument does this program print `win` with variables 81, 0 and 3? File: chall_1.S 
Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 
5614267 would be picoCTF{0055aabb})
## HINT:
1. Shifts
## STEPS:
1. First, download the file given.
2. Then let's analyze the assembly code given.

> CHALL 1.S

```asm
	.arch armv8-a
	.file	"chall_1.c"
	.text
	.align	2
	.global	func
	.type	func, %function
func:
	sub	sp, sp, #32
	str	w0, [sp, 12]
	mov	w0, 81
	str	w0, [sp, 16]
	str	wzr, [sp, 20]
	mov	w0, 3
	str	w0, [sp, 24]
	ldr	w0, [sp, 20]
	ldr	w1, [sp, 16]
	lsl	w0, w1, w0
	str	w0, [sp, 28]
	ldr	w1, [sp, 28]
	ldr	w0, [sp, 24]
	sdiv	w0, w1, w0
	str	w0, [sp, 28]
	ldr	w1, [sp, 28]
	ldr	w0, [sp, 12]
	sub	w0, w1, w0
	str	w0, [sp, 28]
	ldr	w0, [sp, 28]
	add	sp, sp, 32
	ret
	.size	func, .-func
	.section	.rodata
	.align	3
.LC0:
	.string	"You win!"
	.align	3
.LC1:
	.string	"You Lose :("
	.text
	.align	2
	.global	main
	.type	main, %function
main:
	stp	x29, x30, [sp, -48]!
	add	x29, sp, 0
	str	w0, [x29, 28]
	str	x1, [x29, 16]
	ldr	x0, [x29, 16]
	add	x0, x0, 8
	ldr	x0, [x0]
	bl	atoi
	str	w0, [x29, 44]
	ldr	w0, [x29, 44]
	bl	func
	cmp	w0, 0
	bne	.L4
	adrp	x0, .LC0
	add	x0, x0, :lo12:.LC0
	bl	puts
	b	.L6
.L4:
	adrp	x0, .LC1
	add	x0, x0, :lo12:.LC1
	bl	puts
.L6:
	nop
	ldp	x29, x30, [sp], 48
	ret
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 7.5.0-3ubuntu1~18.04) 7.5.0"
	.section	.note.GNU-stack,"",@progbits

```

3. Seems like our point of interest is at the `func()`.
4. Here's what happen there.

```asm
func:
	sub	sp, sp, #32 ; reserve 32 bytes of space on the stack by substracting32 from the value in sp
	str	w0, [sp, 12] ; stores undefined value from w0 to [sp + 12] 
	mov	w0, 81 ; moves 81 to w0
	str	w0, [sp, 16] ; str (store a register value into memory) -> [sp + 16] = 81
	str	wzr, [sp, 20] ; xzr/wzr hold 0 values -> hence -> [sp + 20] = 0
	mov	w0, 3 ; moves 3 to w0
	str	w0, [sp, 24] ; [sp + 24] = 3
	ldr	w0, [sp, 20] ; w0 = 0
	ldr	w1, [sp, 16] ; ldr -> load something from memory into register -> w1 = 81
	lsl	w0, w1, w0 ; lsl (logical shift left) -> 81 << 0 = 81 (in decimal) and stored it into w0.
	str	w0, [sp, 28] ; [sp + 28] = 81
	ldr	w1, [sp, 28] ; w1 = [sp + 28] = 81
	ldr	w0, [sp, 24] ; w0 = [sp + 24] = 3
	sdiv	w0, w1, w0 ; signed division (sdiv) -> w1 by w0 (divide 81 by 3) = 27
	str	w0, [sp, 28] ; [sp + 28] = 27
	ldr	w1, [sp, 28] ; w1 = 27
	ldr	w0, [sp, 12] ; stored undefined value to w0
	sub	w0, w1, w0 ; substract -> w0 - w1
	str	w0, [sp, 28] ; [sp + 28] = 27
	ldr	w0, [sp, 28] ; w0 = 27
	add	sp, sp, 32
	ret
	.size	func, .-func
	.section	.rodata
	.align	3
```

5. Then looking at the main functions, we know if the user's input makes the substraction result 0, hence the program shall continue to .LC0.

![image](https://user-images.githubusercontent.com/70703371/222640735-a5ded69e-0dc8-4b82-ab5d-0d4e6babf4b3.png)


![image](https://user-images.githubusercontent.com/70703371/222640758-a79a8523-ddcc-4758-bb3a-1180eceb66aa.png)


6. Hence, we know the user input must be 27.
7. Convert 27 to hex -> `1B` -> `0x0000001B` -> `0x0000001b` (lowercase)
8. Got the flag!

```
picoCTF{0000001b}
```
