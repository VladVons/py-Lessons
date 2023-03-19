'''
python async http server example
VladVons@gmail.com
2023.03.19
'''

import os
import re
import subprocess
from datetime import datetime
import asyncio
from asyncio import StreamReader, StreamWriter


async def ProveA():
    Sleep = 10

    Loops = 0
    while True:
        Loops += 1
        print(f'{Loops} async prove every {Sleep} sec')
        await asyncio.sleep(Sleep)


class THeader():
    @staticmethod
    def GetStatus(aCode: int) -> str:
        Data = {
            200: 'ok',
            404: 'not found'
        }
        return Data.get(aCode, 'unknown')

    @staticmethod
    def GetMime(aExt: str) -> str:
        Res = {
            'html': 'text/html',
            'css':  'text/css',
            'jpg':  'image/jpeg',
            'png':  'image/png',
            'zip':  'application/zip'
        }
        return Res.get(aExt)

    def GetHead(self, aCode: int, aType: str, aLen: int, aFile: str = '') -> str:
        Mime = self.GetMime(aType)
        if (Mime):
            ContentType = 'Content-Type: %s' % Mime
        else:
            ContentType = f'Content-disposition: attachment; filename={aFile}'

        Data  = [
            'HTTP/1.1 %d %s' % (aCode, self.GetStatus(aCode)),
            ContentType,
            'Server: MicroPy',
            'Content-Length: %d' % aLen,
            '\r\n'
        ]
        return '\r\n'.join(Data)


class THttpSrv():
    def __init__(self):
        self.Requests = 0
        self.DefPage = 'index.html'

    @staticmethod
    async def ReadHead(aReader: StreamReader) -> dict:
        Res = {}
        while True:
            Data = await aReader.readline()
            if (Data == b'\r\n') or (Data is None):
                break

            Data = Data.decode('utf-8').strip()
            if (len(Res) == 0):
                Res['mode'], Res['url'], Res['prot'] = Data.split(' ')
                Res['path'], *Res['query'] = Res['url'].split('?')
            else:
                Key, Value = Data.split(':', maxsplit=1)
                Res[Key.lower()] = Value.strip()
        return Res

    @staticmethod
    def ReadFile(aPath: str) -> tuple:
        Ext = aPath.rsplit('.', maxsplit = 1)[-1]
        Mode = 'r' if (Ext in ['html', 'css', 'js']) else 'rb'
        with open(aPath, Mode) as F:
            Data = F.read()
        return (Data, Ext)

    def Format(self, aData: str, aReplace: dict) -> str:
        Keys = re.findall(r'\{(\w+?)\}', aData)
        if (Keys):
            KeyMissed = {Key: f'-= {Key} =-'for Key in Keys if not Key in aReplace}
            InfoOut = aReplace.copy()
            InfoOut.update(KeyMissed)
            KeyPresent = {Key: InfoOut[Key] for Key in Keys}
            aData = aData.format(**KeyPresent)
        return aData

    async def CallBack(self, aReader: StreamReader, aWriter: StreamWriter):
        self.Requests += 1

        Head = await self.ReadHead(aReader)
        Path = Head.get('path').lstrip('/')
        if (not Path):
            Path = self.DefPage

        Host, Port = aWriter.get_extra_info('peername')
        Info = {
            'requests': self.Requests,
            'time':  datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'host': Head["host"],
            'remote_host': Host,
            'remote_port': Port,
            'url': Head["url"],
            'mode': Head["mode"]
        }
        print(Info)

        Header = THeader()
        if (os.path.exists(Path)):
            Data, Ext = self.ReadFile(Path)
            if (Ext == 'html'):
                Data = self.Format(Data, Info)
                Head = Header.GetHead(200, Ext, len(Data))
            elif (Ext == 'php'):
                Cmd = 'php'
                Proc = subprocess.Popen(f'{Cmd} {Path}', shell=True, stdout=subprocess.PIPE)
                Data = Proc.communicate()[0]
                if (Proc.returncode != 0):
                    Data = f'error executing {Cmd} interpreter'
                Head = Header.GetHead(200, 'html', len(Data))
            else:
                FileName = Path.rsplit('/', maxsplit=1)[-1]
                Head = Header.GetHead(200, Ext, len(Data), FileName)
        else:
            Data = f'File not exists {Path}'
            Head = Header.GetHead(404, 'html', len(Data))

        aWriter.write(Head.encode())
        if (isinstance(Data, str)):
            Data = Data.encode()
        aWriter.write(Data)

        await aWriter.drain()
        aWriter.close()

    async def Run(self, aPort: int = 80):
        Interface = '0.0.0.0'
        print(f'server listen {Interface}:{aPort}')
        await asyncio.start_server(self.CallBack, Interface, aPort)


async def Main():
    Task1 = asyncio.create_task(THttpSrv().Run(8080))
    Task2 = asyncio.create_task(THttpSrv().Run(8081))
    Task3 = asyncio.create_task(ProveA())
    await asyncio.gather(Task1, Task2, Task3)


asyncio.run(Main())
