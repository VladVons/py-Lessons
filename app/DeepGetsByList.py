# VladVons@gmailcom
# 2023.01.24

def DeepGetsByList(aObj, aKeys: list, aWithPath: bool = True) -> list:
    def Recurs(aObj, aKeys: list, aPath: str) -> list:
        Res = []
        if (aKeys):
            Type = type(aObj)
            if (Type == dict):
                Val = aObj.get(aKeys[0])
                if (not Val is None):
                    Res += Recurs(Val, aKeys[1:], f'{aPath}.{aKeys[0]}')
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
            }
        },
        {
            'image': 'pic2.jpg',
            'sort_order': 2
        },
        {
            'image_top': 'pic_top.jpg',
            'sort_order': 12
        },
        'hello',
        '123'
    ]
}

print()
Arr = DeepGetsByList(Data, ['ref_product', 'image'])
print(Arr)
print()
Arr = DeepGetsByList(Data, ['ref_product', 'test1', 'test2'], False)
print(Arr)
