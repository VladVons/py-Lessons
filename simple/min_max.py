def MyFunc(aMsg: str, aIdx: int) -> str:
    Arr = ["zero", "one", "two", "three"]
    Idx = min(max(0, aIdx), len(Arr) - 1)
    Res = "%s %s" % (aMsg, Arr[Idx])
    return Res

Res = MyFunc("Digit:", 2)
print(Res)
