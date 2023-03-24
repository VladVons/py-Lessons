'''
python loops speed test
VladVons@gmailcom, 2023.03.24

apt install python-profiler
pip3 install snakeviz
'''


import time
import cProfile
import pstats


def Profiler(aFunc: callable, aArgs: list = None) -> object:
    with cProfile.Profile() as F:
        Res = aFunc(*aArgs) if (aArgs) else aFunc()
    Stats = pstats.Stats(F)
    Stats.sort_stats(pstats.SortKey.TIME)
    #Stats.print_stats()
    File = f'{aFunc.__name__}.prof'
    Stats.dump_stats(File)
    print(f'To visualize use: snakeviz {File}')
    return Res

def Repeat(aFunc: callable, aArgs: list = None, aCnt: int = 100_000) -> object:
    StartAt = time.time()
    for _i in range(aCnt):
        Res = aFunc(*aArgs) if (aArgs) else aFunc()
    Time = time.time() - StartAt
    print(f'{aFunc.__name__}: {Time :.6f}, Loops: {aCnt}, Avg: {Time / aCnt :.6f}')
    return Res

#----------------------------------------------------------------

def Test_01(aArr: list, aFind: int) -> int:
    Res = 0
    i = 0
    while(i < len(aArr)):
        if (aArr[i] == aFind):
            Res += 1
        i += 1
    return Res

def Test_02(aArr: list, aFind: int) -> int:
    Res = 0
    for a in aArr:
        if (a == aFind):
            Res += 1
    return Res

def Test_03(aArr: list, aFind: int) -> int:
    #Arr = [1 for i, a in enumerate(aArr) if a == aFind]
    Arr = [1 for a in aArr if a == aFind]
    return len(Arr)

def Test_04(aArr: list, aFind: int) -> int:
    return aArr.count(aFind)

def Test_All_01(aArr: list, aFind: int) -> int:
    Repeat(Test_01, [aArr, aFind])
    Repeat(Test_02, [aArr, aFind])
    Repeat(Test_03, [aArr, aFind])
    Repeat(Test_04, [aArr, aFind])

def Test_All_02(aArr: list, aFind: int) -> int:
    Test_01(aArr, aFind)
    Test_02(aArr, aFind)
    Test_03(aArr, aFind)
    Test_04(aArr, aFind)

Arr1 = [2, 3, 7, 1, 5, 3, 12, 18, 3, 4, 3, 1, 16, 9, 7, 3, 3] * 10
print()
Test_All_01(Arr1, 3)
Profiler(Test_All_02, [Arr1, 3])
