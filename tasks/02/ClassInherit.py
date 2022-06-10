'''
write conditional class inheritance
2022.05.07
'''


class TClassStr():
    def Test1(self):
        print('TClassStr.Test1', self.Value)


class TClassNum():
    def Test2(self):
        print('TClassNum.Test2', self.Value)


def MagicClassInherit(aValue: object):
    if (type(aValue) == str):
        Class = TClassStr
    else:
        Class = TClassNum

    class TClass(Class):
        def __init__(self, aValue: object):
            self.Value = aValue

        def Test3(self):
            print('TClass.Test3', self.Value)

    return TClass(aValue)


print()
Obj1 = MagicClassInherit(1)
Obj1.Test3()
Obj1.Test2()

print()
Obj2 = MagicClassInherit('Just python')
Obj2.Test3()
Obj2.Test1()
