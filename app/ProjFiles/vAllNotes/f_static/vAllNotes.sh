#!/bin/bash

py=python3.12
Dir=~/VirtEnv/$py
source $Dir/bin/activate

$py -B vAllNotes.py --conf Dev
