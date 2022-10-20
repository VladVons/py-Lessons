def FindLetter1(aWords, aFind):
    i = 0
    Counter = 0
    while(i < len(aWords)):
        Leter = aWords[i]
        if (Leter == aFind):
            Counter += 1
        i += 1
    print (aFind, Counter)


Words = 'Hello world. Ok!'
#FindLetter1(Words, 'o')
#FindLetter1(Words, 'l')
#FindLetter1(Words, 'r')
#FindLetter1(Words, 'e')

#for Letter in ['o', 'l', 'r', 'e']:
#    FindLetter1(Words, Letter)

#for Letter in Words:
#    FindLetter1(Words, Letter)

LUniq = set(Words)
LSort = sorted(LUniq)
for Letter in LSort:
    FindLetter1(Words, Letter)
