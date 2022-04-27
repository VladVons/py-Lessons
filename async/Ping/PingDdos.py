'''
python async ping example
VladVons@gmail.com
2022.04.28OB
'''


import asyncio
import aioping

class TPingDdos():
    async def Ping(self, aHost: str):
        try:
            Delay = await aioping.ping(aHost)
            return round(Delay * 1000, 2)
        except TimeoutError:
            return -1

    async def PingEver(self, aHost: str, aTaskId: int):
        Cnt = 0
        while (True):
            Delay = await self.Ping(aHost)

            Cnt += 1
            if (Cnt % 100 == 0):
                print('time: %sms, id %s:, cnt: %s' % (Delay, aTaskId, Cnt))

            await asyncio.sleep(0.001)

    async def Run(self, aHost: str, aCnt: int):
        Tasks = [self.PingEver(aHost, i) for i in range(aCnt)]
        print('gathering %s tasks ...' % (aCnt))
        await asyncio.gather(*Tasks)


Task = TPingDdos().Run('192.168.12.214', 100)
asyncio.run(Task)
