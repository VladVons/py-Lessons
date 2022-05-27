'''
Python lesson
File word counter 
VladVons@gmail.com, 2022.03.01
'''

def Main(aFile: str):
    Words = {}
    WordsCnt = 0
    with open(aFile, 'r') as F:
        for Line in F:
            for Word in Line.split():
                WordsCnt += 1
                if (len(Word) > 3):
                    Word = Word.lower()
                    Count = Words.get(Word, 0)
                    if (Count == 0) :
                        Words[Word] = 1
                    else:
                        Words[Word] = Count + 1

    WordsSorted = sorted(Words.items(), reverse=True, key=lambda item: item[1])
    for Word in WordsSorted[:50]:
        print(Word)
    print('Words', WordsCnt)


#Main('Noviy_zavet.txt')
Main('Noviy_zavet_matv.txt')
