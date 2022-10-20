#!/usr/bin/python3 -B

import random
from SimpleDict import TLearnDict


def Learn():
    Dict = TLearnDict()
    #Dict.LoadFile('eng-ukr.dic')
    #Dict.LoadFile('eng-ukr-computer.dic')

    SetA = ['-eng-ukr.dic', 'eng-ukr-computer.dic']
    Dict.LoadFiles(SetA)

    print()
    Dict.Info()

    Mode = bool(random.getrandbits(1))
    Dict.SetDict(Mode)

    print('Random words:')
    Dict.ShowRand(10)

    print()
    Dict.Learn(5, 10)

Learn()
