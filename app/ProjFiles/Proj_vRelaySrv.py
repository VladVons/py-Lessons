import os
from ProjFiles import TProjFiles


def Main():
    PF = TProjFiles('/home/vladvons/Projects/py/py-vRelaySrv/src')
    PF.FilesLoad(['vRelaySrv.py', 'Task/Scraper/__init__.py', 'Task/ScraperSrv/__init__.py'])
    PF.DirsLoad(['Conf'])
    PF.DirsLoad(['Task/WebSrv'], True)
    PF.PkgExt.update(['cffi', 'lxml'])
    PF.Release('Proj_vRelaySrv')

os.system('clear')
Main()
