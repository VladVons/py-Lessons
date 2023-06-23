# Created: 2023.05.01
# Author: Vladimir Vons <VladVons@gmail.com>
# License: GNU, see LICENSE for more details


import os
import sys
import argparse
from xlrd import open_workbook


def FileWrite(aFile: str, aData: dict):
    Data = [f'{Key}\t{Val}' for Key, Val in aData.items()]
    Data = '\n'.join(Data)
    File = f'{aFile}.txt'
    print('saving file', File)
    with open(File, 'w', encoding='utf8') as F:
        F.write(Data)

def LoadOptions():
    Usage = f'usage: --ukr <file> --can <file>'
    Parser = argparse.ArgumentParser(usage = Usage)
    Parser.add_argument('--ukr', default='ukr.xls')
    Parser.add_argument('--can', default='can.xls')
    return Parser

def LoadFile_Ukr(aFile: str) -> dict:
    assert(os.path.isfile(aFile)), f'file not exists {aFile}'

    Res = {}
    WBook = open_workbook(aFile)
    Sheet = WBook.sheet_by_index(0)

    for i in range(0, Sheet.nrows):
        Row = Sheet.row_values(i)
        Code, *Name = Row[0].split(' ', maxsplit=1)
        if (Name):
            Res[Code] = Name[0]
    return Res

def LoadFile_Can(aFile: str) -> dict:
    assert(os.path.isfile(aFile)), f'file not exists {aFile}'

    Res = {}
    WBook = open_workbook(aFile)
    Sheet = WBook.sheet_by_index(0)

    for i in range(0, Sheet.nrows):
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

def Parse(aOptions):
    DataUkr = LoadFile_Ukr(aOptions.ukr)
    DataCan = LoadFile_Can(aOptions.can)

    Dif = Compare(DataUkr, DataCan)
    FileWrite(aOptions.ukr, Dif)

    Dif = Compare(DataCan, DataUkr)
    FileWrite(aOptions.can, Dif)

    print('done')

def Main():
    print('Compare UkrCan, v1.01, VladVons@gmail.com')
    print(sys.version)
    print(sys.executable)

    Parser = LoadOptions()
    if (len(sys.argv) == 1):
        Parser.print_help()
    else:
        Options = Parser.parse_args()
        Parse(Options)

Main()
