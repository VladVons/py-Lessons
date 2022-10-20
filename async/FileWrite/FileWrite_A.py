#!/usr/bin/env python3

'''
python async example
VladVons@gmail.com
2022.01.07
'''

import time
import asyncio
import aiofile
import os


class TFileWriteA():
    async def WriteFileA(self, aName: str, aData):
        print('WriteFileA', aName)
        async with aiofile.async_open(aName, 'w') as FileH:
            await FileH.write(aData)

    async def Main(self, aDir: str, aCnt: int):
        print('Main. create tasks', aCnt)
        os.makedirs(aDir, exist_ok=True)
        Tasks = []
        for i in range(aCnt):
            File = '%s/file_%04d.txt' % (aDir, i)
            Task = asyncio.create_task(self.WriteFileA(File, (File + '\n') * 10000))
            Tasks.append(Task)

        print('Main. launch tasks')
        await asyncio.gather(*Tasks)
        print('Main. done')


# 2x faster on slow samba connection
StartT = time.time()
Task = TFileWriteA().Main('/mnt/smb/tr41/filesA', 100)
asyncio.run(Task)
print('async duration (s)', round(time.time() - StartT, 2))
