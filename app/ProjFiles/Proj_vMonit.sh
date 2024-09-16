#!/bin/bash

Dir="./Proj_vMonit"
Ext="*.py"

{ find $Dir -type f -name "$Ext" -printf "%s+"; echo 0; } | bc
find $Dir -name "$Ext" | xargs wc
find $Dir -name "$Ext" | wc -l

python3 Proj_vMonit.py

cd $Dir
tar -czf .${Dir}.tar.gz .
