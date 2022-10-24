import os
from ProjFiles import TProjFiles


def Main1():
    PF = TProjFiles('../src')
    PF.FilesLoad(['vRelaySrv.py', 'Task/Scraper/__init__.py', 'Task/ScraperSrv/__init__.py'])
    PF.DirsLoad(['Conf'])
    PF.DirsLoad(['Task/WebSrv'], True)

    PF.ExtPkg.add('cffi')
    PF.Release('Proj_vRelaySrv')

os.system('clear')
Main1()
