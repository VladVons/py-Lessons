#!/bin/bash


py=python3
Dir=~/virt/$py
source $Dir/bin/activate

$py -B vCrawler.py --conf Client
