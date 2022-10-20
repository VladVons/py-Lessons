
# вивести числа менші 10 і більші 2
def Problem0():
    Arr = [12,1,2,3,5,8,13,21,34,55,9]
    #print(len(Arr))
    #print()
   
    i = 0
    while(i < len(Arr)): 
        a = Arr[i]  
        #if (a < 10):
        #    if (a > 2):
        #        print(a)

        #if (a < 10) and (a > 2):
            #print(a)

        if (2 < a < 10 ):
            print(a)

        i += 1
    print('end')

# вивести перші 3 числа
def Problem1():
    Arr = [6,12,1,2,3,5,8,13,21,34,55,9]
    i = 0
    while(i < 3 ):
        print(Arr[i])
        i += 1 

# сума чисел
def Problem2a():
    Arr = [6,12,1,2,3,5,8,9]
    i = 0
    d = 0
    while(i < len(Arr)):
        a = Arr[i]
        d += a
        i = i + 1
    print(d)

# середнє значення
def Problem2b():
    Arr = [6,12,1,2,3,5,8,9]
    i = 0
    d = 0
    while(i < len(Arr)):
        a = Arr[i]
        d += a
        i = i + 1
    print(d, round(d / len(Arr)))

# сума чисел більших 10
def Problem2c():
    Arr = [6,12,1,2,3,5,8,13,21,34,55,9]
    i = 0
    d = 0
    while(i < len(Arr)):
        a = Arr[i]
        if (a > 10):
            d = d + a
            print(a)
        i = i + 1
    print(d)


Problem0()
#Problem1()
#Problem2a()
#Problem2b()
#Problem2c()
