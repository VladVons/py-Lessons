'''
VladVons@gmail.com

Show all digits from a list less then 10
[12, 1, 2, 3, 5, 8, 13, 21, 34, 55, 9]
'''

import os
os.system('clear')


Max = 10
List = [12, 1, 3, 8, 13, 21, 34, 55, 9, 5, 2]


def Method_1():
    print('Method 1')
    i = 0
    while (i < len(List)):
        Item = List[i]
        if (Item < Max):
            print(Item)
        i += 1

def Method_2():
    print('Method 2')
    for i in range(len(List)):
        Item = List[i]
        if (Item < Max):
            print(Item)

def Method_3():
    print('Method 3')
    for Item in List:
        if (Item < Max):
            print(Item)

def Method_4():
    print('Method 4')
    [print(Item) for Item in List if (Item < Max)]

def Method_5():
    print('Method 5')
    Res = filter(lambda Item: Item < Max, List)
    print(list(Res))

def Method_6():
    print('Method 6')
    Res = filter((Max).__ge__, List)
    print(list(Res))


Method_1()
Method_2()
Method_3()
Method_4()
Method_5()
Method_6()
