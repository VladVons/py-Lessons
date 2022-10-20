#!/usr/bin/python3 -B

import os
import time
import asyncio
import aiohttp
from urllib.parse import urlparse
from bs4 import BeautifulSoup


def Log(aFile: str, aData: str):
        print(aData)
        with open(aFile, 'a+') as FileH:
            FileH.write(aData + '\n')


class TScraper():
    def __init__(self, aUrl: str, aMaxConn = 16):
        self.Root = aUrl
        self.Url = []
        self.UrlErr = []
        self.MaxConn = aMaxConn
        self.TotalData = 0
        self.UrlCnt = 0

        #self.Queue = asyncio.Queue()
        #self.Lock = asyncio.Lock()

        Dir = 'log'
        if (not os.path.isdir(Dir)): 
            os.makedirs(Dir)
        self.FileLog = Dir + '/' + urlparse(aUrl).hostname + '.log'

    def WriteDB(self, aData: str):
        Log(self.FileLog, aData)

    def _AddItem(self, aList: list, aUrl: str):
        if (not aUrl in aList):
            aList.append(aUrl)

    def _GetHeader(self):
        Res = {
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"
        }
        return Res

    async def _GrabHref(self, aUrl: str, aData: str, aDepth: int):
        self.UrlCnt += 1
        self.TotalData += len(aData)

        Hrefs = []
        Soup = BeautifulSoup(aData, "lxml")
        for A in Soup.find_all("a"):
            Href = A.get("href", '').strip().rstrip('/')
            if (Href):
                #print(aUrl, Href)

                Path = urlparse(Href).path
                Ext = os.path.splitext(Path)[1]

                if (Href.startswith('/')):
                    Href = self.Root + Href

                if (Href.startswith(self.Root)) and \
                   (not Href.startswith('#')) and \
                   (not Href in Hrefs) and \
                   (not Ext in ['.zip', '.jpg', '.png']):
                    self._AddItem(Hrefs, Href)

        #self.WriteDB(aUrl)
        await self._ParseRecurs(Hrefs, aDepth + 1)

    async def _Fetch(self, aUrl: str, aSession, aSemaph, aDepth: int):
        async with aSemaph:
            try:
                async with aSession.get(aUrl) as Response:
                    Data = await Response.read()
                    if (Data):
                        await self._GrabHref(aUrl, Data, aDepth)
            except (aiohttp.ClientConnectorError, aiohttp.ClientError) as E:
                self.Url.remove(aUrl)
                self._AddItem(self.UrlErr, aUrl)
                Log(self.FileLog, '_Fetch_A %s %s' % (E, aUrl))
            #except Exception as E:
            #    Log(self.FileLog, '_Fetch_B %s %s' % (E, aUrl))

    async def _ParseRecurs(self, aUrl: list, aDepth: int):
            #async with self.Lock:
            #print('_ParseRecurs')
            async with aiohttp.ClientSession(headers=self._GetHeader()) as Session:
                Semaph = asyncio.Semaphore(self.MaxConn)

                Tasks = []
                for Url in aUrl:
                    if (not Url in self.Url):
                        self.Url.append(Url)
                        Msg = 'Depth:%d, Url found:%d, Url done:%d, Total:%dM, Tasks:%d, URL:%s' % (aDepth, len(self.Url), self.UrlCnt, self.TotalData / 1000000, len(asyncio.all_tasks()), Url)
                        Log(self.FileLog, Msg.strip())

                        Task = asyncio.create_task(self._Fetch(Url, Session, Semaph, aDepth))
                        Tasks.append(Task)

                if (Tasks):
                    await asyncio.gather(*Tasks)

class TMain():
    def __init__(self):
        pass

    async def _Scheduler(self, aUrl: str, aSemaph):
        async with aSemaph:
            Scraper = TScraper(aUrl, 16)
            await Scraper._ParseRecurs([aUrl], 0)
            Msg = 'url: %s, count: %d, size: %d' % (aUrl, len(Scraper.Url), Scraper.TotalData)
            Log(Scraper.FileLog, Msg)

    async def CreateTasks(self, aUrl: list, aMaxTasks: int):
        Semaph = asyncio.Semaphore(aMaxTasks)

        Tasks = []
        for Url in aUrl:
            if (not Url.startswith('-')):
                Task = asyncio.create_task(self._Scheduler(Url, Semaph))
                Tasks.append(Task)
        await asyncio.gather(*Tasks)

    def Run(self, aUrl: list, aMaxTasks: int = -1):
        if (aMaxTasks == -1):
            aMaxTasks = len(aUrl)

        Task = self.CreateTasks(aUrl, aMaxTasks)
        asyncio.run(Task)


def Test1():
    #Hosts = ['https://kaluna.te.ua']
    #Hosts = ['http://bereka-radio.com.ua']
    Hosts = ['https://largo.com.ua']
    #Hosts = ['https://www.neotec.ua', 'https://largo.com.ua', 'http://oster.com.ua', 'http://bereka-radio.com.ua', 'https://kaluna.te.ua']
    StartT = time.time()
    Main = TMain()
    Main.Run(Hosts)
    print('duration (s)', round(time.time() - StartT, 2))

Test1()
