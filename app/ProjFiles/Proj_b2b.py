import os
from ProjFiles import TProjFiles


def Main1():
    PF = TProjFiles('../src')
    PF.FilesLoad(['b2b.py', 'Task/Price/Main.py'])
    PF.DirsLoad(['Conf'])
    PF.DirsLoad(['Task'], not True)
    PF.Release('Proj_b2b')

os.system('clear')
Main1()