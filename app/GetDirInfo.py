# Created: 2023.03.17
# Author: Vladimir Vons <VladVons@gmail.com>
# License: GNU, see LICENSE for more details


import os


def GetFileInfo(aFile: str) -> tuple:
    try:
        with open(aFile, 'r', encoding = 'utf8') as F:
            Lines = len(F.readlines())
            Size = F.tell()
    except UnicodeDecodeError:
        Lines = 0
        Size = os.path.getsize(aFile)

    Ext = aFile.rsplit('.', maxsplit = 1)[-1]
    if ('/' in Ext) or (len(Ext) > 4):
        #Ext = aFile.rsplit('/', maxsplit = 1)[-1]
        Ext = '___'
    return (Ext, Size, Lines)

def GetFiles(aPath: str, aDepth: int = 0):
    for File in sorted(os.listdir(aPath)):
        Path = aPath + '/' + File
        IsDir = os.path.isdir(Path)
        if (IsDir):
            yield from GetFiles(Path, aDepth + 1)
        yield (Path, IsDir, aDepth)

def GetInfo(aDir: str) -> tuple:
    Res = {}
    MaxDepth = 0
    for Path, IsDir, Depth in GetFiles(Dir):
        if (IsDir):
            Ext = 'DIR'
            Size = Lines = 0
        else:
            Ext, Size, Lines = GetFileInfo(Path)

        if (Ext not in Res):
            Res[Ext] = []
        Res[Ext].append((Size, Lines))

        if (Depth > MaxDepth):
            MaxDepth = Depth
    return (Res, MaxDepth)

def ShowInfo(aDir: str) -> dict:
    print('Directory statistics parsing', aDir)
    print('parsing', aDir)
    Data, MaxDepth = GetInfo(aDir)

    print()
    print('Ext   Count      Size      Lines')
    print('--------------------------------')
    FilesAll = SizeAll = LinesAll = 0
    for Key, Val in sorted(Data.items()):
        Files = len(Val)
        Size, Lines = list(map(sum, zip(*Val)))

        FilesAll += Files
        SizeAll += Size
        LinesAll += Lines

        print(f'{Key:5} {Files:5} {Size / 1000 :8.1f}k {Lines: 10}')

    print()
    print(f'Total {FilesAll:5} {SizeAll / 1000 :8.1f}k {LinesAll: 10}')
    print(f'Depth {MaxDepth:5}')


#Dir = '/var/www/enabled/3w_shop4.oster.com.ua'
Dir = '/home/vladvons/Projects/py/py-vShops/src'
ShowInfo(Dir)
