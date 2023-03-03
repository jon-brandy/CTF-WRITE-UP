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
