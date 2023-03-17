'''
python async example
VladVons@gmail.com
2023.02.03
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

        self.Queue = asyncio.Queue()

    def WriteFile(self, aName: str, aData: bytes):
        Path = self.Dir + '/' + aName
        with open(Path, 'wb') as F:
            F.write(aData)

    async def Fetch(self, aUrl: str, aSession, aCnt: int):
        async with aSession.get(aUrl) as Response:
            try:
                Data = await Response.read()
                self.WriteFile('File_A_%03d.jpeg' % aCnt, Data)
            except Exception as E:
                print('Err', E)

    async def _Worker(self, aIdx: int):
        #print(f'Starting worker {aIdx}')
        async with aiohttp.ClientSession() as Session:
            while (not self.Queue.empty()):
                Size = self.Queue.qsize()
                if (Size % 10 == 0):
                    print(f'remains {Size}')

                UrlQ = await self.Queue.get()
                await self.Fetch(UrlQ, Session, Size)

    async def Main(self, aUrl: str, aCnt: int, aMaxConn: int):
        for i in range(aCnt):
            self.Queue.put_nowait(aUrl)

        Tasks = [asyncio.create_task(self._Worker(i + 1)) for i in range(aMaxConn)]
        await asyncio.gather(*Tasks)

StartT = time.time()
Url = 'http://shop3.oster.com.ua:8080/api/misc/exit'
Url = 'http://localhost:8080/api/misc/exit'
#Url = 'https://loremflickr.com/800/600/girl'
#Url = 'http://localhost/phpHello.php'
#Url = 'http://localhost:8080'
Task = TDownload().Main(Url, 100000, 100)
asyncio.run(Task)
print('async duration (s) %0.2f' % (time.time() - StartT))

