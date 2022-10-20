import datetime



a = 1
b = 2
c = (a == b)

#if (a == b):
#if (c):
#if (c == True):
#    print('ok')
#else:
#    print('bad')

#Sunday = 0

#Today = 0
#Today = datetime.datetime.today().weekday()
#print('Today is %s' % (Today))

#if (Today == Sunday):
#    print('Hello Sunday !')
#else:
#    print('Go to school')

#IsSunday = (Today == Sunday)
#if (IsSunday):
#    print('Hello Sunday !')
#else:
#    print('Go to school')

Numbers = ['Null', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine' ]
c =  0
if (c == 0):
    print('null')
elif (c == 1):
    print('one')
elif (c == 2) or (c == -2):
    print("two")
elif (c == 3):
    print("three")
elif (c == 4) or (c == -4):
    print("four")
elif (c == 5):
    print("five")
elif (c == 6):
    print("six")
elif (c == 7):
    print("seven")
elif (c == 8):
    print("eight")
elif (c == 9):
    print("nine")
else:
    print("bad 1")

c = 5
#if (c <= 9):
#if (c < 9) or (c == 9):
if (c >= 0) and (c <= len(Numbers)):
     print (Numbers [c])
else:
    print('bad 2')


# <, <=, >, >=, ==, !=

#c = 0 
#if (c <= -1):
#if (c < 0):
    #print('negative1')
#else: 
    #print('positive1')

#if (c >= 0):
    #print('positive2')
#else: 
    #print('negative2')

c = -10
#c = 10
if (c == 10) or (c == 20) or (c == 30) or (c == 40) or (c == 50) or (c == 60) or (c == 70) or (c == 80) or (c == 90):
    print('x10-1')
else:
    print('not x10-1')

if (c in [10, 20, 30, 40, 50, 60, 70, 80, 90]):
    print('x10-2')
else:
    print('not x10-2') 

if (c % 10 == 0):
    print('x10-3')
else:
    print('not x10-3') 


#print(113 % 2)
 