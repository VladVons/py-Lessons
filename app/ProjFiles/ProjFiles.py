'''
Author:      Vladimir Vons, Oster Inc.
Created:     2022.03.30
License:     GNU, see LICENSE for more details
Description:

Search project dependencies from a file or directory
'''


import os
import re
import shutil
import site


class TProjFiles():
    def __init__(self, aSrc: str = ''):
        self.Filter = '.*\.log|.*\.LOG'
        self.Files = []
        self.Lines = 0
        self.ExtPkg = set()
        self.DirExtPkg = site.getsitepackages()[0]

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
        if (os.path.exists(aFile)) and (not aFile in self.Files) and (not self._Filter(aFile)):
            self.Files.append(aFile)
            self.FileLoad(aFile)

    def _Find(self, aFileP: str , aFilesA: list, aFilesB: list = []):
        for FileA in aFilesA:
            FileA = FileA.strip()

            ExtPkgPath = self.DirExtPkg + '/' + FileA
            if (os.path.exists(ExtPkgPath)):
                self.ExtPkg.add(FileA.split('/')[0])

            for FileB in aFilesB + ['__init__']:
                self._FileAdd(FileA + '/' + FileB.strip() + '.py')
                self._FileAdd(FileA + '.py')
                self._FileAdd(os.path.dirname(aFileP) + FileA + '.py')

    def FileLoad(self, aFile: str):
        Patt1 = 'import\s+(.*)'
        Patt2 = 'from\s+(.*)\s+import\s+(.*)'
        #Patt3 = '__import__\((.*)\)'

        if (os.path.exists(aFile)):
            if (not self._Filter(aFile)):
                try:
                    with open(aFile, 'r') as F:
                        Lines = F.readlines()
                except UnicodeDecodeError:
                    print('Not a text file', aFile)
                    return

                self.Lines += len(Lines)
                for Line in Lines:
                    Find = re.findall(Patt1 + '|' + Patt2, Line)
                    if (Find) and (not Line.startswith('#')):
                        F1, F2, F3 = [i.replace('.', '/') for i in Find[0]]
                        if (F1):
                            self._Find(aFile, F1.split(','))
                        else:
                            self._Find(aFile, F2.split(','), F3.split(','))
                self._FileAdd(aFile)
        else:
            print('File not found', aFile)

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
                        if (not Path in self.Files) and (not self._Filter(Path)):
                            if (Path.endswith('.py')):
                                self.FileLoad(Path)
                            else:
                                self.Files.append(Path)
                    else:
                        self.FileLoad(Path)

                if (aAll):
                    self.DirsLoad(Dirs, aAll)


    def Requires(self, aDir: str):
        ExtPkg = sorted(self.ExtPkg)
        Install = 'pip3 install ' + ' '.join(ExtPkg)
        print(Install)

        File = 'requires.txt'
        Head = [
            '# sudo apt install python3-pip python3-dev gcc libpq-dev libffi-dev --no-install-recommends',
            '# curl -sS https://bootstrap.pypa.io/get-pip.py | python3',
            f'# pip3 install -r {File}',
            ''
        ]
        with open(aDir + '/' + File, 'w') as F:
            F.write('\n'.join(Head))
            F.write('\n'.join(ExtPkg))
            F.write('\n')

    def Release(self, aDir: str = 'Release'):
        SizeTotal = 0
        DirDst = self.Dst + aDir
        for Idx, File in enumerate(sorted(self.Files)):
            Dir = DirDst + '/' + os.path.dirname(File)
            os.makedirs(Dir, exist_ok=True)
            shutil.copy(File, self.Dst + aDir + '/' + File)

            Size = os.path.getsize(File)
            SizeTotal += Size
            print('%2d, %4.1fk, %s' % (Idx + 1, Size / 1000, File))
        print('Size %4.1fk, Lines: %s' % (SizeTotal / 1000, self.Lines))

        print()
        self.Requires(DirDst)
