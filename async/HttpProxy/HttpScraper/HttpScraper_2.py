#!/usr/bin/python3 -B


'''
python async site parser example
VladVons@gmail.com
2022.02.17
'''


import os
import asyncio
import aiohttp
import time
import random
from datetime import datetime
from random import randint
from urllib.parse import urlparse
from bs4 import BeautifulSoup


class TLog():
    def __init__(self, aFile):
        self.File = aFile

    def Print(self, aMsg: str):
        print('%s, %s' % (datetime.now().strftime('%d/%m/%Y %H:%M:%S') ,aMsg))

        with open(self.File, 'a+') as FileH:
            FileH.write(aMsg + '\n')


class THeader():
    def __init__(self):
        self.OS = ['Macintosh; Intel Mac OS X 10_15_5', 'Windows NT 10.0; Win64; x64; rv:77', 'Linux; Intel Ubuntu 20.04']
        self.Browser = ['Chrome/83', 'Firefox/77', 'Opera/45']

    def Get(self):
        return {
            'Accept': '*/*',
            'User-Agent': 'Mozilla/5.0 (%s) %s' % (random.choice(self.OS), random.choice(self.Browser))
        }


class THttpScraper():
    def __init__(self, aRoot: str, aMaxTask = 16, aSleep: float = 0.5):
        self.Root = aRoot
        self.MaxTask = aMaxTask
        self.Sleep = aSleep

        self.Timeout = 30

        self.Url = []
        self.UrlCnt = 0
        self.TotalData = 0
        self.IsRun = False

        self.Queue = asyncio.Queue()
        self.Queue.put_nowait(aRoot)

        FileLog = '%s_%s.log' % ('L', urlparse(aRoot).hostname)
        self.Log = TLog(FileLog)

    async def DoGrab(self, aUrl: str, aSoup):
        pass

    @staticmethod
    def IsMimeApp(aUrl: str) -> bool:
        Path = urlparse(aUrl).path
        Ext = os.path.splitext(Path)[1]
        return Ext in ['.zip', '.rar', '.xml', '.pdf', '.jpg', '.jpeg', '.png', '.gif']

    async def _GrabHref(self, aUrl: str, aData: str, aTaskId: int):
        self.TotalData += len(aData)
        self.UrlCnt += 1

        Soup = BeautifulSoup(aData, "lxml")
        for A in Soup.find_all("a"):
            Href = A.get("href", '').strip().rstrip('/')
            if (Href):
                if (Href.startswith('/')):
                    Href = self.Root + Href

                if (Href.startswith(self.Root)) and \
                   (not Href.startswith('#')) and \
                   (not Href in self.Url) and \
                   (not self.IsMimeApp(Href)):
                    self.Url.append(Href)
                    self.Queue.put_nowait(Href)
        await self.DoGrab(aUrl, Soup, aTaskId)

    async def _Worker(self, aSession, aTaskId: int):
        Loops = 0
        TimeStart = time.time()
        self.IsRun = True
        while (self.IsRun):
            Sleep = random.randint(int(self.Sleep / 2), self.Sleep)
            await asyncio.sleep(Sleep)
            if (self.Queue.empty()) and (time.time() - TimeStart > self.Timeout):
                break

            try:
                Url = await asyncio.wait_for(self.Queue.get(), timeout = self.Timeout)
                async with aSession.get(Url) as Response:
                    Data = await Response.read()
                    if (Response.status == 200):
                        await self._GrabHref(Url, Data, aTaskId)
                self.Queue.task_done()
            except (aiohttp.ClientConnectorError, aiohttp.ClientError) as E:
                self.Log.Print('Err:%s %s' % (Url, E))
            except asyncio.TimeoutError:
                self.Log.Print('Err:%s, queue timeout %d' % (self.Root, self.Timeout))
            except Exception as E:
                self.Log.Print('Err:%s %s' % (Url, E))

            Loops += 1
        self.Log.Print('_Worker %d done. Loops %d' % (aTaskId, Loops))

    async def Parse(self):
        Header = THeader()
        async with aiohttp.ClientSession(headers=Header.Get()) as Session:
            Tasks = [asyncio.create_task(self._Worker(Session, i)) for i in range(self.MaxTask)]
            self.Log.Print('URL:%s, Tasks:%d' % (self.Root, len(asyncio.all_tasks())))
            await asyncio.gather(*Tasks)
            self.IsRun = False
            self.Log.Print('Done')


class THttpScraperEx(THttpScraper):
    async def DoGrab(self, aUrl: str, aSoup, aTaskId: int):
        Msg = 'TaskId:%2d, URL found:%2d, URL done:%d, Total:%dM, URL:%s' % (aTaskId, len(self.Url), self.UrlCnt, self.TotalData / 1000000, aUrl)
        self.Log.Print(Msg.strip())


class TMain():
    async def _Scheduler(self, aUrl: str, aSemaph):
        async with aSemaph:
            Scraper = THttpScraperEx(aUrl, 1, 10)
            await Scraper.Parse()

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
    #File = 'hotline_1.txt'
    File = 'hotline_min.txt'
    with open(File, 'r') as F:
        Hosts = F.read().splitlines()

    StartT = time.time()
    Main = TMain()
    Main.Run(Hosts)
    print('duration (s)', round(time.time() - StartT, 2))

Test1()

