#!/usr/bin/python3 -B

from SimpleDict import TSimpleDict


def Test():
    Dict = TSimpleDict()                                       # створити клас і виклик його __init__()
    Dict.LoadFile('test.dic')
    #Dict.LoadFile('eng-ukr-computer.dic')

    print()
    print('eng-ukr:')
    Dict.Show('three')                                         # переклад 2. одного слова
    Dict.Show('boy')
    Dict.Show('dog')

    print()
    print('Adding dog = собака')
    Dict.SetWord('dog', 'собака')

    Dict.SetDict(False)                                        # встановити укр словник

    print()
    print('ukr-eng:')
    Words = ['три', 'хлопець', 'собака']                        # переклад 3. списку слів
    for Word in Words:
        Dict.Show(Word)

    print()
    print('All words sorted:')
    Dict.ShowAll()                                             # показати просортований і очищений словник

    print()
    print('Create sorted dictionary file:')
    Dict.SaveFile('test-sorted.dic')                           # зберегти у файл просортований і очищений словник

Test()
