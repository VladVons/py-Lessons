#!/usr/bin/env python3

'''
python async example
VladVons@gmail.com
2021.04.09
'''


import asyncio
import time
import random


def GetIpRange(aCidr: str) -> list:
    import socket
    import struct

    Ip, Cidr = aCidr.split('/')
    Cidr = int(Cidr)
    Bits = 32 - Cidr
    if (Bits == 0):
        return [Ip]

    i = struct.unpack('>I', socket.inet_aton(Ip))[0]
    Start = (i >> Bits) << Bits
    End = Start | ((1 << Bits) - 1)
    Res = []
    for i in range(Start, End):
        Addr = socket.inet_ntoa(struct.pack('>I', i))
        Res.append(Addr)
    #Uniq = set(Res)
    return Res


class TPortScan():
    #MaxConn = 1015
    MaxConn = 512
    TimeOut = 3

    _CntAll = 0
    _CntOpen = 0

    @staticmethod
    def FilterOpened(aList: list, aValue: bool) -> list:
        return [Item for Item in aList if Item[2] == aValue]

    async def CheckPort(self, aIp: str, aPort: int) -> bool:
        #print('CheckPort', aIp, aPort)
        Conn = asyncio.open_connection(aIp, aPort)
        try:
            Reader, Writer = await asyncio.wait_for(Conn, timeout=self.TimeOut)
            self._CntOpen += 1
            print(f'opened {aIp}:{aPort}')
            return True
        except:
            return False
        finally:
            self._CntAll += 1
            if (self._CntAll > 0) and (self._CntAll % 1000 == 0):
                print('CntAll', self._CntAll, 'CntOpen', self._CntOpen)

            if ('Writer' in locals()):
                Writer.close()

    async def CheckPortSem(self, aSem: asyncio.Semaphore, aIp: str, aPort: int) -> tuple:
        #print('CheckPortSem', aIp, aPort)
        async with aSem:
            Opened = await self.CheckPort(aIp, aPort)
            return (aIp, aPort, Opened)

    async def CheckRange(self, aHosts: list[str], aPorts: list[int]):
        print('CheckRange. create tasks')
        Sem = asyncio.Semaphore(self.MaxConn)
        Tasks = []
        for Host in aHosts:
            for Port in aPorts:
                Task = asyncio.create_task(self.CheckPortSem(Sem, Host, Port))
                Tasks.append(Task)

        print('CheckRange. launch tasks', len(Tasks))
        Res = await asyncio.gather(*Tasks)
        return Res


def Scan(aHosts: list[str], aPorts: list[int]):
    PortScan = TPortScan()
    Task = PortScan.CheckRange(aHosts, aPorts)
    Res = asyncio.run(Task)
    Res = PortScan.FilterOpened(Res, True)
    for Item in Res:
        print(Item)


StartAt = time.time()
#Hosts = GetIpRange('192.168.11.0/24')
Hosts = ['94.247.62.24']
#Ports = [22, 53, 80, 139, 443, 3389, 8006, 8080]
Ports = list(range(10000, 11000))

Scan(Hosts, Ports)
print('time: %0.2f sec' % (round(time.time() - StartAt, 2)))
