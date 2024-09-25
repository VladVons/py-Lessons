#!/bin/bash

Build()
{
  rm -r $cDir 2>/dev/null

  python3 Main.py

  cp -r  f_static/* $cDir/

  File="${cDir}.tar.gz"
  rm $File 2>/dev/null
  tar -czf $File -C $cDir .

  rm -r $cDir
}
