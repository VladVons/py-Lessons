#!/usr/bin/env python3

'''
python async tor example
VladVons@gmail.com
2022.02.26
'''


import time
import requests
import json
from datetime import datetime


class TDownload():
    def __init__(self):
        self.Uniq = []

    def WriteFile(self, aName: str, aData):
        print(aData)
        with open(aName, 'a+') as FileH:
            FileH.write(aData + '\n')

    def Fetch(self, aUrl: str, aCnt: int):
        Proxies = {
            'http': 'socks5://localhost:9050',
            'https': 'socks5://localhost:9050'
        }

        Data = requests.get(aUrl, allow_redirects=True, proxies=Proxies).content.decode()
        Data = json.loads(Data)
        Data = '%s, %s, %s, %s' % (datetime.now().strftime('%d/%m/%Y %H:%M:%S'), aCnt, Data['ip'], Data['city'])
        self.WriteFile('Data.log', Data)

    def Main(self, aUrl: str, aCnt: int):
        print('Main cycles', aCnt)
        for i in range(aCnt):
            try:
                self.Fetch(aUrl, i + 1)
            except Exception as E:
                print(E)
            time.sleep(60)


StartT = time.time()
#Url='https://brain.com.ua/ukr'
Url='https://ipinfo.io/json'
TDownload().Main(Url, 1000)
print('duration (s)', round(time.time() - StartT, 2))
