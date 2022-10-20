'''
2022.01.23
'''

def Problem_02a():
    Arr = [12,1,2,3,5,8,13,21,34,55,9]
    #D = 10
    D = len(Arr) - 1
    while(D >=0):
        print(Arr[D])
        D -= 1

def Problem_02b():
    Arr = [12,1,2,3,5,8,13,21,34,55,9]
    for V in reversed(Arr):
        print(V)

def Problem_04():
    Arr = [12,1,2,3,5,8,13]
    #D = 0
    #while(D <= 6):
    #    print(Arr[D])
    #    D += 6
    print(Arr[0], Arr[len(Arr) - 1])

def Problem_06a():
    a = 8
    b = 5

    tmp = a
    a = b 
    b = tmp
    print(a, b)

def Problem_06b():
    a = 8
    b = 5

    a, b = b, a
    print(a, b)

def Problem_08():
    #d = 18 + 1
    #for i in range(6, d, 3):
    #    print(i)

    for i in range(6, 18+1, 3):
        print('Method1', i)

    print('Method2', list(range(6, 18+1, 3)))


#def Problem_10(Res1, Res2):
def Problem_10():
    Res1 = input('Width:')
    Res2 = input('Lenght:')
    print('Square:', int(Res1) * int(Res2))


def Problem_11(aDigit: int):
    i = 2
    while(i <= 9):
        #print(aDigit, 'x' , i, '=' , aDigit * i)
        print('%s x %s = %3d' % (aDigit, i, aDigit * i))
        i += 1
    print()

def Problem_11a(aCount: int):
    for i in range(1, aCount + 1):
        Problem_11(i)


def Problem_12a():
    Arr = [12,1,2,3,5,8,13,21,34,55]
    i = 0
    while(i < len(Arr)):
        V = Arr[i]
        if(V < 10):
            print(V)
        i += 1

def Problem_12b():
    Arr = [12,1,2,3,5,8,13,21,34,55]
    for V in Arr:
        if (V < 10):
            print(V)


def Problem_13():
    Arr = [12,6,2,3,15,8,13]
    #print(min(Arr))
    Res = None
    i = 0
    while (i < len(Arr)):
        V = Arr[i]
        if (Res == None) or (V > Res):
            Res = V
        i += 1    
    print(Res)

def Problem_13a():
    Arr = [12,6,2,3,15,8,13]   
    Res = float('inf')
    i = 0
    while (i < len(Arr)):
        V = Arr[i]
        if (V < Res):
            Res = V
        i += 1
    print(Res)    


#Problem_02a()
#Problem_02b()

#Problem_04()

#Problem_06a()
#Problem_06b()

#Problem_08()

#Problem_10(input('Width:'), input('Lenght:'))
#Problem_10()
#Problem_11a(5)
Problem_12a()
#Problem_12a()
#Problem_13()
#Problem_13a()
