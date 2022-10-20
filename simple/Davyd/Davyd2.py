


Arr = [12,1,2,3,5,8,13,21,34,55,9]

def Task3():
    i = 0
    while(i < 3):
        print (Arr[i])
        i += 1

def Task4():
    Arr = [12,1,2,3,5,8,13]
    #D = 0
    #while(D <= 6):
    #    print(Arr[D])
    #    D += 6 
    #print(Arr[0], Arr[len(Arr) - 1])
    print(Arr[0], Arr[-1])

def Task5():
    Arr = [12,1,2,3,5,8,13]
    i = 0
    Res = 0
    while (i < len(Arr)):
        Res += Arr[i]
        i += 1
    print(Res)

def Task6():
    a = 8
    b = 5

    c = a
    a = b
    b = c
    
    #b, a = a, b
    print(a, b)

def Task7():
    Arr = [12,1,2,3,5,8,13]
    i = 0
    while(i < len(Arr)):
        if(Arr[i] %2 == 0 ):
            print(Arr[i])
        i += 1

def Task9():
    A = -3
    if (A >= 3) and (A <= 5):
        print('Весна')
    elif (A >= 6) and (A <= 8):
        print('Літо')
    elif (A >= 9) and (A <= 11):
        print('Осінь')
    elif (A == 12) or ((A > 0) and (A <= 2)):
        print('Зима')
    else:
        print('%s is not a month' % (A))

def Task9B():
    A = 4

    Spring = [3,4,5]
    Summer = [6,7,8]
    Autumn = [9,10,11]
    Winter = [12,1,2]

    if (A in Spring):
        print('Весна')
    elif(A in Summer):
        print('Літо')
    elif(A in Autumn):
        print('Осінь')
    elif(A in Winter):
        print('Зима')
    else:
        print('%s is not a month' % (A))

def Task13():
    Arr = [12,1,2,3,5,8,13,21,34,55,9]
    A = None
    i = 0
    while (i < len(Arr)):
        V = Arr[i]
        if (A == None) or (V > A):
            A = V
        i += 1    
    print(A)
        

#Task3()
#Task4()
#Task5()
#Task6()
#Task7()
#Task9()
#Task9B()
Task13()