import os
from ProjFiles import TProjFiles


def Main():
    PF = TProjFiles('/home/vladvons/Projects/py/py-vShops/src', 'Proj_vShops')
    PF.FilesLoad([
        'vShops.py',
        'Task/SrvView/__init__.py',
        'Task/SrvCtrl/__init__.py',
        'Task/SrvModel/__init__.py',
        'Task/SrvImg/__init__.py',
        'Task/Price/__init__.py',
        'Task/Queue/__init__.py'
    ])
    PF.DirsLoad(['Conf/Default', 'Task/Price'])
    #PF.DirsLoad(['MVC/View', 'MVC/Ctrl', 'MVC/Model', 'MVC/Lang'], True)
    PF.DirsLoad(['MVC'], True)
    PF.DirsCreate(['MVC/_common/lang', 'Data/img'])
    PF.Release()

#os.system('clear')
Main()
