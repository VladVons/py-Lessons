# Created: 2022.04.11
# Author: Vladimir Vons <VladVons@gmail.com>
# License: GNU, see LICENSE for more details


def FilterKeyErr(aData: dict, aAsStr: bool = False) -> list:
    def _FilterKey(aData: object, aRes: list):
        if (isinstance(aData, dict)):
            for Key, Val in aData.items():
                _FilterKey(Val, aRes)
                if (Key == 'type') and (Val == 'err'):
                    aRes.append(aData.get('data'))
                elif (Key == 'err'):
                    aRes.append(aData.get('err'))

    Res = []
    _FilterKey(aData, Res)
    if (aAsStr):
        Res = ', '.join([str(x) for x in Res])
    return Res
