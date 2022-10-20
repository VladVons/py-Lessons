def Task1():
    print('1')
    print('22')
    print('333')
    print('4444')
    print('55555')
    print('666666')

def Task2():
    print('x' * 1)
    print('x' * 2)
    print('x' * 3)
    print('x' * 4)
    print('x' * 5)
    print('x' * 6)

def Task3():
    print('1' * 1)
    print('2' * 2)
    print('3' * 3)
    print('4' * 4)
    print('5' * 5)
    print('6' * 6)

def Task4():
    i = 1
    d = 6
    while(i <= d):
        #print('x' * i)
        #print(str(i) * i)
 
        s = '%s'  % (i) * i
        print(s)
 
        i += 1


def Task5():
    d = 6
    i = d

    #while(i <= d) or ( i <= 0):
    while( i > 0):
        #print('x' * i)
        print(str(i) * i)
 
        #s = '%s'  % (i) * i
        #print(s)
 
        i -= 1
    print ('end')

    def Task6(aMsg: str, aIdx: int) -> str:
    Arr = ["zero", "one", "two", "three"]
    Idx = min(max(0, aIdx), len(Arr) - 1)
    Res = "%s %s" % (aMsg, Arr[Idx])
    return Res

Res = Task6("Digit:", 2)
print(Res)

        
#Task1()
#Task2()
#Task3()
#Task4()
#Task5()
Task6()
