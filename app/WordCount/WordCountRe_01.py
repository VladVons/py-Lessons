'''
Python example. Words counter
2022.06.20
VladVons@gmail.com
'''

import re

class TWords():
    def __init__(self):
        self.Data = []

    def LoadFile(self, aFile: str):
        with open(aFile, 'r') as File:
            Data = File.read()
            self.LoadString(Data)

    def LoadString(self, aData: str):
        self.Data = re.findall('\w+', aData)

    def Show(self):
        print('Words', len(self.Data))
        print(self.Data)


Words = TWords()
Words.Show()

print()
File = 'Noviy_zavet_matv.txt'
Words.LoadFile(File)
Words.Show()

print()
Words.LoadString('Hello there from Ukraine :) !')
Words.Show()
