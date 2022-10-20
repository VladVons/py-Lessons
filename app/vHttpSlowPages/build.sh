#!/bin/bash

# Copyright:   (c) 2022, Vlad Vons
# Author:      Vladimir Vons <VladVons@gmail.com>
# Created:     2022.02.16
# License:     GNU, see LICENSE for more details
# Description:


source ./const.conf


MakeDebControl()
{
echo "\
Package: $NameDeb
Version: $Ver
Architecture: $Platform
Section: web
Priority: optional
Depends: $Depends
Suggests:
Recommends:
Maintainer: Vladimir Vons <VladVons@gmail.com>
Description: Relay automation" > $DirDebRoot/src/DEBIAN/control
}

Deb()
{
  find ./ \( -name "*.pyc" -o -name "*.log" -o -name "__pycache__" \) -delete

  MakeDebControl

  rm -R $DirDeb 2>/dev/null
  cp -R $DirDebRoot/src/CONTENTS $DirDeb
  cp -R $DirDebRoot/src/DEBIAN $DirDeb

  #python3 -B setup.py install .
  pip3 install --upgrade .

  UserSite=$(python3 -m site --user-site)
  echo "user-site dir: $UserSite"

  mkdir -p $DirDeb/usr/lib/python3/dist-packages
  cp -rb $UserSite/$NamePy* $DirDeb/usr/lib/python3/dist-packages
  mkdir -p $DirDeb/usr/bin
  cp -rb ~/.local/bin/$NamePy* $DirDeb/usr/bin

  rm -f $DirDeb.deb
  dpkg-deb --build $DirDeb
  rm -R $DirDeb
}

Package()
{
  pipreqs $NamePy

  python3 -B setup.py sdist --formats=gztar
  rm -R $NamePy.egg-info
}

Install()
{ 
  pip3 install pipreqs 
}


#clear
case $1 in
    Deb)       "$1" "$2" "$3" ;;
    Package)   "$1" "$2" "$3" ;;
    Install)   "$1" "$2" "$3" ;;
esac
