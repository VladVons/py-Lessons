#!/bin/bash

Dir="./Proj_vShops"
Ext="*.py"

python3 Main.py

#cp f_static/Task~Update.json $Dir/Conf/Default 

cd $Dir
tar -czf .${Dir}.tar.gz .