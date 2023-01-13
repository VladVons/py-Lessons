# Created: 2023.01.12
# Author: Vladimir Vons <VladVons@gmail.com>
# License: GNU, see LICENSE for more details


import os
import re
#
from .SiteMap import TSiteMap


class TFozzy(TSiteMap):
    def __init__(self):
        super().__init__()
        self.Download.OnFetch = self._OnFetch
        self.UrlToEan = {}

    def _OnFetch(self, aPath: str) -> str:
        return 'Image/' + self.UrlToEan.get(aPath) + '.jpg'

    def _Parse(self, aData):
        Ean = re.search(r'-(\d{8,13})\.html$', aData['Path'])
        if (Ean):
            aData['EAN'] = Ean.group(1)
            return aData

    async def SaveImages(self):
        self.UrlToEan = {x['Image']:x['EAN'] for x in self.Data}

        Urls = []
        for x in self.Data:
            File = self.Download.DirOut + '/' + self._OnFetch(x['Image'])
            if (not os.path.exists(File)):
                Urls.append(x['Image'])
        await self.Download.GetUrls(Urls)
