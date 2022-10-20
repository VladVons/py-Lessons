#!/usr/bin/python3 -B

'''
python async tor proxy example
VladVons@gmail.com
2022.02.23

sudo apt-get install tor
pip3 install asyncio aiohttp aiohttp-socks

https://gist.github.com/DusanMadar/8d11026b7ce0bce6a67f7dd87b999f6b
'''

import time
import random
import asyncio
import aiohttp
from aiohttp_socks import ProxyConnector

#print(parse_proxy_url('socks5://localhost:9050'))


class TTorProxy():
    def __init__(self):
        self.Url = 'http://icanhazip.com'
        #self.Url = 'https://ipinfo.io/json'

        self.Proxy = ['socks5://localhost:9050']
        self.Headers = {
            'Accept': '*/*',
            'User-Agent': 'Mozilla/5.5 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0'
        }

    def GetConnector(self, aProxy: bool):
        if (aProxy):
            Proxy = random.choice(self.Proxy)
            return ProxyConnector.from_url(Proxy)

    async def _Worker(self, aSession, aTaskId: int):
        try:
            async with aSession.get(self.Url) as Response:
                Data = await Response.read()
                print('TaskId: %d, Status: %d, Data: %s' % (aTaskId, Response.status, Data.decode().strip()))
        except (aiohttp.ClientConnectorError, aiohttp.ClientError) as E:
            print('Exception', E, self.Url)

    async def Run(self, aProxy: bool = True, aTaskCnt: int = 10):
        async with aiohttp.ClientSession(headers=self.Headers, connector=self.GetConnector(aProxy)) as Session:
            Tasks = [asyncio.create_task(self._Worker(Session, i)) for i in range(aTaskCnt)]
            await asyncio.gather(*Tasks)


def Main(aTaskCnt: int):
    Duration = []
    for IsProxy in [False, True]:
        TimeStart = time.time()
        asyncio.run(TTorProxy().Run(IsProxy, aTaskCnt))
        TimeDur = round(time.time() - TimeStart, 3)
        Duration.append(TimeDur)

        print('Tasks %d, Proxy %s, Time: %.3f' % (aTaskCnt, IsProxy, TimeDur))
        print()
    print('Duration', Duration)

Main(5)
