import os
from ProjFiles import TProjFiles


def Main1():
    PF = TProjFiles('../src')
    PF.FilesLoad(['vRelaySrv.py'])
    PF.DirsLoad(['Conf'])

    PF.DirsLoad(['App/WebSrv'], True)
    PF.FilesLoad(['App/Scraper/__init__.py', 'App/ScraperSrv/__init__.py'])

    PF.Release('Proj_1')


os.system('clear')
Main1()
