'''
VladVons@gmail.com
2022.03.24
'''


import os
import random


def Main():
    Dir = '.'
    Files = [f for f in os.listdir(Dir) if os.path.isfile(os.path.join(Dir, f))]
    File = random.choice(Files)

    print()
    print('File:', File)
    with open(File, 'r') as F:
        print(F.read())

Main()
