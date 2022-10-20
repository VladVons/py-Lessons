'''
Python lesson
e=mv**2/2
VladVons@gmail.com, 2022.09.15
'''


import math


class TBody():
    def __init__(self, aMass: float):
        self.Mass = aMass

    def GetEnergy(self, aSpeed: float) -> float:
        return self.Mass * (aSpeed ** 2) / 2

    def GetSpeed(self, aEnergy: float) -> float:
        return math.sqrt(2 * aEnergy / self.Mass)


# km/h -> m/s
Speed1 = 120 / (3600 / 1000)

Body1 = TBody(5.0)
Energy1 = Body1.GetEnergy(Speed1)
print('1) Mass kg: %f, Speed m/s: %d, Energy j: %d' % (Body1.Mass, Speed1, Energy1))

Body2 = TBody(0.01)
Speed2 = Body2.GetSpeed(Energy1)
print('2) Mass kg: %f, Speed m/s: %d, Energy j: %d' % (Body2.Mass, Speed2, Energy1))
