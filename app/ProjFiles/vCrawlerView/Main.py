# Created: 2024.09.10
# Author: Vladimir Vons, Oster Inc.
# License: GNU, see LICENSE for more details


from ProjFiles import TProjFiles


def Main():
    PF = TProjFiles('/home/vladvons/Projects/py/py-vCrawler/src', 'Proj_vCrawlerView')

    PF.FilesCopy([
    ])

    PF.FilesLoad([
        'vCrawler.py',
        'IncP/LibCtrl.py',
        'IncP/LibModel.py'
    ])

    PF.DirsLoad([
      'MVC/Search',
      'Task/Search'
    ])

    PF.Release()

Main()
