# Created: 2023.01.12
# Author: Vladimir Vons <VladVons@gmail.com>
# License: GNU, see LICENSE for more details


import os
import logging
import json
import xml.dom.minidom as dom
#
from .Download import TDownload


class TSiteMap():
    def __init__(self):
        self.Download = TDownload()
        self.Data = []

    def LoadFile(self, aName: str) -> list:
        logging.info('LoadFile(): %s', aName)

        Path = f'{self.Download.DirOut}/{aName}'
        with open(Path, 'r', encoding = 'utf8') as F:
            return F.read()

    def _Parse(self, aData: dict):
        raise NotImplementedError()

    def Parse(self, aData: str):
        logging.info('Parse()')

        Nodes = dom.parseString(aData).getElementsByTagName('url')
        for Node in Nodes:
            try:
                Path = Node.getElementsByTagName('loc')[0].firstChild.wholeText
                Title = Node.getElementsByTagName('image:title')[0].firstChild.wholeText
                Image = Node.getElementsByTagName('image:loc')[0].firstChild.wholeText
            except  Exception as _E:
                continue

            Data = self._Parse({'Path': Path, 'Title': Title, 'Image': Image})
            if (Data):
                self.Data.append(Data)

    def ParseDir(self):
        for File in sorted(os.listdir(self.Download.DirOut)):
            Path = f'{self.Download.DirOut}/{File}'
            if (Path.endswith('.xml')):
                Data = self.LoadFile(File)
                self.Parse(Data)

    def _OnFetch(self, aPath: str) -> str:
        return aPath

    def LoadData(self, aFile: str) -> bool:
        File = self.Download.DirOut + '/' + aFile
        if (os.path.exists(File)):
            with open(File, 'r', encoding = 'utf8') as F:
                self.Data = json.load(F)
                return True

    def SaveData(self, aFile: str):
        File = self.Download.DirOut + '/' + aFile
        with open(File, 'w', encoding = 'utf8') as F:
            json.dump(self.Data, F, indent=2, sort_keys=True, ensure_ascii=False)

    async def SaveImages(self):
        Urls = [x['Image'] for x in self.Data]
        await self.Download.GetUrls(Urls)
