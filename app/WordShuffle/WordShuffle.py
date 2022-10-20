import random


class TWordShuffle():
    def Shuffle(self, aWord: str) -> str:
        if (len(aWord) > 3) and (aWord.isalpha()):
            Middle = list(aWord[1:-1])
            random.shuffle(Middle)
            return aWord[0] + ''.join(Middle) + aWord[-1]
        return aWord

    def Parse(self, aString: str) -> str:
        Arr = [self.Shuffle(Word ) for Word in aString.split(' ')]
        return ' '.join(Arr)

    def LoadFile(self, aName: str):
        with open(aName, 'r') as FR:
            with open(aName + '.rnd', 'w') as FW:
                for Line in FR.readlines():
                    FW.write(self.Parse(Line))

WS = TWordShuffle()
WS.LoadFile('Bible.txt')
