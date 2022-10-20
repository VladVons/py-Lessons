#!/bin/bash
# VladVons@gmail.com

Get()
{
  local aHost=$1
  local wget="wget --read-timeout=6 --tries=1 -qO-"

  echo $aHost
  Exec="$wget $aHost/$Cnt"
  $Exec
}

Loop()
{
  Cnt=0
  while true; do
    Cnt=$((Cnt+1))

    echo
    Get "localhost:8080/$Cnt"
    Get "localhost:8081/$Cnt"

    sleep 1
  done
}

Loop
