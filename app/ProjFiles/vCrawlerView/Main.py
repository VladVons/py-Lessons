# Created: 2024.09.10
# Author: Vladimir Vons, Oster Inc.
# License: GNU, see LICENSE for more details


from ProjFiles import TProjFiles


def Main():
    PF = TProjFiles('/home/vladvons/Projects/py/py-vCrawler/src', 'Proj_vCrawlerView')

    PF.FilesCopy([
        'vCrawler.sh',
        'Conf/View'
    ])

    PF.FilesLoad([
        'vCrawler.py',

        'IncP/LibModel.py',
        'IncP/LibCtrl.py'
    ])

    PF.DirsLoad([
      'MVC/Search',
      'Task/Search'
    ])

    PF.Release()

Main()
