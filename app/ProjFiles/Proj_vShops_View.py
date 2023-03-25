import os
from ProjFiles import TProjFiles


def Main():
    PF = TProjFiles('/home/vladvons/Projects/py/py-vShops/src')
    PF.FilesLoad(['vShops.py', 'Task/SrvView/__init__.py'])
    PF.DirsLoad(['Conf/Default'])
    PF.DirsLoad(['MVC/catalog/view', '/MVC/catalog/lang/ua'], True)
    PF.Release('Proj_vShops_View')

#os.system('clear')
Main()
