import os
from ProjFiles import TProjFiles


def Main():
    PF = TProjFiles('/home/vladvons/Projects/py/py-vShops-B2B/src')
    PF.FilesLoad([
        'vShops-B2B.py.py' 
    ])
    PF.DirsLoad(['Conf/Tenant', 'Conf/Product0'])
    PF.DirsLoad(['Task', 'IncP'], True)
    PF.Release('Proj_vShops-B2B')

#os.system('clear')
Main()
