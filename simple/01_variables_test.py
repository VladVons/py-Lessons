a = 10
b = 20
c = a + b
f = 3.145
#print(a,b,c)
#print(c, a + b + c1)
#print(a * 5)
# print( (a + b) * 2 )

#d = (a + b) * 2
#print (d)

#print("a + b =", a + b)
#print("a + b = " + "a + b")
#print("a + b = " + str(a + b))
#print("a + b = %s. This is good" % (a + b))
print(str(a) + "+" + str(b) + "=" + str(a + b))
#print("a + b = %s, a * b = %s, f = %f" % (a + b, a * b, f) )

a = 2022
b = 'Hello'
c = 'World'
d = 8
e = 3.14159
f = False


# 'Hello + World  = HelloWorld2022' 
print('%s + %s = %s' % (b, c, b+c+str(a)))
print('%s + %s = %s%s' % (b, c, b + c, a))

# Hello + World  = Hello 'World' 2022
print("%s + %s = %s '%s' %s" % (b, c, b, c, a))

# Hello + World  = Hello 'World' 2022 + 8 = 2030
print("%s + %s = %s '%s' %s + %s = %s" % (b, c, b, c, a, d, a+d))

# str: Hello, int: 2022, float: 3.14, bool: True
print('str: %s, int: %s, float: %s, bool: %s' % (b, a, round(e, 2), not f))
print('str: %s, int: %d, float: %.2f, bool: %s' % (b, a, round(e, 2), not f))

