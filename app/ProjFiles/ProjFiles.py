# Created: 2022.03.30
# Author: Vladimir Vons, Oster Inc.
# License: GNU, see LICENSE for more details
#
# Search project dependencies from a file or directory


import os
import sys
import re
import shutil


class TProjFiles():
    def __init__(self, aSrc: str = ''):
        self.Filter = r'.*\.log'
        self.PkgExt = set()
        self.PkgInt = set()

        self._Files = []
        self._BuiltIn = [x for x in sys.builtin_module_names if not x.startswith('_')]
        #self._DirExtPkg = site.getsitepackages()
        self._DirPy = os.path.dirname(os.__file__)
        self._Lines = 0


        if (aSrc):
            self.Dst = os.getcwd() + '/'
            os.chdir(aSrc)
        else:
            self.Dst = './'

    def _Filter(self, aFile: str) -> bool:
        if (self.Filter):
            Find = re.findall(self.Filter, aFile)
            return bool(Find)

    def _FileAdd(self, aFile: str):
        if (os.path.exists(aFile)) and (not aFile in self._Files) and (not self._Filter(aFile)):
            self._Files.append(aFile)
            self.FileLoad(aFile)

    def _Find(self, aFileP: str , aFilesA: list, aFilesB: list = []):
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

    def FileLoad(self, aFile: str):
        if (not os.path.exists(aFile)):
            print('File not found', aFile)
            return

        try:
            with open(aFile, 'r') as F:
                Lines = F.readlines()
        except UnicodeDecodeError:
            #print('Not a text file', aFile)
            return

        Patt1 = r'import\s+(.*)'
        Patt2 = r'from\s+(.*)\s+import\s+(.*)'
        #Patt3 = r'__import__\((.*)\)'

        self._Lines += len(Lines)

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
                    self._Find(aFile, F2.split(','), F3.split(','))
        self._FileAdd(aFile)

    def FilesLoad(self, aFiles: list):
        for File in aFiles:
            if (not File.startswith('-')):
                self.FileLoad(File)

    def DirsLoad(self, aDirs: list, aAll: bool = False):
        for Dir in aDirs:
            if (Dir.startswith('-')):
                continue

            for Root, Dirs, Files in os.walk(Dir):
                for File in Files:
                    Path = Root + '/' + File
                    if (aAll):
                        if (not Path in self._Files) and (not self._Filter(Path)):
                            if (Path.endswith('.py')):
                                self.FileLoad(Path)
                            else:
                                self._Files.append(Path)
                    else:
                        self.FileLoad(Path)

                if (aAll):
                    self.DirsLoad(Dirs, aAll)


    def Requires(self, aDir: str):
        PkgExt = self.GetPkgExt()
        Install = 'pip3 install ' + ' '.join(PkgExt)
        print(Install)


        File = 'requires.txt'
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

    def Release(self, aDir: str = 'Release'):
        SizeTotal = 0
        DirDst = self.Dst + aDir
        for Idx, File in enumerate(sorted(self._Files)):
            Dir = DirDst + '/' + os.path.dirname(File)
            os.makedirs(Dir, exist_ok=True)
            shutil.copy(File, self.Dst + aDir + '/' + File)

            Size = os.path.getsize(File)
            SizeTotal += Size
            print('%2d, %4.1fk, %s' % (Idx + 1, Size / 1000, File))
        print('Size %4.1fk, Lines: %s' % (SizeTotal / 1000, self._Lines))

        print()
        self.Requires(DirDst)
