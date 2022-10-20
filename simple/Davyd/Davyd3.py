class TRectangle():
    def __init__(self, aWidth: float = 0, aLenght: float = 0):
        self.Width = aWidth
        self.Length = aLenght
        
    def GetSquare(self):
        Res = self.Width * self.Length
        return Res

    def GetPerimeter(self):
        Res = 2 * (self.Width + self.Length) 
        return Res

    def ShowSquare(self):
        Res = self.GetSquare()
        print(Res)

    def ShowPerimeter(self):
        Res = self.GetPerimeter()
        print('Perimeter: %s ' % (Res))


Rect1 = TRectangle(20, 10)
Rect1.ShowSquare()
Rect1.ShowPerimeter()

Rect1.Width = 30
Rect1.Length = 40
Rect1.ShowSquare()
Rect1.ShowPerimeter()


Rect2 = TRectangle(5, 6)
#Rect2.Width = 5
#Rect2.Length = 6
print(Rect1.GetSquare() + Rect2.GetSquare())