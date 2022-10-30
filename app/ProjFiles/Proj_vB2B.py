import os
from ProjFiles import TProjFiles


def Main1():
    PF = TProjFiles('/home/vladvons/Projects/py/py-vB2B/src')
    PF.FilesLoad(['vB2B.py', 'Task/Price/Main.py', 'vB2B.sh'])
    PF.DirsLoad(['Conf'])
    PF.DirsLoad(['Task'], not True)
    PF.PkgExt.update(['email_validator'])
    PF.Release('Proj_vB2B')

os.system('clear')
Main1()
