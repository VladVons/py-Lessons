# Created: 2023.01.12
# Author: Vladimir Vons <VladVons@gmail.com>
# License: GNU, see LICENSE for more details


import os
import re
import logging
import json
import gzip
import xml.dom.minidom as dom
#
from .Download import TDownload
from .Misc import FilterKeyErr


class TSiteMap():
    def __init__(self):
        self.Download = TDownload()
        self.Data = []

    def LoadFile(self, aName: str) -> str:
        logging.info('LoadFile(): %s', aName)

        Path = f'{self.Download.DirOut}/{aName}'
        with open(Path, 'r', encoding = 'utf8') as F:
            return F.read()

    async def LoadSiteMap(self, aUrl: str) -> list:
        Res = []

        UrlDown = await self.Download.GetUrl(aUrl)
        Err = FilterKeyErr(UrlDown)
        if (not Err):
            Data = UrlDown['data']
            Status = UrlDown['status']
            if (Status == 200):
                if (aUrl.endswith('.xml.gz')):
                    Data = gzip.decompress(Data)

                Data = Data.decode("utf-8")
                Urls = re.findall('<loc>(.*?)</loc>', Data)
                for Url in Urls:
                    if (Url.endswith('.xml')) or (Url.endswith('.xml.gz')):
                        Res += await self.LoadSiteMap(Url)
                    else:
                        Res.append(Url.rstrip('/'))
            else:
                logging.info('Sitemap error %s', Status)
        return Res

    async def SaveSiteMap(self, aUrl: str) -> list:
        Res = None

        UrlDown = await self.Download.GetUrl(aUrl)
        Err = FilterKeyErr(UrlDown)
        if (not Err):
            Data = UrlDown['data']
            Status = UrlDown['status']
            if (Status == 200):
                if (aUrl.endswith('.xml.gz')):
                    Data = gzip.decompress(Data)

                Res = Data.decode('utf-8')
                Urls = re.findall('<loc>(.*?)</loc>', Res)
                for Url in Urls:
                    if (Url.endswith('.xml')) or (Url.endswith('.xml.gz')):
                        File = Url.rsplit('/', maxsplit=1)[-1]
                        FileData = await self.SaveSiteMap(Url)
                        logging.info('Save %s', File)
                        with open(File, 'w') as F:
                            F.write(FileData)
            else:
                logging.info('Sitemap error %s', Status)
        return Res

    def _DoParse(self, aData: dict):
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

            Data = self._DoParse({'Path': Path, 'Title': Title, 'Image': Image})
            if (Data):
                self.Data.append(Data)

    def ParseDir(self):
        for File in sorted(os.listdir(self.Download.DirOut)):
            Path = f'{self.Download.DirOut}/{File}'
            if (Path.endswith('.xml')):
                Data = self.LoadFile(File)
                self.Parse(Data)

    def LoadData(self, aFile: str) -> bool:
        File = self.Download.DirOut + '/' + aFile
        if (os.path.exists(File)):
            with open(File, 'r', encoding = 'utf8') as F:
                self.Data = json.load(F)
                return True

    def SaveData(self, aFile: str):
        File = self.Download.DirOut + '/' + aFile
        with open(File, 'w', encoding = 'utf8') as F:
            json.dump(self.Data, F, indent=2, sort_keys=True, ensure_ascii = False)

    async def SaveImages(self):
        Urls = [x['Image'] for x in self.Data]
        await self.Download.GetUrls(Urls)
