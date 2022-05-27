'''
2022.05.26, VladVons@gmail.com
1c7 log file parser
'''


import glob
from datetime import datetime


def ReadFile(aFile: str):
    with open(aFile, 'r', encoding="cp1251") as hFile:
        for x in hFile.readlines():
            if ('DocWriteNew;' in x) and ('Прих. накл' in x):
                Words = x.split(';')
                DateSys = datetime.strptime(Words[0], '%Y%m%d')

                DocInfo = Words[-1].rstrip()
                DateDoc = DocInfo.split(' ')[-2].strip()
                DateDoc = datetime.strptime(DateDoc, '%d.%m.%Y')
                if (DateSys != DateDoc): 
                    DocInfo = ' '.join(DocInfo.split(' ')[:-2])
                    Days = (DateSys.date() - DateDoc.date()).days
                    print(Days, DateSys.date(), DateDoc.date(), DocInfo, Words[2])

def Main():
    for x in glob.glob('*.mlg'):
        print('---', x)
        ReadFile(x)

Main()
