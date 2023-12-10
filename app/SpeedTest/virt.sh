#!/bin/bash

clear

_py()
{
    Dir=~/VirtEnv

    py=python3
    $py -B LoopSpeedTest.py

    py=python3.9
    source $Dir/$py/bin/activate
    $py -B LoopSpeedTest.py

    py=python3.12
    source $Dir/$py/bin/activate
    $py -B LoopSpeedTest.py
}

_php()
{
    php LoopSpeedTest.php
}

_cpp()
{
    rm *.o

    g++ -m64 -c LoopSpeedTest.cpp
    nasm -f elf64 TestAsm1.asm
    nasm -f elf64 TestAsm2.asm
    g++ -m64 -o LoopSpeedTest.bin LoopSpeedTest.o TestAsm1.o TestAsm2.o

    ./LoopSpeedTest.bin
}

_py
_php
_cpp
