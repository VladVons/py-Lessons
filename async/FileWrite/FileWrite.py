#!/usr/bin/env python3

'''
python async example
VladVons@gmail.com
2021.01.07
'''


import time
import os


class TFileWrite():
    def WriteFile(self, aName: str, aData):
        print('WriteFile', aName)
        with open(aName, 'w') as FileH:
            FileH.write(aData)

    def Main(self, aDir: str, aCnt: int):
        print('Main cycles', aCnt)
        os.makedirs(aDir, exist_ok=True)

        for i in range(aCnt):
            File = '%s/file_%04d.txt' % (aDir, i)
            self.WriteFile(File, (File + '\n') * 10000)
        print('Main. Done')


StartT = time.time()
TFileWrite().Main('/mnt/smb/tr41/files', 100)
print('duration (s)', round(time.time() - StartT, 2))
