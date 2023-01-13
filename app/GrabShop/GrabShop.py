# Created: 2023.01.12
# Author: Vladimir Vons <VladVons@gmail.com>
# License: GNU, see LICENSE for more details


import os
import sys
import time
import logging
import asyncio
#
from Lib.PluginFozzy import TFozzy


async def Run():
    SiteMap = TFozzy()

    File = 'Data.json'
    if (not SiteMap.LoadData(File)):
        SiteMap.ParseDir()
        SiteMap.SaveData(File)
    await SiteMap.SaveImages()
    await asyncio.sleep(1)

def Main():
    StartT = time.time()
    AppName = os.path.basename(sys.argv[0])
    print('%s, v1.01, 2023.01.12, vladvons@gmail.com' % (AppName))
    print('Python:', sys.version)
    print('Directory:', os.getcwd())

    logging.basicConfig(
        level = logging.INFO,
        format = '%(asctime)s [%(levelname)s] %(message)s',
        datefmt = '%Y-%m-%d %H:%M:%S',
        handlers = [
            logging.FileHandler(AppName + '.log'),
            logging.StreamHandler()
        ]
    )

    asyncio.run(Run())
    logging.info('async duration (s) %s', round(time.time() - StartT, 2))

Main()
