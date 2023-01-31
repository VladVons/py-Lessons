'''
python async example
VladVons@gmail.com
2021.03.04
'''


import os
import time
import asyncio
import aiohttp


class TDownload():
    def __init__(self):
        _, Dir = os.path.split(__file__)
        self.Dir = Dir.split('.')[0]
        os.makedirs(self.Dir, exist_ok = True)
        self.Cnt = 0

    def WriteFile(self, aName: str, aData: bytes):
        Path = self.Dir + '/' + aName
        with open(Path, 'wb') as F:
            F.write(aData)

        self.Cnt -= 1
        if (self.Cnt % 10 == 0):
            print('remains', self.Cnt)

    async def Fetch(self, aUrl: str, aSession, aCnt):
        async with aSession.get(aUrl) as Response:
            try:
                Data = await Response.read()
                self.WriteFile('File_A_%03d.jpeg' % aCnt, Data)
            except Exception as E:
                print('Err', E)

    async def FetchSem(self, aUrl: str, aSession, aSem, aIdx: int):
        async with aSem:
             await self.Fetch(aUrl, aSession, aIdx)

    async def Main(self, aUrl: str, aCnt: int, aMaxConn: int = 5):
        self.Cnt = aCnt
        Sem = asyncio.Semaphore(aMaxConn)
        async with aiohttp.ClientSession() as Session:
            print('Main. create tasks', aCnt)
            Tasks = []
            for i in range(aCnt):
                Task = asyncio.create_task(self.FetchSem(aUrl, Session, Sem, i + 1))
                Tasks.append(Task)
            print('Main. launch tasks', aCnt)
            await asyncio.gather(*Tasks)


StartT = time.time()
Task = TDownload().Main('https://loremflickr.com/800/600/girl', 100, 5)
asyncio.run(Task)
print('async duration (s) %0.2f' % (time.time() - StartT))
