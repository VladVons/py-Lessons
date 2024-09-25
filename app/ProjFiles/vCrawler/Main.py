# Created: 2024.09.10
# Author: Vladimir Vons, Oster Inc.
# License: GNU, see LICENSE for more details


from ProjFiles import TProjFiles


def Main():
    PF = TProjFiles('/home/vladvons/Projects/py/py-vCrawler/src', 'Proj_vCrawler')

    PF.FilesCopy([
        'vCrawler.sh',
        'Conf/Client/Task.py',
        'Conf/Client/Task.Collector.Crawler.Api.json',
        'Conf/Client/Task~Collector~Crawler.json'
    ])

    PF.FilesLoad([
        'vCrawler.py',
        'IncP/LibCrawler.py'
    ])

    PF.DirsLoad([
      'MVC/Collector/crawler',
      'Task/Collector/Crawler'
    ])

    PF.Release()

Main()
