#!/bin/bash


Slow() 
{
    for File in $(ls *.log); do
        echo
        echo "$File"
        grep "task:" $File | sort --reverse --numeric-sort -k 13 | head -20
    done
}

Slow
