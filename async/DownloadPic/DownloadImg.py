#!/usr/bin/env python3

'''
python async example
VladVons@gmail.com
2024.03.21
'''


import os
import time
import asyncio
from urllib.parse import urlparse
from aiohttp import ClientSession
from bs4 import BeautifulSoup


class TDownload():
    def __init__(self):
        _, Dir = os.path.split(__file__)
        self.Dir = Dir.split('.')[0]
        os.makedirs(self.Dir, exist_ok = True)

    @staticmethod
    def UrlToFile(aUrl: str) -> str:
        for x in ['/', '?', ':', '=']:
            aUrl = aUrl.replace(x, '_')
        return aUrl

    def WriteFile(self, aName: str, aData):
        Path = self.Dir + '/' + aName
        #print('WriteFile', Path)
        with open(Path, 'wb') as FileH:
            FileH.write(aData)

    async def Fetch(self, aUrl: str, aSession: ClientSession, aSem):
        async with aSem:
            try:
                print('Fetch', aUrl)
                async with aSession.get(aUrl) as Response:
                    Data = await Response.read()
                    Url = self.UrlToFile(aUrl)
                    self.WriteFile(Url, Data)
            except Exception as E:
                print('Fetch err', aUrl, E)

    async def GetImg(self, aUrl: str, aSession: ClientSession):
        UrlObj = urlparse(aUrl)
        async with aSession.get(aUrl) as Response:
            Data = await Response.read()
            BS = BeautifulSoup(Data, 'html.parser')
            Hrefs = []
            for x in BS.find_all('img'):
                Href = x.get('src')
                if (Href):
                    if (not Href.startswith('http')):
                        Href = f'{UrlObj.scheme}://{UrlObj.netloc}{Href}'
                    Hrefs.append(Href)
            Uniq = set(Hrefs)
            return Uniq

    async def Main(self, aUrl: str, aMaxConn: int = 10):
        async with ClientSession() as Session:
            Sem = asyncio.Semaphore(aMaxConn)
            Tasks = []
            Hrefs = await self.GetImg(aUrl, Session)
            for xHref in Hrefs:
                Task = asyncio.create_task(self.Fetch(xHref, Session, Sem))
                Tasks.append(Task)
            print('Main. run tasks')
            await asyncio.gather(*Tasks)

def Main():
    Url = 'http://oster.com.ua'
    Url = 'https://yahoo.com'
    StartT = time.time()
    Task = TDownload().Main(Url)
    asyncio.run(Task)
    print('async duration (s)', round(time.time() - StartT, 2))

Main()
