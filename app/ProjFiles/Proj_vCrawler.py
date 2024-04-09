import os
from ProjFiles import TProjFiles


def Main():
    PF = TProjFiles('/home/vladvons/Projects/py/py-vCrawler/src', 'Proj_vCrawler')
    PF.FilesLoad([
        'vCrawler.py',
        'Task/SrvModel/__init__.py',
        'Task/Crawler/__init__.py'
    ])
    PF.DirsLoad(['Conf/Default', 'Task/Price'])
    #PF.DirsLoad(['MVC/model', 'MVC/crawler'], True)
    PF.DirsLoad(['MVC'], True)
    PF.Release()

#os.system('clear')
Main()
