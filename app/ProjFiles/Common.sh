#!/bin/bash

Backup()
{
  aFile="$1";

  Dir="backup"
  mkdir -p $Dir

  File="${aFile##*/}"
  Name="${File%%.*}"
  Ext="${File#"$Name."}"

  Cnt=1
  while true; do
    NewFile="$Dir/${Name}_${Cnt}.${Ext}"
    if [[ ! -e "$NewFile" ]]; then
      break
    fi
    ((Cnt++))
  done

  cp $File $NewFile
}

Build()
{
  rm -r $cDir 2>/dev/null

  python3 -B Main.py

  cp -r  f_static/* $cDir/

  File="${cDir}.tar.gz"
  rm $File 2>/dev/null

  tar -czf $File -C $cDir .
  rm -r $cDir

  Backup "$File"
}
