#!/bin/bash

Dir="./Proj_vShops"
Ext="*.py"

{ find $Dir -type f -name "$Ext" -printf "%s+"; echo 0; } | bc
find $Dir -name "$Ext" | xargs wc
find $Dir -name "$Ext" | wc -l
