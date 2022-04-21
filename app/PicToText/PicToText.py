'''
Python lesson
picture to ASCII
VladVons@gmail.com, 2022.04.21
'''

import PIL.Image


def LoadFile(aFile: str, aWidth: int = 120) -> str:
    Img = PIL.Image.open(aFile)

    Width, Height = Img.size
    Ratio = Height / Width
    NewHeight = Ratio * aWidth * 0.6
    Img = Img.resize((aWidth, int(NewHeight)))
    GrayScale = Img.convert('L')
    Pixels = GrayScale.getdata()

    #Chars = 'DavidVons20@7=*+,.'
    Chars = 'DavidVons20@7'
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

File = 'cup_of_coffee.jpg'
Text = LoadFile(File, 160)
FileOut = File + '.txt'
with open(FileOut, 'w') as F:
    F.write(Text)
print('Saved to', FileOut)
