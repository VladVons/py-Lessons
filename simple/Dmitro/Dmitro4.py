Arr = [12,1,2,3,5,8,13,21,34,55,9]

def task1():
     for i in Arr:
        print(i)

def task2a():
    for i in Arr[::-1]:
        print(i)

def task2b():
    for i in reversed(Arr):
        print(i)

def task2c():
    i = len(Arr) -1
    while(i >= 0):
        print(Arr[i])
        i -= 1

def task3a():
    for i in range(6 , 18+1, 3):
        print(i)

def task3b():
    i = 6
    while(i <= 18):
        print(i)
        i += 3

def task4():
    W: str  = input('Width:')
    L: str = input('Lenght:')
    if (L.isdigit()):
        pass
    else:
        print('nothing is specified')
    if (W.isdigit()):
        pass
    else:
        print('nothing is specified')
    print('Square:', int(W) * int(L))

def task5a():
    a = 4
    for i in range(2, 9+1):
        print('%s * %s = %s' % (a, i, a * i))

def task5b():
    for i in range(2, 9+1):
        print()
        for a in range(2, 9+1):
            print('%s * %s = %s' % (i, a, a * i))
    
def task6():
    Arr = [12,1,2,3,5,8,13,21,34,55,9]
    i = 0
    while(i < len(Arr)):
        if(Arr[i] % 2 != 0 ):
            print(Arr[i])
        i += 1

def task7():
    Arr = [12,1,2,3,5,8,13,21,34,54,55,9,90]

    #i = 0
    #while (i < len(Arr)):
    #    if(Arr[i] % 3 == 0):
    #        print(Arr[i])
    #    i += 1 

    for i in Arr:
        if(i % 3 == 0):
            print(i)

    print()
    for i1 in Arr:
        si1 = str(i1)
        Sum = 0
        for i2 in si1:
            Sum += int(i2)
        
        if (Sum % 3 == 0):
            print(i1)


#task1()
#task2a()
#task2b()  
#task2c()      
#task3a()
#task3b()
#task4()
#task5a()
#task5b()
#task6()
task7()
