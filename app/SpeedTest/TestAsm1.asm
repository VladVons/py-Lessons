section .text
global TestAsm1

TestAsm1:
    ; Input parameters:
    ;   edi: pointer to the array (aArr)
    ;   esi: size of the array (aSize)
    ;   edx: value to find (aFind)

    xor     rax, rax        ; Initialize result to zero
    xor     ecx, ecx        ; Loop counter (i)
    test    rsi, rsi        ; Check if array size is zero
    jz      .end            ; If zero, return zero

.loop:
    cmp     ecx, esi        ; Compare loop counter with array size
    je      .end            ; If equal, exit the loop

    cmp     [rdi + rcx*4], edx  ; Compare array element with the value to find
    jne     .next           ; If not equal, go to the next iteration

    inc     eax             ; Increment the result if a match is found

.next:
    inc     ecx             ; Increment loop counter
    jmp     .loop           ; Jump back to the beginning of the loop

.end:
    ret
