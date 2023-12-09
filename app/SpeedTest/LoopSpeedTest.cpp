#include <iostream>
#include <vector>
#include <ctime>
#include <cstdlib>
#include <algorithm>


int Test_01(const std::vector<int>& aArr, int aFind) {
    int Res = 0;
    for (size_t i = 0; i < aArr.size(); ++i) {
        if (aArr[i] == aFind) {
            Res += 1;
        }
    }
    return Res;
}

int Test_02(const std::vector<int>& aArr, int aFind) {
    auto it = std::count(aArr.begin(), aArr.end(), aFind);
    return static_cast<int>(it);
}

int Test_03(const std::vector<int>& aArr, int aFind) {
    int Res = 0;
    for (int a : aArr) {
        if (a == aFind) {
            Res += 1;
        }
    }
    return Res;
}

int Test_04(const std::vector<int>& aArr, int aFind) {
    auto it = std::count(aArr.begin(), aArr.end(), aFind);
    return static_cast<int>(it);
}

void SpeedFunc(int (*aFunc)(const std::vector<int>&, int), const std::vector<int>& aArr, int aFind, int aCount) {
    clock_t Start = clock();
    int Res = 0;
    for (int a = 0; a < aCount; ++a) {
        Res = aFunc(aArr, aFind);
    }
    std::cout << "Method: " << aFunc << ", Time: " << static_cast<double>(clock() - Start) / CLOCKS_PER_SEC << ", Found: " << Res << std::endl;
}

void SpeedAll(const std::vector<int>& aArr, int aFind, int aCount) {
    std::cout << std::endl;
    std::cout << "C++ ver" << std::endl;

    clock_t Start = clock();
    int (*Methods[])(const std::vector<int>&, int) = { Test_01, Test_02, Test_03, Test_04 };
    for (auto Method : Methods) {
        SpeedFunc(Method, aArr, aFind, aCount);
    }
    std::cout << "Total: " << static_cast<double>(clock() - Start) / CLOCKS_PER_SEC << std::endl;
}

int main() {
    srand(static_cast<unsigned>(time(0)));
    std::vector<int> Arr1(100);
    std::generate(Arr1.begin(), Arr1.end(), []() { return rand() % 10 + 1; });

    SpeedAll(Arr1, 3, 1 * 1000000);
    return 0;
}
