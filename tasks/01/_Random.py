'''
VladVons@gmail.com
2022.03.24
'''


import os
import random


def GetFiles(aPath: str) -> list:
    Res = []
    for File in os.listdir(aPath):
        Path = aPath + '/' + File
        if (os.path.isdir(File)):
            Res += GetFiles(Path)
        else:
            Res.append(Path)
    return Res

 
def Main():
    Files = GetFiles('.')
    File = random.choice(Files)

    print()
    print(f'Files: {len(Files)}')
    print('Random file:', File)
    with open(File, 'r') as F:
        print(F.read())

Main()
