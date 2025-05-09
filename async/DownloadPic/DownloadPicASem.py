#!/usr/bin/env python3

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

    def WriteFile(self, aName: str, aData):
        Path = self.Dir + '/' + aName
        print('WriteFile', Path)
        with open(Path, 'wb') as FileH:
            FileH.write(aData)

    async def Fetch(self, aUrl: str, aSession, aCnt):
        async with aSession.get(aUrl) as Response:
            print('Fetch', aCnt)
            Data = await Response.read()

            self.WriteFile('File_A_%03d.jpeg' % aCnt, Data)
            #await self.WriteFileA('File_A_%03d.jpeg' % aCnt, Data)

    async def FetchSem(self, aUrl: str, aSession, aSem, aIdx: int):
        async with aSem:
             await self.Fetch(aUrl, aSession, aIdx)

    async def Main(self, aUrl: str, aCnt: int, aMaxConn: int):
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
Task = TDownload().Main('https://loremflickr.com/640/480', 50, 10)
asyncio.run(Task)
print('async duration (s)', round(time.time() - StartT, 2))
