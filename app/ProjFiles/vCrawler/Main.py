import os
from ProjFiles import TProjFiles


def Main():
    PF = TProjFiles('/home/vladvons/Projects/py/py-vCrawler/src', 'Proj_vCrawler')

    PF.FilesCopy([
        'vCrawler.sh',
        'Conf/Default/Task.py',
        'Conf/Default/Task.Collector.Crawler.Api.json',
        'Conf/Default/Task~Collector~Crawler.json'
    ])

    PF.FilesLoad([
        'vCrawler.py',
        'IncP/LibCrawler.py'
    ])

    PF.DirsLoad([
      'Task/Collector/Crawler'
    ])

    PF.Release()

Main()
