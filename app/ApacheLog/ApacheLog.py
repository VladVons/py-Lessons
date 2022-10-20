'''
apache web server log analyzer
2022.04.08

sudo apt install geoip-bin
geoiplookup 8.8.8.8
'''


import os
import re
import socket
import json
import subprocess


class TApache():
    def __init__(self):
        self.Data = {}

    def GetCountryByIp(self, aIp: str) -> str:
        Data = subprocess.run(['geoiplookup', aIp], stdout=subprocess.PIPE, text=True)
        return Data.stdout.split(':')[-1].strip()

    def GetHostByIp(self, aIp: str) -> str:
        try:
            Res = socket.gethostbyaddr(aIp)[0]
        except socket.error:
            Res = ''
        return Res

    def Save(self, aFile):
        with open(aFile, 'w') as F:
            json.dump(self.Data, F)

    def Load(self, aFile):
        with open(aFile, 'r') as F:
            self.Data = json.load(F)

    def Sort(self, aIdx: int):
        return sorted(self.Data.items(), key = lambda k: k[1][aIdx], reverse=False)

    def Count(self, aIdx: int) -> list:
        Res = {}
        for _, Val in self.Data.items():
            Key = Val[aIdx]
            if (not Key):
                Key = 'unknown'

            Res[Key] = Res.get(Key, 0) + Val[0]
        return sorted(Res.items(), key = lambda k: k[1], reverse=False)

    def LoadLog(self, aFile: str):
        reRec = re.compile('(\d+\.\d+\.\d+\.\d+).*(\[.*\])(.*)')
        reUrl = re.compile('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+')
        reHost = re.compile('(\d+\-\d+\-\d+\-\d+)\.(.*)')

        with open(aFile, 'r') as F:
            for Line in F.readlines():
                rLine = reRec.findall(Line)[0]
                Ip = rLine[0]
                Val = self.Data.get(Ip)
                if (Val):
                    Val[0] = Val[0] + 1
                    self.Data[Ip] = Val
                else:
                    Host = self.GetHostByIp(Ip)
                    if (Host):
                        HostBase = reHost.findall(Host)
                        if (HostBase):
                            HostBase = HostBase[0][1]
                        else:
                            Arr = Host.split('.')
                            HostBase = '.'.join(Arr[-2:])
                    else:
                        HostBase = Ip

                    rBot = reUrl.findall(rLine[2])
                    if (rBot):
                        Bot = rBot[0]
                    else:
                        Bot = ''

                    Rec = [1, Host, HostBase, Bot, self.GetCountryByIp(Ip)]
                    self.Data[Ip] = Rec
                    print('%4s, %15s %s' % (len(self.Data), Ip, Rec))

    def LoadLogs(self, aFile: list):
        for File in aFile:
            print()
            print(File)
            self.LoadLog(File)

    def LoadLogMask(self, aVal: str):
        Arr = [x for x in os.listdir('.') if (aVal in x)]
        self.LoadLogs(sorted(Arr))

    def Info_Ip(self):
        Cnt = 0
        Arr = self.Sort(0)
        for Ip, Data in Arr:
            Cnt += Data[0]
            print('%15s %s' % (Ip, Data))
        print('All %s, Ip %s, %s' % (Cnt, len(self.Data), len(Arr)))

    def Info_Host(self, aIdx: int = 2):
        Cnt = 0
        Arr = self.Count(aIdx)
        for Key, Val in Arr:
            Cnt += Val
            print('%3s %s' % (Val, Key))
        print('All %s, Ip %s, %s' % (Cnt, len(self.Data), len(Arr)))


def Main():
    Apache = TApache()
    #Apache.LoadLogMask('.log')
    #Apache.LoadLog('access.log')
    #Apache.Save('access.log.json')

    Apache.Load('access.log.json')
    print()
    Apache.Info_Ip()
    for i in [2,4]:
        print()
        Apache.Info_Host(i)

if (__name__ == '__main__'):
    os.system('clear')
    Main()


