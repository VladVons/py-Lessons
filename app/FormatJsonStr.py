'''
Python lesson. 
Format lines on brackets [] {}
VladVons@gmail.com, 2022.04.14
'''

def FormatJsonStr(aScript: str, aPad: int = 2, aChar: str = ' ') -> str:
    Res = []
    Level = 0
    Lines = aScript.splitlines()
    for Line in Lines:
        Line = Line.strip()
        if (Line):
            if (Line[-1] in ['{', '[']):
                Spaces = Level * aPad
                Level += 1
            elif (Line[0] in ['}', ']']):
                Level -= 1
                Spaces = Level * aPad
            else:
                Spaces = Level * aPad
            Res.append((aChar * Spaces) + Line)
    return '\n'.join(Res)


Str1 = '''
    "_Items": {
"Name": [
["find", ["h1"]],
["find", ["bdi"]],
["text"]
    ],
    "Price": [
["find", ["span", {"class": "ty-price"}]],
["text"],
    ["Price"]
]
}
'''

Str2 = FormatJsonStr(Str1)
print(Str2)
