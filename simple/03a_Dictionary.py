DigitList = ['Null', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine' ]
DigitDict = {'Null': 'Ноль', 'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Чотири', 'Five': 'Пять', 'Six': 'Шість', 'Seven': 'Сім', 'Eight': 'Вісім', 'Nine': 'Девять'}

def task1():
    for i in DigitList:
        print(i)

def task2():
    i = 0
    while(i < len(DigitList)):
        print(DigitList[i])
        i += 1

def task3():
    for Key in DigitDict:
        print(Key, DigitDict[Key])

def task4a(aWord: str):
    aWord = aWord.lower()
    if (aWord == 'one'):    
        a = 'Один'
    elif (aWord == 'two'):    
        a = 'Два'
    elif (aWord == 'three'): 
        a = 'Три'
    else:
        a = '???'
    
    print(a)

def task4b():
    a = DigitDict['Two']
    print(a)

#task1()
#task2()
#task3()
task4a('Two')
task4a('two')
