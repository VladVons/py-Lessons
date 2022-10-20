a = 10
b = 20
c = 30
d = 60

#print(a, b, c)


#c = input ("Введите число: ")
def Test1():
    if (a + b == 30):
        print( "okey")
        print( "%s + %s = %s" % (a, b, c))
    elif (a + b == 40):
        print( "okey2")
    else:
        print("bad")


def Test2():
    if (a + b * 2 == 40):
        print("good joy")
    else:
        print("bad joy. must be", a + b * 2)


def Test3():
    d = input("Input a digit:")
    print("you input a digit", d)
    if (a + b * 2 == int(d)):
        print("good joy")
    else:
        print("bad joy. must be", a + b * 2)

#Test1()
#Test2()
Test3()
