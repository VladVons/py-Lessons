import os
from ProjFiles import TProjFiles


def Main():
    PF = TProjFiles('/home/vladvons/Projects/py/py-vShops/src')
    PF.FilesLoad(['vShops.py', 'Task/SrvView/__init__.py', 'Task/SrvCtrl/__init__.py', 'Task/SrvModel/__init__.py'])
    PF.DirsLoad(['Conf/Default'])
    PF.DirsLoad(['IncP/view', 'IncP/ctrl', 'IncP/model'], True)
    PF.Release('Proj_vShops')

#os.system('clear')
Main()
