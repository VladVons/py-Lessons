'''
2022.05.26, VladVons@gmail.com
1c7 log file parser
'''


import glob
from datetime import datetime


class TLog():
    def FilterOr(self, aLine: str, aFilter: list):
        return bool([Filter for Filter in aFilter if (Filter in aLine)])

    def FilterAnd(self, aLine: str, aFilter: list):
        for Filter in aFilter:
            if (Filter not in aLine):
                return False
        return True

    def Print(self, aData: list, aDelim: str = '\t'):
        print(aDelim.join([str(x) for x in aData]))

    def DiffDate(self, aLine: str):
        Words = aLine.split(';')
        DateSys = datetime.strptime(Words[0], '%Y%m%d')

        DocInfo = Words[-1].rstrip()
        DateDoc = DocInfo.split(' ')[-2].strip()
        DateDoc = datetime.strptime(DateDoc, '%d.%m.%Y')
        if (DateSys != DateDoc): 
            DocInfo = ' '.join(DocInfo.split(' ')[:-2])
            Days = (DateSys.date() - DateDoc.date()).days
            self.Print([Days, DateSys.date(), DateDoc.date(), DocInfo, Words[2]])

    def ReadFile(self, aFile: str):
        with open(aFile, 'r', encoding="cp1251") as hFile:
            for Line in hFile.readlines():
                if ('DocWriteNew;' in Line):
                    if (self.FilterOr(Line, ['Спис. ТМЦ', 'Прих. накл', 'Расх. накл', 'Розн. накл'])):
                    #if (self.FilterAnd(Line, ['Спис. ТМЦ', 'Сичевський'])):
                    #if (self.FilterAnd(Line, ['Сичевський'])):
                    #if (self.FilterAnd(Line, ['Прих. накл', 'Сичевський'])):
                        self.DiffDate(Line)
                        #print(Line)

    def Main(self):
        for x in sorted(glob.glob('*.mlg')):
            print('---', x)
            self.ReadFile(x)


Log = TLog()
Log.Main()
