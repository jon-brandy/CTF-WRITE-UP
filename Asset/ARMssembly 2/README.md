# ARMssembly 2
> Write-up author: jon-brandy
## DESCRIPTION:
What integer does this program print with argument 2610164910? 
File: chall_2.S Flag format: picoCTF{XXXXXXXX} -> (hex, lowercase, no 0x, and 32 bits. ex. 5614267 would be picoCTF{0055aabb})
## HINT:
1. Loops
## STEPS:
1. Given an assembly file.

```asm
	.arch armv8-a
	.file	"chall_2.c"
	.text
	.align	2
	.global	func1
	.type	func1, %function
func1:
	sub	sp, sp, #32
	str	w0, [sp, 12]
	str	wzr, [sp, 24]
	str	wzr, [sp, 28]
	b	.L2
.L3:
	ldr	w0, [sp, 24]
	add	w0, w0, 3
	str	w0, [sp, 24]
	ldr	w0, [sp, 28]
	add	w0, w0, 1
	str	w0, [sp, 28]
.L2:
	ldr	w1, [sp, 28]
	ldr	w0, [sp, 12]
	cmp	w1, w0
	bcc	.L3
	ldr	w0, [sp, 24]
	add	sp, sp, 32
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
	str	w0, [x29, 28]
	str	x1, [x29, 16]
	ldr	x0, [x29, 16]
	add	x0, x0, 8
	ldr	x0, [x0]
	bl	atoi
	bl	func1
	str	w0, [x29, 44]
	adrp	x0, .LC0
	add	x0, x0, :lo12:.LC0
	ldr	w1, [x29, 44]
	bl	printf
	nop
	ldp	x29, x30, [sp], 48
	ret
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 7.5.0-3ubuntu1~18.04) 7.5.0"
	.section	.note.GNU-stack,"",@progbits
```

2. Let's start by analyzing the main function.

```asm
main:
	stp	x29, x30, [sp, -48]!
	add	x29, sp, 0
	; store the 1st arg of the program 
	;(which passed into the wo register) on the stack at 
	; an offset of 28 bytes from the frame pointer x29
	str	w0, [x29, 28] 
	str	x1, [x29, 16] ; store the 2nd arg , at the offset of 16 bytes
	ldr	x0, [x29, 16] ; load the 2nd arg to x0
	add	x0, x0, 8 ; add 8 to the address stored in x0 to skip the first 8 bytes of the user input string
	ldr	x0, [x0] ; load the integer value from the address pointed to by x0 (the user input)
	bl	atoi ; convert the user input string into an integer
	bl	func1 ; call the func1 with the integer value obtained from the user input
	; store the return value of func1 (which is an integer)
	; on the stack at an offset of 44 bytes from the frame pointer x29
	str	w0, [x29, 44] 
	adrp	x0, .LC0 ; load the address of the format string ".LC0" into register x0
	add	x0, x0, :lo12:.LC0 ; add the lower 12 bits of the address of the format string to x0
	ldr	w1, [x29, 44] ; load the integer return value of func1 from the stack into register w1
	bl	printf ; print the format string stored in x0 and integer value stored in w1
	nop
	ldp	x29, x30, [sp], 48
	ret
	.size	main, .-main
	.ident	"GCC: (Ubuntu/Linaro 7.5.0-3ubuntu1~18.04) 7.5.0"
	.section	.note.GNU-stack,"",@progbits
```

3. Based from the description, the user input strings is -> `2610164910`.
4. Now we know the input used at the func1.
5. Next, let's analyze func1

```asm
func1:
	sub	sp, sp, #32 ; reserves a block of 32 bytes on the stack by substract 32 from the stack pointer.
	str	w0, [sp, 12] ; [sp + 12] stored the user input -> 2610164910
	str	wzr, [sp, 24] ; [sp + 24] stored 0
	str	wzr, [sp, 28] ; [sp + 28] stored 0
	b	.L2 ; branches to .L2
```

6. Since it's branching to .L2, let's analyze .L2 then.

```asm

```
