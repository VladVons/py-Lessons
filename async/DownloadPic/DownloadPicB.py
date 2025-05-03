'''
python async example
VladVons@gmail.com
2021.03.04
'''


import os
import time
import random
import asyncio
import ssl
import aiohttp


class TDownload():
    def __init__(self):
        _, Dir = os.path.split(__file__)
        self.Dir = Dir.split('.')[0]
        os.makedirs(self.Dir, exist_ok = True)
        self.Cnt = 0
        self.TotalRead = 0
        self.TimeLap = time.time()

    def WriteFile(self, aName: str, aData: bytes):
        Path = self.Dir + '/' + aName
        with open(Path, 'wb') as F:
            F.write(aData)

    async def Fetch(self, aUrl: str, aSession, aIdx: int):
        SSL = ssl.create_default_context()
        SSL.options = 0
        async with aSession.get(aUrl, ssl=SSL) as Response:
            try:
                Data = await Response.read()
            except Exception as E:
                print('Err', E)
            else:
                if (Response.status == 200):
                    self.WriteFile('File_A_%03d.dat' % aIdx, Data)

                    self.TotalRead += len(Data)
                    self.Cnt -= 1
                    if (self.Cnt % 10 == 0):
                        print('remains %d' % self.Cnt, 'read %d Kb' % (self.TotalRead / 1000), 'time %0.2f sec' % (time.time() - self.TimeLap))
                        self.TimeLap = time.time()
                else:
                    print('Err status', Response.status)

    async def FetchSem(self, aUrl: str, aSession, aSem, aIdx: int):
        async with aSem:
            await self.Fetch(aUrl, aSession, aIdx)

    async def Main(self, aUrl: list[str], aCnt: int, aMaxConn: int = 5):
        self.Cnt = aCnt
        Sem = asyncio.Semaphore(aMaxConn)
        async with aiohttp.ClientSession() as Session:
            print('Main. create tasks', aCnt)
            Tasks = []
            for i in range(aCnt):
                Url = random.choice(aUrl)
                Task = asyncio.create_task(self.FetchSem(Url, Session, Sem, i + 1))
                Tasks.append(Task)
            print('Main. launch tasks', aCnt)
            await asyncio.gather(*Tasks)


def Main():
    StartT = time.time()
    #Url = ['https://loremflickr.com/800/600/girl']
    #Url = ['https://kaluna.te.ua/search/?query=240']
    #Url = ['https://used.1x1.com.ua/?route=product0/search&q=dell']
    Url = ['https://onefacecosmetics.com.ua/oblichchia/', 'https://onefacecosmetics.com.ua/tilo/', 'https://onefacecosmetics.com.ua/catalog/', 'https://onefacecosmetics.com.ua/search/?query=%D0%BA%D1%80%D0%B5%D0%BC']
    Task = TDownload().Main(Url, 1000, 50)
    asyncio.run(Task)
    print('async duration (s) %0.2f' % (time.time() - StartT))

Main()
