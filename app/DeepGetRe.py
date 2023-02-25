# VladVons@gmailcom
# 2023.01.24

import re

def DeepGetRe(aObj, aKeys: list, aWithPath: bool = True) -> list:
    RegExSign = '.*+^$[({'

    def Recurs(aObj, aKeys: list, aPath: str) -> list:
        Res = []
        if (aKeys):
            Type = type(aObj)
            if (Type == dict):
                Key = aKeys[0]
                if (any(x in RegExSign for x in Key)):
                    for xKey in aObj:
                        if (re.match(Key, xKey)):
                            Res += Recurs(aObj.get(xKey), aKeys[1:], f'{aPath}.{xKey}')
                else:
                    Val = aObj.get(Key)
                    if (Val is not None):
                        Res += Recurs(Val, aKeys[1:], f'{aPath}.{Key}')
            elif (Type in [list, tuple, set]):
                for Idx, Val in enumerate(aObj):
                    Res += Recurs(Val, aKeys, f'{aPath}[{Idx}]')
        else:
            if (aWithPath):
                Res.append((aObj, aPath.lstrip('.')))
            else:
                Res.append(aObj)
        return Res
    return Recurs(aObj, aKeys, '')


Data = {
    'ref_product': [
        {
            'image': 'pic1.jpg',
            'sort_order': 1,
            'test1': {
                'test2': 3
            },
        },
        {
            'image': 'pic2.jpg',
            'sort_order': 2
        },
        {
            'image_top': 'pic_top.jpg',
            'sort_order': 9
        },
        'hello',
        '123'
    ]
}

print()
Arr = DeepGetRe(Data, ['ref_product', 'image.*'])
for x in Arr:
    print(x)

print()
Arr = DeepGetRe(Data, ['ref_product', 'test1', 'test2'], False)
for x in Arr:
    print(x)
