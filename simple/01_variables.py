'''
this is a multiple
line comment string
'''

# operands:
# + - * / %

# comparation
# >, >=, <, <=, ==, !=
if (4 > 4) or (4 == 4):
    print('OK')

# Variables
#12MyInt = 1# Error
MyInt = 1 # int
MyStr1 = "1" # str
MyStr2 = 'Hello world' 
MyFloat = 3.1415 # float
MyLogic = True # logical true/false
MyList = [1, 2, 3, 4, 5] # array list
MyDict = {'1': 'one', '2': 'two', '3': 'three'} # array dict

#d = MyInt + MyStr # Error !
d = str(MyInt) + MyStr1
print(MyInt, MyStr1, MyStr2, d)

# bad 
s = 0
m = 1
t = 2 
print('bad', s, m, t)

# good. first day of the week 
sun = 0
mon = 1
thu = 2 
print('good', sun, mon, thu)

THURSDAY = 2
print('best', Sunday, Monday, THURSDAY)

# Logical
a = True
a = (2==2)

c = (3 != 5) 
d = (3 < 5) 
#print(a, b, c, d)
#print(c, d)
#print(type(True), type('True'))
#print(2==2)
#print(3 != 5, 3 < 5)
print(a)

#c = (Sunday == 3) 
#print('Is Suday', Sunday == 0)
#print('Is Suday', c)

