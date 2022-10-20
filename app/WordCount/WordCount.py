'''
Python lesson
File word counter 
VladVons@gmail.com, 2022.03.01
'''


def Main_A(aFile: str):
    Words = {}
    WordsCnt = 0
    with open(aFile, 'r') as F:
        for Line in F:
            for Word in Line.split():
                WordsCnt += 1
                if (len(Word) > 3):
                    Word = Word.lower()
                    Words[Word] = Words.get(Word, 0) + 1

    WordsSorted = sorted(Words.items(), reverse=True, key=lambda item: item[1])
    for Word in WordsSorted[:50]:
        print(Word)
    print('Words', WordsCnt)


Main_A('Noviy_zavet.txt')
#Main_A('Noviy_zavet_matv.txt')
