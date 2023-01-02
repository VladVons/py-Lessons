#!/usr/bin/env python3

'''
python async example
VladVons@gmail.com
2021.04.09
https://steemit.com/python/@gunhanoral/python-asyncio-port-scanner
'''


import asyncio
import time
import random


class TPortScan():
    #MaxConn = 1015
    MaxConn = 512
    TimeOut = 3
    _CntAll = 0
    _CntOpen = 0

    @staticmethod
    def GetIpRange_1(aCidr: str) -> list:
        import ipaddress
        Res = [str(IP) for IP in ipaddress.IPv4Network(aCidr)]
        return Res

    @staticmethod
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

    async def CheckPortSem(self, aSem, aIp: str, aPort: int) -> tuple:
        #print('CheckPortSem', aIp, aPort)
        async with aSem:
            Opened = await self.CheckPort(aIp, aPort)
            return (aIp, aPort, Opened)

    async def CheckRange(self, aHosts: list, aPorts: list):
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

    async def CheckList(self, aHosts: list):
        print('CheckList. create tasks')
        Sem = asyncio.Semaphore(self.MaxConn)
        Tasks = []
        for Item in aHosts:
            Arr = Item.strip().split(':')
            if (len(Arr) == 2):
                Task = asyncio.create_task(self.CheckPortSem(Sem, Arr[0], Arr[1]))
                Tasks.append(Task)
        Res = await asyncio.gather(*Tasks)
        return Res


def SpeedTest():
    from Conf import Hosts, Ports

    PortScan = TPortScan()
    StartT = time.time()
    Task = PortScan.CheckRange(Hosts, Ports)
    Res = asyncio.run(Task)
    Res = PortScan.FilterOpened(Res, True)
    for Item in Res:
        print(Item)
    print('Opened', len(Res))

    print('async duration (s)', round(time.time() - StartT, 2))

def Scan():
    #Ports = [80]
    Ports = list(range(0, 65535))
    Hosts = ['195.140.244.47']

    PortScan = TPortScan()
    Task = PortScan.CheckRange(Hosts, Ports)
    Res = asyncio.run(Task)
    Res = PortScan.FilterOpened(Res, True)
    for Item in Res:
        print(Item)

def ScanFromFile(aFile: str):
    PortScan = TPortScan()
    with open(aFile, 'r') as F:
        Task = PortScan.CheckList(F.readlines())
        Res = asyncio.run(Task)
        for Host, Port, Opened in Res:
            print('%s:%s %s' % (Host, Port, Opened))

StartAt = time.time()
#SpeedTest()
Scan()
#ScanFromFile('proxies.txt')
print('time sec: ', round(time.time() - StartAt, 2))
