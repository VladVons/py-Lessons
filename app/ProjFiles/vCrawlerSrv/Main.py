# Created: 2024.09.10
# Author: Vladimir Vons, Oster Inc.
# License: GNU, see LICENSE for more details


import os
from ProjFiles import TProjFiles


def Main():
    PF = TProjFiles('/home/vladvons/Projects/py/py-vCrawler/src', 'Proj_vCrawlerSrv')

    PF.FilesCopy([
        'vCrawler.sh'
    ])

    PF.FilesLoad([
        'vCrawler.py',
        'IncP/LibCrawler.py',
        'IncP/LibModel.py'
    ])

    PF.DirsLoad([
      'MVC/Collector/model',
      'Task/Collector/SrvModel'
    ])

    PF.Release()

Main()
