from ProjFiles import TProjFiles


def Main():
    PF = TProjFiles('/home/vladvons/Projects/py/py-vShops/src', 'Proj_vShops')

    PF.FilesCopy([
        'vShops.sh'
    ])

    PF.FilesLoad([
        'vShops.py',
        'Task/SrvView/__init__.py',
        'Task/SrvCtrl/__init__.py',
        'Task/SrvModel/__init__.py',
        'Task/SrvImg/__init__.py',
        'Task/Price/__init__.py',
        'Task/Queue/__init__.py',

        'IncP/__init__.py'
    ])

    PF.DirsLoad([
        'Conf/Default',
        'Task',
        'IncP'
    ])

    PF.DirsLoad([
      'MVC'
    ], True)

    PF.DirsCreate([
        'MVC/_common/lang',
        'Data/img'
    ])

    PF.Release()

Main()
