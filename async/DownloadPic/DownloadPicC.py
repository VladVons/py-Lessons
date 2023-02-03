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

    async def Fetch(self, aUrl: str, aIdx: int):
        async with aiohttp.ClientSession() as Session:
            async with Session.get(aUrl) as Response:
                try:
                    Data = await Response.read()
                    self.WriteFile('File_A_%03d.jpeg' % aIdx, Data)
                except Exception as E:
                    print('Err', E)
                else:
                    self.Cnt -= 1
                    if (self.Cnt % 10 == 0):
                        print('remains', self.Cnt)

    async def FetchSem(self, aUrl: str, aSem, aIdx: int):
        async with aSem:
             await self.Fetch(aUrl, aIdx)

    async def Main(self, aUrl: str, aCnt: int, aMaxConn: int = 5):
        print('Main. create tasks', aCnt)
        self.Cnt = aCnt
        Sem = asyncio.Semaphore(aMaxConn)
        Tasks = [asyncio.create_task(self.FetchSem(aUrl, Sem, i + 1)) for i in range(aCnt)]
        print('Main. launch tasks', aCnt)
        await asyncio.gather(*Tasks)


StartT = time.time()
Url = 'https://loremflickr.com/800/600/girl'
#Url = 'http://localhost/phpHello.php'
#Url = 'http://localhost:8080'
Task = TDownload().Main(Url, 100, 5)
asyncio.run(Task)
print('async duration (s) %0.2f' % (time.time() - StartT))
