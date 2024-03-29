# Created: 2023.03.17
# Author: Vladimir Vons <VladVons@gmail.com>
# License: GNU, see LICENSE for more details


import os
import re


class TDirInfo():
    def __init__(self, aDir: str):
        self. Dir = aDir
        self.Incl = None
        self.Excl = None
        #self.Excl = r'.*\.(tmp|temp)$'

    def _Filter(self, aPath) -> bool:
        if (self.Excl) and (re.findall(self.Excl, aPath)):
            return False

        if (self.Incl) and (not re.findall(self.Incl, aPath)):
            return False

        return True

    @staticmethod
    def GetFileInfo(aFile: str) -> tuple:
        Lines = Size = 0
        try:
            with open(aFile, 'r', encoding = 'utf8') as F:
                Lines = len(F.readlines())
                Size = F.tell()
        except (PermissionError, FileNotFoundError):
            print(f'Errpr opening {aFile}')
        except (UnicodeDecodeError):
            Size = os.path.getsize(aFile)

        Ext = aFile.rsplit('.', maxsplit = 1)[-1]
        if ('/' in Ext) or (len(Ext) > 4):
            #Ext = aFile.rsplit('/', maxsplit = 1)[-1]
            Ext = '___'
        return (Ext, Size, Lines)

    def Walk(self) -> iter:
        def Recurs(aPath: str, aDepth: int):
            for File in sorted(os.listdir(aPath)):
                Path = aPath + '/' + File
                IsDir = os.path.isdir(Path)
                if (IsDir):
                    yield from Recurs(Path, aDepth + 1)

                if (self._Filter(File)):
                    yield (Path, IsDir, aDepth)
        yield from Recurs(self.Dir, 0)

    def Get(self) -> tuple:
        Res = {}
        MaxDepth = 0
        for Path, IsDir, Depth in self.Walk():
            if (IsDir):
                Ext = 'DIR'
                Size = Lines = 0
            else:
                Ext, Size, Lines = self.GetFileInfo(Path)

            if (Ext not in Res):
                Res[Ext] = []
            Res[Ext].append((Size, Lines))

            if (Depth > MaxDepth):
                MaxDepth = Depth
        return (Res, MaxDepth)

    def Show(self) -> dict:
        print('Parsing', self.Dir)
        Data, MaxDepth = self.Get()

        print()
        print(' No Ext   Count      Size   SizeMax      Lines   LinesMax')
        print('---------------------------------------------------------')
        FilesAll = SizeAll = LinesAll = 0
        for Idx, (Key, Val) in enumerate(sorted(Data.items())):
            Files = len(Val)

            Size, Lines = list(map(sum, zip(*Val)))
            SizeMax, LinesMax = list(map(max, zip(*Val)))

            FilesAll += Files
            SizeAll += Size
            LinesAll += Lines

            print(f'{Idx: 3} {Key:5} {Files:5} {Size / 1000 :8.1f}k {SizeMax / 1000 :8.1f}k {Lines: 10} {LinesMax: 10}')

        print()
        print(f'          {FilesAll:5} {SizeAll / 1000 :8.1f}k           {LinesAll: 10}')
        print(f'Depth     {MaxDepth:5}')


#Dir = '/var/www/opencart-4'
#Dir = '/home/vladvons/Projects/py/py-vShops/src'
Dir = '/home/vladvons/VirtEnv/python3.10/lib/python3.10/site-packages/aiohttp'
DirInfo = TDirInfo(Dir)
#DirInfo.Excl = r'.*\.(tmp|dat|xml|xlsx|jpg|png|gif|ico)$'
DirInfo.Show()
