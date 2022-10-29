# https://habr.com/ru/post/469043/

import sys
import glob


def Test1():
    LibDir = glob.glob('build/lib*')[0]
    sys.path.append(LibDir)
    print(LibDir)

    import MyLib, FS

    print()
    print('Py Hello(): ', MyLib.Hello())

    print()
    print('Py GetInt(): ', MyLib.GetInt(101))

    print()
    print('Py GetDouble: ', MyLib.GetDouble(3.14))

    print()
    print('Py GetStr: ', MyLib.GetStr('Hello!'))

    print()
    print('Py GetMany(): ', MyLib.GetMany(15, 18.1617, "Many arguments!"))

    print()
    print('var a: ', MyLib.a)

    print()
    print('Py GetFiles(): ', FS.GetFiles("/etc"))

Test1()

