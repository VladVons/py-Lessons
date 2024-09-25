import os
from ProjFiles import TProjFiles


def Main():
    PF = TProjFiles('/home/vladvons/Projects/py/py-vMonit/src', 'Proj_vMonit')

    PF.FilesLoad([
        'vMonit.py'
    ])

    PF.DirsLoad([
     'Conf/Default', 'Task'
    ])

    PF.Release()

#os.system('clear')
Main()
