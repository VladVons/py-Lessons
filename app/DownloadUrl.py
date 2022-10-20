'''
Python lesson. 
Download url
VladVons@gmail.com, 2022.04.15
'''

import requests

def Download(aUrl: str):
    Data  = requests.get(aUrl)
    if (Data.status_code == 200):
        FileName = aUrl.split('/')[-1]
        with open(FileName,'wb') as File:
            File.write(Data.content)
        print('Saved %d bytes to %s' % (len(Data.content), FileName))
    else:
        print('Cant load %s' % aUrl)

Download('http://oster.com.ua/image/catalog/logo_2.png')
