Arr = [2, 7, 1, 5, 3, 12, 18, 4, 16, 9, 7, 3]

#виводить перших 3 числа
def Problem01():
    i = 0
    while(i < 3):
        print(Arr[i])
        i += 1

# виводить всі числа масиву
def Problem02():
    i = 0
    while(i < len(Arr)):
        print(Arr[i])
        i += 1
    
 #виводить всі числа більше 3 
def Problem03():
    i = 0
    while(i < len(Arr)):
        if (Arr[i] > 3):
            print(Arr[i])
        i += 1

#виводить числа більше 3 починаючи з 3 елеиента
def Problem04():
    i = 2
    while(i < len(Arr)):
        if (Arr[i] > 3):
            print(Arr[i])
        i += 1

#виводить числа більше 3 починаючи з 3 елеиента і закінчуючи перед двома останіми
def Problem05():
    i = 2
    while(i < len(Arr) - 2):
        if (Arr[i] > 3):
            print(Arr[i])
        i += 1

# знайти максимальне число
def Problem06():
    Arr = [2, 7, 1, 5, 3, 12, 18, 4, 16, 9]
    
    i = 0
    a = 0
    print(a)
    while(i < len(Arr)): 
        if (Arr[i] > a):
            a = Arr[i]
            #print(a)
        i += 1
    print(a)

# сума чисел і середнє число
def Problem07a():
    i = 0
    d = 0
    while(i < len(Arr)):
        a = Arr[i]
        d += a
        i += 1
    Avr = d / len(Arr) 
    print(d, Avr, round(Avr))    

# сума чисел і середнє число
def Problem07b():
    d = 0
    for a in Arr:
        d += a
    Avr = d / len(Arr) 
    print(d, Avr, round(Avr))    

#Problem01()
#Problem02()
#Problem03()
#Problem04()
#Problem05()
#Problem06()
#Problem07a()
Problem07b()
