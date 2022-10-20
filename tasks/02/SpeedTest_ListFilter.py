'''
Pyrhon list filter speed test example
Show first three not even digits from a list

2022.06.12
VladVons@gmail.com
'''

import time

BigList = [12, 6, 2, 3, 15, 8, 13, 10, 7] * 1000
MaxLen = 3

def FilterOddDigits_01():
    Res = []
    for i in range(len(BigList)):
        if BigList[i] % 2 != 0:
            Res.append(BigList[i])
    return Res[:MaxLen]

def FilterOddDigits_02():
    Res = []
    i = 0
    while i < len(BigList):
        if BigList[i] % 2 != 0:
            Res.append(BigList[i])
        i += 1
    return Res[:MaxLen]

def FilterOddDigits_03():
    Res = [i for i in BigList if i % 2 != 0]
    return Res[:MaxLen]

def FilterOddDigits_04():
    Res = list(filter(lambda x: x % 2 != 0, BigList))
    return Res[:3]

def FilterOddDigits_05():
    Res = []
    for x in BigList:
        if (x % 2 != 0):
            if (len(Res) >= MaxLen):
                break
            Res.append(x)
    return Res

def Run():
    def SpeedTest(aFunc):
        StartAt = time.time()
        for i in range(100):
            aFunc()
        return round(time.time() - StartAt, 4)

    Res = {}
    for x in [FilterOddDigits_01, FilterOddDigits_02, FilterOddDigits_03, FilterOddDigits_04, FilterOddDigits_05]:
        Res[x.__name__] = SpeedTest(x)

    Sorted = sorted(Res.items(), key=lambda kv: kv[1])
    for x in Sorted:
        print(x)

print('Speed test')
Run()
