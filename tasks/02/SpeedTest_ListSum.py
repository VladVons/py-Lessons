'''
Pyrhon list sum speed test example

2023.02.03
VladVons@gmail.com
'''

import time


def Decor_SpeedTest(aFunc):
    def Wraper(aData):
        StartAt = time.time()
        Loops = 10_000
        for _i in range(Loops):
            aFunc(aData)
        print('%s, %.3fs' % (aFunc.__name__, time.time() - StartAt))
    return Wraper

@Decor_SpeedTest
def Sum_01(aData: str):
    return sum(int(aData[x]) for x in range(1, len(aData) -1, 2))

@Decor_SpeedTest
def Sum_02(aData: str):
    return sum(int(x) for x in aData[0::2])

@Decor_SpeedTest
def Sum_03(aData: str):
    return sum([int(x) for x in aData[0::2]])

@Decor_SpeedTest
def Sum_04(aData: str):
    return sum(map(int, aData[0::2]))


print('Speed test')
BigList = '123456789012' * 100
Sum_01(BigList)
Sum_02(BigList)
Sum_03(BigList)
Sum_04(BigList)
