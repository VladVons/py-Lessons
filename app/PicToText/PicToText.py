'''
Python lesson
picture to ASCII
VladVons@gmail.com, 2022.04.21
'''

import random
import PIL.Image


def GetRandStr(aLen: int) -> str:
    Ascii = [chr(i) for i in range(33, 126)]
    Rand = random.sample(Ascii, aLen)
    return ''.join(Rand)

def LoadFile(aFile: str, aWidth: int = 150) -> str:
    Img = PIL.Image.open(aFile)

    Width, Height = Img.size
    Ratio = Height / Width
    NewHeight = Ratio * aWidth * 0.45
    Img = Img.resize((aWidth, int(NewHeight)))
    GrayScale = Img.convert('L')
    Pixels = GrayScale.getdata()

    #Chars = gscale1 = '@%#*+=-:. '
    Chars = 'DavidVons20@7=*+,.'
    #Chars = GetRandStr(20)
    print(Chars)

    Ratio = 255 / (len(Chars) - 1)
    Pixels = GrayScale.getdata()
    Arr = []
    for Pixel in Pixels:
        Idx = int(Pixel / Ratio)
        Char = Chars[Idx]
        Arr.append(Char)

    StrPixels = ''.join(Arr)
    StrLen = len(StrPixels)
    Arr = []
    for Idx in range(0, StrLen, aWidth):
        Line = StrPixels[Idx : Idx + aWidth]
        Arr.append(Line)
    Res = '\n'.join(Arr)
    return Res

def SaveFile(File: str, aData):
    with open(FileOut, 'w') as F:
        F.write(aData)

if (__name__ == '__main__'):
    File = 'cup_of_coffee.jpg'
    Text = LoadFile(File, 100)

    FileOut = File + '.txt'
    SaveFile(FileOut, Text)
    print('Saved to', FileOut)
