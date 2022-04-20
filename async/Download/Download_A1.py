#!/usr/bin/env python3

'''
python async example
VladVons@gmail.com
2021.03.04
'''

import time
import asyncio
import aiohttp
import aiofile


class TDownload():
    def WriteFile(self, aName: str, aData):
        print('WriteFile', aName)
        with open(aName, 'wb') as FileH:
            FileH.write(aData)

    async def WriteFileA(self, aName: str, aData):
        print('WriteFileA', aName)
        async with aiofile.async_open(aName, 'wb') as FileH:
            await FileH.write(aData)

    async def Fetch(self, aUrl: str, aSession, aCnt):
        async with aSession.get(aUrl) as Response:
            print('Fetch', aCnt)
            Data = await Response.read()

            self.WriteFile('File_A_%03d.jpeg' % aCnt, Data)
            #await self.WriteFileA('File_A_%03d.jpeg' % aCnt, Data)

    async def Main(self, aUrl: str, aCnt: int):
        async with aiohttp.ClientSession() as Session:
            print('Main. create tasks', aCnt)
            Tasks = []
            for i in range(aCnt):
                Task = asyncio.create_task(self.Fetch(aUrl, Session, i + 1))
                Tasks.append(Task)

            print('Main. launch tasks', aCnt)
            await asyncio.gather(*Tasks)

StartT = time.time()
Task = TDownload().Main('https://loremflickr.com/800/600/girl', 100)
asyncio.run(Task)
print('async duration (s)', round(time.time() - StartT, 2))
