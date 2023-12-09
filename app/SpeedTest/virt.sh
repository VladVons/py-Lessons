#!/bin/bash

clear
Dir=~/VirtEnv

py=python3
$py -B LoopSpeedTest.py

py=python3.9
source $Dir/$py/bin/activate
$py -B LoopSpeedTest.py

py=python3.12
source $Dir/$py/bin/activate
$py -B LoopSpeedTest.py

php LoopSpeedTest.php

./LoopSpeedTest2
