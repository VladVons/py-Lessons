#!/usr/bin/env python3

'''
python async example
VladVons@gmail.com
2021.03.01
'''


import asyncio
from datetime import datetime


async def ProveA():
    Loops = 0
    while True:
        Loops += 1
        print('ProveA 2s', Loops)
        await asyncio.sleep(2)


async def ProveB():
    Loops = 0
    while True:
        Loops += 1
        print('ProveB 3s', Loops)
        await asyncio.sleep(3)


class THttpSrv():
    Loops = 0

    async def ReadHead(self, aReader) -> list:
        R = []
        while True:
            Data = await aReader.readline()
            if (Data == b'\r\n') or (Data is None):
                break

            Data = Data.decode('utf-8').strip()
            R.append(Data)
        return R

    def Responce(self, aData):
        R = [
            'HTTP/1.1 200 OK',
            'Content-Type: text/html',
            'Server: HttpMicro',
            '\r\n',
            aData,
            '\r\n'
            ]
        return '\r\n'.join(R)

    async def CallBack(self, aReader, aWriter):
        self.Loops += 1

        Head = await self.ReadHead(aReader)
        #print(*Head, sep = "\n")
        print('Http head:', Head[0], self.Loops)

        Head.insert(0, '')
        Head.insert(0, 'Http head:')
        Head.insert(0, 'python async %d at %s' % (self.Loops, datetime.now()))
        Data = '<BR>\r\n'.join(Head)

        aWriter.write(self.Responce(Data).encode())
        await aWriter.drain()
        aWriter.close()

    async def Run(self, aPort = 80):
        print('Listen 0.0.0.0:',  aPort)
        await asyncio.start_server(self.CallBack, '0.0.0.0', aPort)


async def Main():
    Task1 = asyncio.create_task(THttpSrv().Run(8080))
    Task2 = asyncio.create_task(THttpSrv().Run(8081))
    Task3 = asyncio.create_task(ProveA())
    Task4 = asyncio.create_task(ProveB())
    await asyncio.gather(Task1, Task2, Task3, Task4)


asyncio.run(Main())
