#!/usr/bin/python3 -B

'''
python async tor proxy
VladVons@gmail.com
2022.02.23
'''

import time
import random
import asyncio
import aiohttp
from aiohttp_socks import ProxyConnector
from datetime import datetime


class TBase():
    def __init__(self):
        self.TaskCnt = 5
        self.PrevIP = []
        self.Url = 'http://icanhazip.com'
        self.Proxy = 'socks5://localhost:9050'
        self.Headers = {
            'Accept': '*/*',
            'User-Agent': 'Mozilla/5.5 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0'
        }

    def WriteFile(self, aName: str, aData):
        print(aData)
        with open(aName, 'a+') as FileH:
            FileH.write(aData + '\n')

    def GetConnector(self, aProxy: bool):
        if (aProxy):
            return ProxyConnector.from_url(self.Proxy)

    def GetIP(self, aData):
        return aData.decode().strip()

    async def Fetch(self, aSession, aTaskId: int):
        Name = self.__class__.__name__

        async with aSession.get(self.Url) as Response:
            Data = await Response.read()
            IP = self.GetIP(Data)
            print(Name, aTaskId, IP)
            if (not IP in self.PrevIP):
                self.PrevIP.append(IP)
                Info = '%s, %s, TaskId:%2d, Status:%d, IP:%15s' % (datetime.now().strftime('%H:%M:%S'), Name, aTaskId, Response.status, IP)
                self.WriteFile(Name + '.log', Info)
        await asyncio.sleep(10)

 
class TTorProxy_1(TBase):
    async def _Worker(self, aSession, aTaskId: int):
        while (True):
            try:
                await self.Fetch(aSession, aTaskId)
            except Exception as E:
                print('Err_1', E, self.Url)
    
    async def Run(self):
        async with aiohttp.ClientSession(headers=self.Headers, connector=self.GetConnector(True)) as Session:
            Tasks = [asyncio.create_task(self._Worker(Session, i)) for i in range(self.TaskCnt)]
            await asyncio.gather(*Tasks)


class TTorProxy_2(TBase):
    async def _Worker(self, aTaskId: int):
        try:
            async with aiohttp.ClientSession(headers=self.Headers, connector=self.GetConnector(True)) as Session:
                while (True):
                    await self.Fetch(Session, aTaskId)
        except Exception as E:
            print('Err_2', E, self.Url)

    async def Run(self):
            Tasks = [asyncio.create_task(self._Worker(i)) for i in range(self.TaskCnt)]
            await asyncio.gather(*Tasks)


class TTorProxy_3(TBase):
    async def _Worker(self, aTaskId: int):
        while (True):
            try:
                async with aiohttp.ClientSession(headers=self.Headers, connector=self.GetConnector(True)) as Session:
                    await self.Fetch(Session, aTaskId)
            except Exception as E:
                print('Err_3', E, self.Url)

    async def Run(self):
            Tasks = [asyncio.create_task(self._Worker(i)) for i in range(self.TaskCnt)]
            await asyncio.gather(*Tasks)


async def Main():
    Tasks = [asyncio.create_task(Obj) for Obj in [TTorProxy_1().Run(), TTorProxy_2().Run(), TTorProxy_3().Run()]]
    await asyncio.gather(*Tasks)


asyncio.run(Main())
