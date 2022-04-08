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


class TProjFiles():
    def __init__(self):
        self.Filter = '.*\.log|.*\.pyc'
        self.Files = []

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
            for FileB in aFilesB + ['__init__']:
                self._FileAdd(FileA + '/' + FileB.strip() + '.py')
                self._FileAdd(FileA + '.py')
                self._FileAdd(os.path.dirname(aFileP) + FileA + '.py')

    def FileLoad(self, aFile: str):
        Patt1 = 'import\s+(.*)'
        Patt2 = 'from\s+(.*)\s+import\s+(.*)'
        #Patt3 = '__import__\((.*)\)'

        if (os.path.exists(aFile)):
            with open(aFile, 'r') as F:
                for Line in F.readlines():
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
            self.FileLoad(File)

    def DirsLoad(self, aDirs: list):
        for Dir in aDirs:
            for Root, Subdirs, Files in os.walk(Dir):
                for File in Files:
                    self.FileLoad(Root + '/' + File)

    def Release(self, aDir: str = 'Release'):
        SizeTotal = 0
        for Idx, File in enumerate(sorted(self.Files)):
            Dir = aDir + '/' + os.path.dirname(File)
            os.makedirs(Dir, exist_ok=True)
            shutil.copy(File, aDir + '/' + File) 

            Size = os.path.getsize(File)
            SizeTotal += Size 
            print('%2d, %4.2fk, %s' % (Idx + 1, Size / 1000, File))
        print('Size %4.2fk' % (SizeTotal / 1000))


def Project_1():
    PF = TProjFiles()
    #PF.FilesLoad(['vRelaySrv.py', 'App/Scraper/__init__.py', 'App/ScraperSrv/__init__.py'])
    PF.FilesLoad(['vRelaySrv.py', 'App/WebSrv/__init__.py', 'App/WebSrv/form/soup.py'])
    PF.DirsLoad(['Conf'])
    PF.Release()


if (__name__ == '__main__'):
    os.system('clear')
    Project_1()
