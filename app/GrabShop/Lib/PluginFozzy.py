# Created: 2023.01.12
# Author: Vladimir Vons <VladVons@gmail.com>
# License: GNU, see LICENSE for more details


import os
import re
#
from .SiteMap import TSiteMap


class TPlugin_Fozzy(TSiteMap):
    def __init__(self):
        super().__init__()

        self.Download.OnFetchWrite = self._OnFetchWrite
        self.UrlToEan = {}

    def _UrlToFile(self, aUrl: str) -> str:
        return 'Image/' + self.UrlToEan.get(aUrl) + '.jpg'

    async def _OnFetchWrite(self, aUrl: str, aData: dict):
        if (aData['status'] == 200):
            File = self._UrlToFile(aUrl)
            self.Download.WriteFile(File, aData['data'])

    def _DoParse(self, aData: dict) -> dict:
        Ean = re.search(r'-(\d{8,13})\.html$', aData['Path'])
        if (Ean):
            aData['EAN'] = Ean.group(1)
            return aData

    async def SaveImages(self):
        self.UrlToEan = {x['Image']:x['EAN'] for x in self.Data}
        UniqEan = []

        Urls = []
        for x in self.Data:
            if (not x['EAN'] in UniqEan):
                UniqEan.append(x['EAN'])

                File = self.Download.DirOut + '/' + self._UrlToFile(x['Image'])
                if (not os.path.exists(File)):
                    Urls.append(x['Image'])
        await self.Download.GetUrls(Urls)
