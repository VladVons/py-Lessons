import os
import re
import socket
import json


class TApache():
    def __init__(self):
        self.Data = {}

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
        Me = 'http://oster.com.ua'
        reHost = re.compile('(\d+\-\d+\-\d+\-\d+)\.(.*)')
        reRec = re.compile('(\d+\.\d+\.\d+\.\d+).*(\[.*\])(.*)')
        reUrl = re.compile('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+')

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
                        HostBase = ''

                    rBot = reUrl.findall(rLine[2])
                    if (rBot):
                        Bot = rBot[0]
                    else:
                        Bot = ''

                    Rec = [1, Host, HostBase, Bot]
                    self.Data[Ip] = Rec
                    print(len(self.Data), Ip, Rec)

    def LoadLogs(self, aFile: list):
        for File in aFile:
            self.LoadFile(File)


    def Info_Ip(self):
        Cnt = 0
        Arr = self.Sort(0)
        for Ip, Data in Arr:
            Cnt += Data[0]
            print(Ip, Data)
        print('All %s, Ip %s, %s' % (Cnt, len(self.Data), len(Arr)))

    def Info_Host(self, aIdx: int = 2):
        Cnt = 0
        Arr = Apache.Count(aIdx)
        for Key, Val in Arr:
            Cnt += Val
            print(Val, Key)
        print('All %s, Ip %s, %s' % (Cnt, len(self.Data), len(Arr)))



#os.system('clear')

File = '3w_oster.com.ua_access.log.8'
Apache = TApache()
#Apache.LoadLog(File)
#Apache.Save(File + '.json')
Apache.Load(File + '.json')
#print()
#Apache.Info_Ip()
print()
Apache.Info_Host(2)
#print()
#Apache.Info_Host(3)

