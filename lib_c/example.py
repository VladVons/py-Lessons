import time
import ctypes
import glob
import numpy


# python3 setup.py build

# find the shared library, the path depends on the platform and Python version
libfile = glob.glob('build/*/mysum*.so')[0]

# open the shared library
mylib = ctypes.CDLL(libfile)

def DTimeIt(aFunc: callable):
    def Wrapper(*aArgs, **aK):
        TimeStart = time.time()
        Res = aFunc(*aArgs, **aK)
        print(f'{time.time() - TimeStart:.3f}')
        return Res
    return Wrapper

@DTimeIt
def Test1(aLen: int):
    Array = numpy.arange(0, aLen, 1, numpy.int32)

    # tell Python the argument and result types of function mysum
    mylib.mysum.restype = ctypes.c_longlong
    mylib.mysum.argtypes = [
       ctypes.c_int,
       numpy.ctypeslib.ndpointer(dtype = numpy.int32)
    ]

    # call function mysum
    Sum = mylib.mysum(aLen, Array)
    print(f'Test1: {Sum}')

@DTimeIt
def Test2(aLen: int):
    Array = list(range(aLen))
    print(f'Test2: {sum(Array)}')

@DTimeIt
def Test3(aLen: int):
    Array = list(range(aLen))
    # slow
    Array_C = (ctypes.c_int * aLen)(*Array)

    # tell Python the argument and result types of function mysum
    mylib.mysum.restype = ctypes.c_longlong
    mylib.mysum.argtypes = [
      ctypes.c_int,
      ctypes.POINTER(ctypes.c_int)
    ]

    # call function mysum
    Sum = mylib.mysum(aLen, Array_C)
    print(f'Test3: {Sum}')

@DTimeIt
def Test4(aLen: int):
    Array = list(range(aLen))
    Sum = 0
    for x in Array:
        Sum += x
    print(f'Test4: {Sum}')


Len = 1000000
Test1(Len)
Test2(Len)
Test3(Len)
Test4(Len)
