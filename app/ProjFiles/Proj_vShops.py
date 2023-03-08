import os
from ProjFiles import TProjFiles


def Main():
    PF = TProjFiles('/home/vladvons/Projects/py/py-vShops/src')
    PF.FilesLoad(['vShops.py', 'Task/SrvView/__init__.py', 'Task/SrvCtrl/__init__.py', 'Task/SrvModel/__init__.py'])
    PF.DirsLoad(['Conf/Default'])
    #PF.DirsLoad(['MVC/View', 'MVC/Ctrl', 'MVC/Model', 'MVC/Lang'], True)
    PF.DirsLoad(['MVC'], True)
    PF.Release('Proj_vShops')

#os.system('clear')
Main()
