'''
Pyrhon Example
find minimal digit in nested list

VladVons@gmail.com
2022.06.10
'''

import sys


def MinimalDigitRecurs(aData: list, aMin: int):
    for x in aData:
        if (type(x) == list):
            x = MinimalDigitRecurs(x, aMin)

        if (x < aMin):
            aMin = x
    return aMin


Arr = [12, 6, 2, 3, 15, 8, 13]
Min = MinimalDigitRecurs(Arr, sys.maxsize)
print(Min, Arr)

Arr = [[2, 6, 5], [3, 15, [1, [12, -4, 60], 10]]]
Min = MinimalDigitRecurs(Arr, sys.maxsize)
print(Min, Arr)
