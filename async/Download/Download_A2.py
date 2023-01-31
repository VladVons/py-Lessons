'''
python async example
VladVons@gmail.com
2022.03.28
'''

import os
import time
import asyncio
import aiohttp
from urllib.parse import urlparse


class TDownload():
    def __init__(self, aFileTail: str = '', aDirOut: str = 'Out'):
        self.FileTail = aFileTail
        self.DirOut = aDirOut
        if (aDirOut != '.'):
            os.makedirs(aDirOut, exist_ok = True)

    def WriteFile(self, aName: str, aData):
        print('WriteFile', aName, len(aData))
        with open(self.DirOut + '/' + aName, 'wb') as F:
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
                    Path = urlparse(aUrl)
                    File = ('%s%s%s' % (Path.netloc, Path.path, self.FileTail)).replace('/', '_')
                    self.WriteFile(File, FetchData['data'])
                Res = (FetchData['status'], aUrl)
            else:
                Res = (None, aUrl)
            return Res

    async def Get(self, aUrl: list[str], aMaxConn: int = 5):
        Sem = asyncio.Semaphore(aMaxConn)
        async with aiohttp.ClientSession() as Session:
            print('Main. create tasks', len(aUrl))
            Tasks = [asyncio.create_task(self.FetchSem(Val, Session, Sem, Idx)) for Idx, Val in enumerate(aUrl)]

            print('Main. launch tasks')
            return await asyncio.gather(*Tasks)

    async def LoadFromFile(self, aFile: str, aTail: str = ''):
        with open(aFile, 'r', encoding = 'utf8') as F:
            List = F.read().splitlines()
        List = ['%s%s' % (i, aTail) for i in List]
        Res = await self.Get(List)
        for Idx, Val in enumerate(Res):
            print(Idx, Val)


StartT = time.time()
#Task = TDownload().LoadFromFile('hotline_1.txt', '/sitemap.xml')
#Task = TDownload().LoadFromFile('hotline_1.txt', '/robots.txt')
Task = TDownload('.html').LoadFromFile('hotline_1.txt')
asyncio.run(Task)
print('async duration (s)', round(time.time() - StartT, 2))
