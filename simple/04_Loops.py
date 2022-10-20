from ast import While


Numbers = ['Null', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine' ]
#print('Array length', len(Numbers))

#print(Numbers[0])
#print(Numbers[1])
#print(Numbers[2])
#print(Numbers[3])
#print(Numbers[4])
#print(Numbers[5])
#print(Numbers[6])
#print(Numbers[7])
#print(Numbers[8])
#print(Numbers[9])

def Test0():
    a = False
    i = 0
    while (i < 10):
        print(i, a)
        i += 1
        a = not a

Digits = [0, 1, 2, 3, 4, 5]
#Digits = list(range(50))
#print(Digits)

#for D in Digits:
#     print(D)
#print('the end')

#for D in range(5):
#     print(D)

#a1 = 0
#for Number in Numbers:
#     print(Numbers[a1])
#     a1 += 1

#D = 0
#while (D < 20):
#     print(D)
#     #D = D + 1
#     #D += 1
#
#     D = D + 2

#D = 5
#while (D < 20):
#     print(D)
#     D = D + 5

#D = 20 
#while (D >= -1):
#while (D >= 0):
#     print(D*2)
#     if (D == 15) or (D == 5):
#          print('hello', D)
#     D = D - 5

#D = 20 
#while (D >= 0):
#     print(D * 2)
#     D = D - 5


Numbers = ['Null', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine' ]
#print(len(Numbers), Numbers[1])

#D = 0
#while (D < len(Numbers)):
#     print(D, Numbers[D])
#     D += 2

#D = len(Numbers) - 1
#while (D >= 0):
#     print(D, Numbers[D])
#     D -= 2


# 0 Null 9 Nine
# 1 One  8 Eight
#D = 0
#C = len(Numbers) - 1
#while (D < len(Numbers)):
#     print(D, Numbers[D], C, Numbers[C])
#     D += 1
#     C -= 1

#D = 0
#L = len(Numbers) - 1 
#while (D < len(Numbers)):
     #print(D, L-D)
     #print(Numbers[D],'-',Numbers[L-D])
     #print(Numbers[D] + '-' + Numbers[L-D])
 #    print('%s-%s' % (Numbers[D], Numbers[L-D]))
 #    D += 1


def Test1():
    D = 0
    L = len(Numbers) - 1 
    while (D <= L):
        #print(str(D) + '+' + str(L-D) + '=' + str(D+L-D))
        print('%s+%s=%s' %(D, L-D, D+(L-D)))
        D += 1

    print('The end')

def Test2():
    c = 0
    while (c < 10):
        l = c % 4
        print(c, l)
        #if (l == 0):
        #    print(c , 'good', l)
        #    #c += 1
        #else:
        #    print(c , 'bad', l)
            #c += 1
        c += 1

def Test3():
    for c in range(10):
        l = c % 4
        print(c, l)


def Test4():
    print('Hello1')
    print('Hello1 Hello1')
    print('Hello1 Hello1 Hello1')
    print()

    s = 'Hello2'
    print(s)
    print(s + ' ' + s)
    print(s + ' ' + s + ' ' + s)
    print()

    s = ''
    p = 'Hello3'
    for b in range(3):
        s += p + ' '
        print(s)
    print()

    s = 'Hello4 '
    #for i in range(3):
    for i in [0, 1 , 2]:
        print(i, s * (i + 1))
    print()

def Test5():
    s = 'Hello5 '
    for i in [2, 1, 0]:
        print(i, s * (i + 1))

def Test6():
    s = 'Hello6 '
    Count = 3
    for i in range(Count):
        print(i, s * (Count - i))


#  10
#  20
# ...
# 100
def TestDmitro1():
    c = 0
    while(c < 100):
        c += 10
        print(c)

#  10, 90
#  20, 80
# ...
# 100, 0 
def TestDmitro2():
    c = 0
    d = 100
    while(c < 100):
        c += 10
        #d -= 10
        print(c , d)

def TestDavyd():
    c = 100
    while(c > 0):
        print(c)
        c -= 10



def TestDmytro(): 
    #for i in [1,2,3,4,5,6,7,8,9]: 
    for i in range(0, 1000, 50): 
        print(i)
    
#Test1()
#Test2()
#Test3()
#Test4()
#Test5()
#Test6()
#TestDmitro1()
#TestDmitro2()
#TestDavyd()
TestDmytro()