#!/usr/bin/env python3

'''
python async example
VladVons@gmail.com
2021.03.04
'''


import time
import requests


class TDownload():
    def WriteFile(self, aName: str, aData):
        print('WriteFile', aName)
        with open(aName, 'wb') as FileH:
            FileH.write(aData)

    def Fetch(self, aUrl: str, aCnt: int):
        Data = requests.get(aUrl, allow_redirects=True).content
        self.WriteFile('File_%03d.jpeg' % aCnt, Data)

    def Main(self, aUrl: str, aCnt: int):
        print('Main cycles', aCnt)
        for i in range(aCnt):
            self.Fetch(aUrl, i + 1)


StartT = time.time()
TDownload().Main('https://loremflickr.com/800/600/girl', 50)
print('duration (s)', round(time.time() - StartT, 2))
