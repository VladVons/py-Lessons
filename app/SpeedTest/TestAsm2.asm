section .text
global TestAsm2

TestAsm2:
    ; Input
    ; rdi pointer to the array (aArr)
    ; esi size of the array (aSize)
    ; edx value to find (aFind)

    xor     eax, eax        ; Initialize result to zero
    test    rsi, rsi        ; Check if array size is zero
    jz      .end            ; If zero, return zero

.loop:
    cmp     [rdi], edx      ; Compare array element with the value to find
    jne     .next           ; If not equal, go to the next iteration

    inc     eax             ; Increment the result if a match is found

.next:
    add     rdi, 4          ; inc int4 pointer
    dec     esi             ; Increment loop counter
    jnz     .loop           ; Jump back to the beginning of the loop

.end:
    ret
