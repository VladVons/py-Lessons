/*
Speed test
VladVons@gmailcom
2023.12.09
*/

#include <iostream>
#include <ctime>

extern "C" int TestAsm1(int aArr[], int aSize, int aFind);
extern "C" int TestAsm2(int aArr[], int aSize, int aFind);


int Test_01(int aArr[], int aSize, int aFind) {
    int Res = 0;
    int *ptr = aArr;
    int *ptrEnd = ptr + aSize;
    while (ptr != ptrEnd) {
        if (*ptr++ == aFind) {
            Res++;
        }
    }
    return Res;
}

int Test_02(int aArr[], int aSize, int aFind) {
    int Res = 0;
    int i = 0;
    while (i < aSize) {
        if (aArr[i] == aFind) {
            Res++;
        }
        i++;
    }
    return Res;
}

int Test_03(int aArr[], int aSize, int aFind) {
    int Res = 0;
    for (int i = 0; i < aSize; i++) {
        if (aArr[i] == aFind) {
            Res++;
        }
   }
   return Res;
}

int Test_04(int aArr[], int aSize, int aFind) {
    int Res = 0;
    int *ptrEnd = aArr + aSize;
    for (int *ptr = aArr; ptr != ptrEnd; ptr++) {
        if (*ptr == aFind) {
            Res++;
        }
   }
   return Res;
}

void SpeedFunc(int (*aFunc)(int aArr[], int aSize, int aFind), int aArr[], int aSize, int aFind, int aCount) {
    clock_t Start = clock();
    int Res = 0;
    for (int i = 0; i < aCount; i++) {
        Res = aFunc(aArr, aSize, aFind);
    }
    std::cout << "Method: " << aFunc << ", Time: " << static_cast<double>(clock() - Start) / CLOCKS_PER_SEC << ", Found: " << Res << std::endl;
}

void SpeedAll(int aArr[], int aSize, int aFind, int aCount) {
    clock_t Start = clock();

    std::cout << std::endl;
    std::cout << "C++" << std::endl;
    int (*Methods1[])(int aArr[], int aSize, int aFind) = { Test_01, Test_03};
    for (auto Method : Methods1) {
        SpeedFunc(Method, aArr, aSize, aFind, aCount);
    }

    std::cout << std::endl;
    std::cout << "ASM" << std::endl;
    int (*Methods2[])(int aArr[], int aSize, int aFind) = { TestAsm1, TestAsm2};
    for (auto Method : Methods2) {
        SpeedFunc(Method, aArr, aSize, aFind, aCount);
    }

    std::cout << "Total: " << static_cast<double>(clock() - Start) / CLOCKS_PER_SEC << std::endl;
}

void Random(int aArr[], int aSize) {
    srand(static_cast<unsigned>(time(0)));

    for (int i = 0; i < aSize; i++) {
        aArr[i] = std::rand() % 10 + 1;
    }
}

int main() {
    const int ArrSize = 100*1000;
    int Arr[ArrSize];
    Random(Arr, ArrSize);
    SpeedAll(Arr, ArrSize, 3, 1*1000);

    return 0;
}
