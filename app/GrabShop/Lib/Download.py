# Created: 2023.01.12
# Author: Vladimir Vons <VladVons@gmail.com>
# License: GNU, see LICENSE for more details


import os
from urllib.parse import urlparse
import asyncio
import aiohttp


class TDownload():
    def __init__(self, aDirOut: str = '_Out'):
        self.DirOut = aDirOut
        self.OnFetch = None
        self.Cnt = 0

    def WriteFile(self, aName: str, aData):
        self.Cnt += 1
        #print(f'WriteFile() No: {self.Cnt}, Size: {len(aData)}, Name:{aName}')

        Path = self.DirOut + '/' + aName
        Dir = os.path.dirname(Path)
        os.makedirs(Dir, exist_ok = True)

        with open(Path, 'wb') as F:
            F.write(aData)

    async def Fetch(self, aUrl: str, aSession) -> tuple:
        try:
            async with aSession.get(aUrl) as Response:
                Data = await Response.read()
                return {'data': Data, 'status': Response.status}
        except Exception as E:
            print('Fetch err:', E, aUrl)

    async def FetchSem(self, aUrl: str, aSession, aSem, aIdx: int) -> tuple:
        async with aSem:
            print('FetchSem', aIdx, aUrl)

            FetchData = await self.Fetch(aUrl, aSession)
            if (FetchData):
                if (FetchData['status'] == 200):
                    if (self.OnFetch):
                        File = self.OnFetch(aUrl)
                    else:
                        Path = urlparse(aUrl)
                        File = ('%s%s' % (Path.netloc, Path.path))
                    self.WriteFile(File, FetchData['data'])
                Res = (FetchData['status'], aUrl)
            else:
                Res = (None, aUrl)
            return Res

    async def GetUrl(self, aUrl) -> tuple:
        async with aiohttp.ClientSession() as Session:
            return await self.Fetch(aUrl, Session)

    async def GetUrls(self, aUrl: list[str], aMaxConn: int = 5):
        Sem = asyncio.Semaphore(aMaxConn)
        async with aiohttp.ClientSession() as Session:
            print('Main. create tasks', len(aUrl))
            Tasks = [
                asyncio.create_task(self.FetchSem(Val, Session, Sem, Idx))
                for Idx, Val in enumerate(aUrl)
            ]

            print('Main. launch tasks')
            return await asyncio.gather(*Tasks)
