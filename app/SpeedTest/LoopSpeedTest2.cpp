#include <iostream>
#include <ctime>
#include <cstdlib>


void Random(int aArr[], int aSize) {
    for (int i = 0; i < aSize; i++) {
        aArr[i] = std::rand() % 10 + 1;
    }
}

int Test_01(int aArr[], int aSize, int aFind) {
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

int Test_02(int aArr[], int aSize, int aFind) {
    int Res = 0;
    for (int i = 0; i < aSize; i++) {
        if (aArr[i] == aFind) {
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
    std::cout << std::endl;
    std::cout << "C++" << std::endl;

    clock_t Start = clock();
    int (*Methods[])(int aArr[], int aSize, int aFind) = { Test_01, Test_02, Test_01, Test_02};
    for (auto Method : Methods) {
        SpeedFunc(Method, aArr, aSize, aFind, aCount);
    }
    std::cout << "Total: " << static_cast<double>(clock() - Start) / CLOCKS_PER_SEC << std::endl;
}

int main() {
    const int ArrSize = 100;
    int Arr[ArrSize];
    Random(Arr, ArrSize);
    SpeedAll(Arr, ArrSize, 3, 1000000);

    return 0;
}
