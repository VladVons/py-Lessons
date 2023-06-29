import time
import random


def SpeedTestA(aCnt: int) -> int:
    Res = 0
    for i in range(aCnt):
        Res += i
    return Res

def SpeedTestB(aCnt: int) -> int:
    Res = 0
    Str1 = 'The quick brown fox jumps over the lazy dog';
    for i in range(aCnt):
        Arr = Str1.split(' ')
        random.shuffle(Arr)
        Res += i + len(Arr[0])
    return Res

Time = time.time()
SpeedTestB(1000000)
print('done', time.time() - Time)
