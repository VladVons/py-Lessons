'''
Pyrhon example
__repr__

vladvons@gmail.com
2022.06.07
'''


class TStarsA():
    def __init__(self, aCount: int):
        self.Count = aCount


class TStarsB():
    def __init__(self, aCount: int):
        self.Count = aCount

    def __repr__(self):
        Res = ['*' * i for i in range(self.Count)]
        return '\n'.join(Res)


StarsA = TStarsA(10)
print(StarsA)

StarsB = TStarsB(10)
print(StarsB)
