'''
Python example. Most used words
VladVons@@gmail.com
2022.06.24
'''


import re 


class TWords():
    def __init__ (self):
        self.Data = []

    def LoadFile(self, aFile: str):
        with open (aFile, 'r') as File:
            data = File.read().lower()
            self.StringLoad(data)

    def StringLoad (self, aData: str):
        self.Data = re.findall('\w{3,}', aData)

    def Top(self, aCnt: int, aReverse: bool = True) -> list:
        Words = {}
        for Word in self.Data:
            Words[Word] = Words.get(Word, 0) + 1

        Sorted = sorted(Words.items(), reverse=aReverse, key=lambda item: item[1])
        for Word in Sorted[:aCnt]:
            print(Word)


Words = TWords()
#File = __file__
File = 'Noviy_zavet_matv.txt'
Words.LoadFile(File)
Words.Top(20, True)
