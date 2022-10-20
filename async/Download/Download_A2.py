#!/usr/bin/env python3

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
            os.mkdir(aDirOut)

    def WriteFile(self, aName: str, aData):
        print('WriteFile', aName, len(aData))
        with open(self.DirOut + '/' + aName, 'wb') as F:
            F.write(aData)

    async def Fetch(self, aUrl: str, aSession, aSem, aIdx: int) -> tuple:
        try:
            async with aSem:
                async with aSession.get(aUrl) as Response:
                    print('Fetch', aIdx, aUrl)
                    Data = await Response.read()
                    if (Response.status == 200):
                        Path = urlparse(aUrl)
                        File = ('%s%s%s' % (Path.netloc, Path.path, self.FileTail)).replace('/', '_')
                        self.WriteFile(File, Data)
                    else:
                        print('Err', Response.status, aUrl)
                return (Response.status, aUrl)
        except Exception as E:
            print('Err:', E, aUrl)

    async def Get(self, aUrl: list, aMaxConn: int = 5):
        Sem = asyncio.Semaphore(aMaxConn)
        async with aiohttp.ClientSession() as Session:
            print('Main. create tasks', len(aUrl))
            Tasks = [asyncio.create_task(self.Fetch(Val, Session, Sem, Idx)) for Idx, Val in enumerate(aUrl)]

            print('Main. launch tasks')
            return await asyncio.gather(*Tasks)

    async def LoadFromFile(self, aFile: str, aTail: str = ''):
        with open(aFile, 'r') as F:
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
