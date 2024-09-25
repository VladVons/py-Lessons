# Created: 2022.03.30
# Author: Vladimir Vons, Oster Inc.
# License: GNU, see LICENSE for more details
#
# Search project dependencies from a file or directory


import os
import sys
import re
import shutil


def GetLines(aFile: str) -> tuple:
    try:
        with open(aFile, 'r', encoding = 'utf8') as F:
            Lines = F.readlines()
            Size = F.tell()
    except UnicodeDecodeError:
        #print('Not a text file', aFile)
        Lines = []
        Size = os.path.getsize(aFile)
    return (Size, Lines)


class TFiles(list):
    Skip = r'.*\.log'

    def Filter(self, aFile: str) -> bool:
        if (self.Skip):
            Find = re.findall(self.Skip, aFile)
            return bool(Find)

    def Add(self, aFile: str):
        if (os.path.exists(aFile)) and (aFile not in self) and (not self.Filter(aFile)):
            self.append(aFile)
            return True

    def GetExtInf(self):
        Res = {}
        for xFile in self:
            Ext = xFile.rsplit('.', maxsplit = 1)[-1]
            if (Ext not in Res):
                Res[Ext] = []
            Size, Lines = GetLines(xFile)
            Res[Ext].append((Size, len(Lines)))
        return Res

class TProjFiles():
    def __init__(self, aSrc: str = '', aDst: str = 'Release'):
        self.PkgExt = set()
        self.PkgInt = set()
        self.PkgSkip = []

        self._BuiltIn = [x for x in sys.builtin_module_names if not x.startswith('_')]
        #self._DirExtPkg = site.getsitepackages()
        self._DirPy = os.path.dirname(os.__file__)
        self.Files = TFiles()

        if (aSrc):
            self.Dst = os.getcwd() + '/'
            os.chdir(aSrc)
        else:
            self.Dst = './'
        self.DirDst = self.Dst + aDst

    @staticmethod
    def _HasComment(aData: list[str]) -> list[str]:
        return [x for x in aData if not x.startswith('-')]

    @staticmethod
    def _GetFilesRecurs(aDir: str) -> list[str]:
        Res = []
        for Entry in os.listdir(aDir):
            Path = os.path.join(aDir, Entry)
            if os.path.isdir(Path):
                Res.extend(TProjFiles._GetFilesRecurs(Path))
            else:
                Res.append(Path)
        return Res

    def _FileAdd(self, aFile: str):
        if (self.Files.Add(aFile)):
            self.FileLoad(aFile)

    def _Find(self, aFileP: str , aFilesA: list, aFilesB: list = None):
        if (aFilesB is None):
            aFilesB = []

        for FileA in aFilesA:
            FileA = FileA.strip()

            for FileB in aFilesB + ['__init__']:
                self._FileAdd(FileA + '/' + FileB.strip() + '.py')
                self._FileAdd(FileA + '.py')
                self._FileAdd(os.path.dirname(aFileP) + FileA + '.py')

    def _FileExists(self, aFiles: list) -> str:
        for File in aFiles:
            if (os.path.exists(File)):
                return File

    def _PkgGroup(self, aFile: str, aVal1: str, aVal2: str):
        Module = aVal2 if (not aVal1) else aVal1
        if (not Module) or (Module in self.PkgInt) or (Module in self.PkgExt):
            return

        Module = Module.strip().split(' as ')[0]

        ModulePath = Module.replace('.', '/')
        Files = [ModulePath, ModulePath + '.py']
        if (Module.startswith('.')) or (self._FileExists(Files)):
            self.PkgInt.add(Module)
            return

        Files = [self._DirPy + '/' + Module, self._DirPy + '/' + Module + '.py']
        if (not self._FileExists(Files)) and (not Module in self._BuiltIn):
            self.PkgExt.add(Module)

    def GetPkgExt(self) -> list:
        return sorted(set([x.split('.')[0] for x in self.PkgExt]))

    def PkgIgnore(self, aVal: list):
        self.PkgSkip = aVal

    def FileLoad(self, aFile: str):
        if (not os.path.exists(aFile)):
            print('File not found', aFile)
            return

        _Size, Lines = GetLines(aFile)
        if (not Lines):
            self.Files.Add(aFile)
            return

        Patt1 = r'import\s+(.*)'
        Patt2 = r'from\s+(.*)\s+import\s+(.*)'
        #Patt3 = r'__import__\((.*)\)'

        self.Files.Add(aFile)

        InComment1 = False
        InComment2 = False
        for Line in Lines:
            Line = Line.strip()
            if (not Line) or (Line.startswith('#')):
                continue

            if (Line.startswith("'''")):
                InComment1 = not InComment1
            if (Line.startswith('"""')):
                InComment2 = not InComment2
            if (InComment1 or InComment2):
                continue

            Find = re.findall(Patt1 + '|' + Patt2, Line)
            if (Find):
                self._PkgGroup(aFile, *Find[0][:2])
                F1, F2, F3 = [i.replace('.', '/') for i in Find[0]]
                if (F1):
                    self._Find(aFile, F1.split(','))
                else:
                    Pkgs = F3.split(',')
                    Skip =  [xPkg for xPkg in Pkgs if (xPkg in self.PkgSkip)]
                    if (not Skip):
                        self._Find(aFile, F2.split(','), Pkgs)
        self._FileAdd(aFile)

    def FilesLoad(self, aFiles: list[str]):
        for xFile in self._HasComment(aFiles):
            self.FileLoad(xFile)

    def DirsCreate(self, aDirs: list[str]):
        for xDir in self._HasComment(aDirs):
            Path = f'{self.DirDst}/{xDir}'
            os.makedirs(Path, exist_ok=True)

    def FilesCopy(self, aFiles: list[str]):
        for xFile in self._HasComment(aFiles):
            if (os.path.isdir(xFile)):
                Files = self._GetFilesRecurs(xFile)
                for xFile in Files:
                    self.Files.Add(xFile)
            else:
                self.Files.Add(xFile)

    def DirsLoad(self, aDirs: list[str], aAll: bool = False):
        for xDir in self._HasComment(aDirs):
            for Root, Dirs, Files in os.walk(xDir):
                for xFile in Files:
                    Path = Root + '/' + xFile
                    if (aAll):
                        if (Path not in self.Files) and (not self.Files.Filter(Path)):
                            if (Path.endswith('.py')):
                                self.FileLoad(Path)
                            else:
                                self.Files.Add(Path)
                    else:
                        self.FileLoad(Path)
                if (aAll):
                    self.DirsLoad(Dirs, aAll)

    def Requires(self, aDir: str):
        PkgExt = self.GetPkgExt()
        Install = 'pip3 install ' + ' '.join(PkgExt)
        print(Install)


        File = 'requires.lst'
        Head = [
            '# sudo apt install python3-pip python3-dev gcc libpq-dev libffi-dev --no-install-recommends',
            '# curl -sS https://bootstrap.pypa.io/get-pip.py | python3',
            '',
            f'# {Install}',
            f'# pip3 install -r {File}',
        ]
        with open(aDir + '/' + File, 'w', encoding = 'utf-8') as F:
            F.write('\n'.join(Head))
            F.write('\n')
            F.write('\n')
            F.write('\n'.join(PkgExt))
            F.write('\n')

    def Release(self):
        def Copy():
            for Idx, File in enumerate(sorted(self.Files)):
                Dir = self.DirDst + '/' + os.path.dirname(File)
                os.makedirs(Dir, exist_ok=True)
                shutil.copy(File, self.DirDst + '/' + File)

                #Size = os.path.getsize(File)
                #print('%2d, %4.1fk, %s' % (Idx + 1, Size / 1000, File))
            print()
            self.Requires(self.DirDst)

        def Info():
            print(f'Project: {self.DirDst}')
            print()
            print(' No Ext Count     Size  Lines')
            print('------------------------------')

            FilesAll = SizeAll = LinesAll = 0
            for Idx, (Key, Val) in enumerate(sorted(self.Files.GetExtInf().items())):
                Files = len(Val)
                Size, Lines = list(map(sum, zip(*Val)))

                FilesAll += Files
                SizeAll += Size
                LinesAll += Lines

                print(f'{Idx + 1: 3} {Key:5} {Files:3} {Size / 1000 :7.2f}k {Lines: 6}')
            print()
            print(f'          {FilesAll:3} {SizeAll / 1000 :7.2f}k   {LinesAll}')

        Copy()
        print()
        Info()
