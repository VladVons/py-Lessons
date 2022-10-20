def Replication(aMessage, aCount):

    for i in range(aCount):
        print(i, aMessage * (i + 1))


def MathAdd(aVal1, aVal2):
    Res = aVal1 + aVal2
    return Res

def MathAdd2(aDigit):
    i = 0
    Res = 0
    while(aDigit >= i):
        Res += i
        i += 1
    return Res         

def MathAdd3(aDigit):
    Res = 0
    while(aDigit > 0):
        Res += aDigit
        aDigit -= 1
    return Res   

def MathAdd4(aDigit):
    Res = 0
    for i in range(1, aDigit + 1):
        Res += i
    return Res

def MathAdd5(aDigit):
    Res = 0
    for i in range(aDigit):
        Res += i+1
    return Res

def MathAdd6(aDigits):
    Res = 0
    for i in aDigits:
        Res += i
    return Res

def MathAdd7(aDigit):
    Res = 0
    for i in range(0, aDigit, 10):
        Res += i
    return Res


#Replication('Hello ', 5)
#print()
#Replication('World ', 3)


#A = MathAdd(3, 4)
#print(A)

#print(MathAdd(5, 4),MathAdd(2, 1) )

print(1+2+3+4+5)
print(MathAdd2(5))

print(5+4+3+2+1)
print(MathAdd3(5))
print(MathAdd4(5))
print(MathAdd5(5))
print(MathAdd6([1,2,3,4,5]))
print(MathAdd7(50))

