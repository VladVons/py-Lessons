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

        self.Cnt = 0
        self.Url = ''

    def WriteFile(self, aName: str, aData: bytes):
        Path = self.Dir + '/' + aName
        with open(Path, 'wb') as F:
            F.write(aData)

    async def Fetch(self, aSession):
        async with aSession.get(self.Url) as Response:
            try:
                Data = await Response.read()
                self.WriteFile('File_A_%03d.jpeg' % self.Cnt, Data)
            except Exception as E:
                print('Err', E)
            else:
                self.Cnt -= 1
                if (self.Cnt % 10 == 0):
                    print(f'remains {self.Cnt}')

    async def _Worker(self, aIdx: int):
        print(f'Starting worker {aIdx}')
        async with aiohttp.ClientSession() as Session:
            while (self.Cnt >= 0):
                await self.Fetch(Session)
    
    async def Main(self, aUrl: str, aCnt: int, aMaxConn: int):
        self.Cnt = aCnt
        self.Url = aUrl
        Tasks = [asyncio.create_task(self._Worker(i + 1)) for i in range(aMaxConn)]
        await asyncio.gather(*Tasks)


StartT = time.time()
Url = 'https://loremflickr.com/800/600/girl'
#Url = 'http://localhost/phpHello.php'
#Url = 'http://localhost:8080'
Task = TDownload().Main(Url, 100, 5)
asyncio.run(Task)
print('async duration (s) %0.2f' % (time.time() - StartT))
