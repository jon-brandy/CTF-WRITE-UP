# Let's get dynamic
> Write-up author: jon-brandy
## DESCRIPTION:
Can you tell what this file is reading? chall.S

## HINT:
1. Running this in a debugger would be helpful
## STEPS:
1. Given an assembly file.

> asm file

```asm
	.file	"chall.c"
	.text
	.section	.rodata
	.align 8
.LC1:
	.string	"Correct! You entered the flag."
.LC2:
	.string	"No, that's not right."
	.align 8
.LC0:
	.string	"\002qs\312\307*\207\375\313-\370\371+\361\025I\020<"
	.string	"TL\r\357\247C\250\002M\367\314\231\223\327\210\226\230\030\370\306*\205LX3\312\353Q\237\347"
	.text
	.globl	main
	.type	main, @function
main:
.LFB5:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	pushq	%rbx
	subq	$296, %rsp
	.cfi_offset 3, -24
	movl	%edi, -292(%rbp)
	movq	%rsi, -304(%rbp)
	movq	%fs:40, %rax
	movq	%rax, -24(%rbp)
	xorl	%eax, %eax
	movq	.LC0(%rip), %rax
	movq	8+.LC0(%rip), %rdx
	movq	%rax, -144(%rbp)
	movq	%rdx, -136(%rbp)
	movq	16+.LC0(%rip), %rax
	movq	24+.LC0(%rip), %rdx
	movq	%rax, -128(%rbp)
	movq	%rdx, -120(%rbp)
	movq	32+.LC0(%rip), %rax
	movq	40+.LC0(%rip), %rdx
	movq	%rax, -112(%rbp)
	movq	%rdx, -104(%rbp)
	movzwl	48+.LC0(%rip), %eax
	movw	%ax, -96(%rbp)
	movabsq	$-7866547665503188383, %rax
	movabsq	$750938240303713972, %rdx
	movq	%rax, -80(%rbp)
	movq	%rdx, -72(%rbp)
	movabsq	$-245100717349187545, %rax
	movabsq	$-1321891645065211527, %rdx
	movq	%rax, -64(%rbp)
	movq	%rdx, -56(%rbp)
	movabsq	$4728704058583732155, %rax
	movabsq	$-7828694793552836984, %rdx
	movq	%rax, -48(%rbp)
	movq	%rdx, -40(%rbp)
	movw	$185, -32(%rbp)
	movq	stdin(%rip), %rdx
	leaq	-208(%rbp), %rax
	movl	$49, %esi
	movq	%rax, %rdi
	call	fgets@PLT
	movl	$0, -276(%rbp)
	jmp	.L2
.L3:
	movl	-276(%rbp), %eax
	cltq
	movzbl	-144(%rbp,%rax), %edx
	movl	-276(%rbp), %eax
	cltq
	movzbl	-80(%rbp,%rax), %eax
	xorl	%eax, %edx
	movl	-276(%rbp), %eax
	xorl	%edx, %eax
	xorl	$19, %eax
	movl	%eax, %edx
	movl	-276(%rbp), %eax
	cltq
	movb	%dl, -272(%rbp,%rax)
	addl	$1, -276(%rbp)
.L2:
	movl	-276(%rbp), %eax
	movslq	%eax, %rbx
	leaq	-144(%rbp), %rax
	movq	%rax, %rdi
	call	strlen@PLT
	cmpq	%rax, %rbx
	jb	.L3
	leaq	-272(%rbp), %rcx
	leaq	-208(%rbp), %rax
	movl	$49, %edx
	movq	%rcx, %rsi
	movq	%rax, %rdi
	call	memcmp@PLT
	testl	%eax, %eax
	je	.L4
	leaq	.LC1(%rip), %rdi
	call	puts@PLT
	movl	$0, %eax
	jmp	.L6
.L4:
	leaq	.LC2(%rip), %rdi
	call	puts@PLT
	movl	$1, %eax
.L6:
	movq	-24(%rbp), %rcx
	xorq	%fs:40, %rcx
	je	.L7
	call	__stack_chk_fail@PLT
.L7:
	addq	$296, %rsp
	popq	%rbx
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE5:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.0"
	.section	.note.GNU-stack,"",@progbits

```

2. Based from the hint, we could get the flag by running it with a debugger.
3. Hence, we need to compile this to an ELF file.
4. Let's compile it -> `gcc chall.S -o compiled`.
5. Since my linux is x64, hence if i run the default gcc compile, then the executable file shall compiled in 64 bit binary file.

![image](https://user-images.githubusercontent.com/70703371/222489483-594b1db6-89b5-4fc7-8d93-7bcc9d7ab523.png)


6. Let's use gdb now and check all the functions avail.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/222489765-245f63a0-62f8-4da1-98f1-b4e2d06598e3.png)


7. Since we're compiling an assembly file to binary, it's best to renew the offset/address that already written in the base address.
8. To do that, first set a breakpoint at 0x1, then run it.

> NOTES:

```
The breakpoint can be anywhere, we just want to trigger the renewal.
```

> RESULT

![image](https://user-images.githubusercontent.com/70703371/222490762-36c8e1a1-861a-448a-a6ac-abefd3f74c12.png)


9. Now check the functions avail.

> RESULT

![image](https://user-images.githubusercontent.com/70703371/222490891-b64457de-fff8-41f4-9946-15a0fc782fe3.png)


10. Great! Let's delete the breakpoints now.
11. Next, let's set a breakpoint at the `memcp@plt` function, then run the binary.

> ENTER ANY STRINGS WITH ANY LENGTH

![image](https://user-images.githubusercontent.com/70703371/222491802-f2d19191-b3c8-49f5-bae3-df0ad835ae12.png)


> RESULT

![image](https://user-images.githubusercontent.com/70703371/222491925-6e5a1fc4-26de-4215-978f-fa868b5388b3.png)


12. Notice, we can see there's a leak value at the **RSI** gadget.

![image](https://user-images.githubusercontent.com/70703371/222492356-65b337f9-4fbd-4790-8bbf-78f638e26ba4.png)


13. Means it comparing our value to the value stored in **RSI**.
14. To see the leaked strings in full, use this command -> 

