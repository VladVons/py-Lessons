# Created: 2024.09.10
# Author: Vladimir Vons, Oster Inc.
# License: GNU, see LICENSE for more details


from ProjFiles import TProjFiles


def Main():
    PF = TProjFiles('/home/vladvons/Projects/py/py-vCrawler/src', 'Proj_vCrawlerView')

    PF.FilesCopy([
      'Inc/ParserSpec/LibComp/*.ini',
      'Data/Chat/vlad_site.session'
    ])

    PF.FilesLoad([
        'vCrawler.py',
        'IncP/LibCtrl.py',
        'IncP/LibImg.py',
        'IncP/LibModel.py'
    ])

    PF.DirsLoad([
      'Data/img',
      'MVC/Search/view/assets/js',
      'MVC/Search',
      'Task/Search',
      'Task/Chat'
    ])

    PF.Release()

Main()
