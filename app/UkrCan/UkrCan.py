# Created: 2023.05.01
# Author: Vladimir Vons <VladVons@gmail.com>
# License: GNU, see LICENSE for more details


import sys
import argparse
from xlrd import open_workbook


def FileWrite(aFile: str, aData: dict):
    Data = [f'{Key}\t{Val}' for Key, Val in aData.items()]
    Data = '\n'.join(Data)
    File = f'{aFile}.txt'
    print(File)
    with open(File, 'w', encoding='utf8') as F:
        F.write(Data)

def LoadOptions():
    Usage = f'usage: --ukr <file> --can <file>'
    Parser = argparse.ArgumentParser(usage = Usage)
    Parser.add_argument('--ukr', default='ukr.xls')
    Parser.add_argument('--can', default='can.xls')
    return Parser.parse_args()


def LoadFile_Ukr(aFile: str) -> dict:
    Res = {}

    WBook = open_workbook(aFile)
    Sheet = WBook.sheet_by_index(0)

    for i in range(2, Sheet.nrows):
        Row = Sheet.row_values(i)
        Code, *Name = Row[0].split(' ', maxsplit=1)
        if (Name):
            Res[Code] = Name[0]
    return Res

def LoadFile_Can(aFile: str) -> dict:
    Res = {}

    WBook = open_workbook(aFile)
    Sheet = WBook.sheet_by_index(0)

    for i in range(2, Sheet.nrows):
        Row = Sheet.row_values(i)
        Code = Row[0].replace('TER', '')
        Res[Code] = Row[1]
    return Res

def Compare(aData1: dict, aData2: dict):
    Res = {}
    for Key, Val in aData1.items():
        if (Key not in aData2):
            Res[Key] = Val
    return Res


print('Compare UkrCan, v1.01, VladVons@gmail.com')
print(sys.version)
print(sys.executable)

Options = LoadOptions()

DataUkr = LoadFile_Ukr(Options.ukr)
DataCan = LoadFile_Can(Options.can)

Dif = Compare(DataUkr, DataCan)
FileWrite(Options.ukr, Dif)

Dif = Compare(DataCan, DataUkr)
FileWrite(Options.can, Dif)

print('done')
