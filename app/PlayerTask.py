#!/usr/bin/env python3
'''
2022.01.27, vladvons@gmail.com
'''

import random


class TPlayerTask():
    def __init__(self, aStart: int, aEnd: int, aPlayers: int) -> None:
        self.Start: int = aStart
        self.End: int = aEnd
        self.Players: int = aPlayers

        self.Randomize()

    def Randomize(self):
        Arr: list = range(self.Start, self.End)
        self.Tasks = random.sample(Arr, self.End - self.Start)

    def PrintA(self) -> None:
        for Idx, Task in enumerate(self.Tasks):
            Player: int = (Idx % self.Players) + 1
            print('Player %s, Task %2d' % (Player, Task))
            if (Player == self.Players):
                print()

    def PrintB(self) -> None:
        Res: list = [[] for i in range(self.Players)]
        for Idx, Task in enumerate(self.Tasks):
            Player: int = (Idx % self.Players)
            Res[Player].append(Task)

        for Idx, Task in enumerate(Res):
            print('Player %s, Tasks %s' % (Idx + 1, sorted(Task)))

def PrintB(aStart, aEnd, aPlayers):
    Arr = range(aStart, aEnd)
    Tasks = random.sample(Arr, aEnd - aStart)

    Res = [[] for i in range(aPlayers)]
    for Idx, Task in enumerate(Tasks):
        Player: int = (Idx % aPlayers)
        Res[Player].append(Task)

    for Idx, Task in enumerate(Res):
        print('Player %s, Tasks %s' % (Idx + 1, sorted(Task)))


print()
#PlayerTask = TPlayerTask(1, 16, 3)

#PlayerTask.PrintA()
#print()
#PlayerTask.PrintB()

#print('---')
PrintB(1, 16+1, 2)
