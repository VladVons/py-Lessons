from ProjFiles import TProjFiles


def Main():
    PF = TProjFiles('/home/vladvons/Projects/py/py-vAllNotes/src', 'Proj_vAllNotes')

    PF.FilesLoad([
        'vAllNotes.py'
    ])

    PF.DirsLoad([
      'MVC',
      'Task',
      'IncP'
    ])

    PF.Release()

#os.system('clear')
Main()
