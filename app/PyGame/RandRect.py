#!/usr/bin/python3 -B


'''
Python lesson
Simple pygame example
VladVons@gmail.com, 2022.02.11

ToDo:
https://www.geeksforgeeks.org/collision-detection-in-pygame/
'''


import pygame
import random


class TColor():
    def __init__(self, aStep: int = 64):
        self.Values = [i for i in range(0, 255, aStep)]
        self.Values.append(255)
        self.Values *= 2

    def GetRandSolid(self) -> tuple:
        random.shuffle(self.Values)
        Res = tuple(self.Values[:3])
        return Res

    def GetRand() -> tuple:
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

gColor = TColor(128)


class TOptions():
    def __init__(self):
        self.Version: str = 'Pygame rectangle 1.01'

        self.BgColor: tuple = (100, 100, 100)
        self.ScreenWidth: int = 640
        self.ScreenHeight: int = 480

        self.ObjInc: int = 10
        self.ObjMinSize: int = 20
        self.ObjMaxSize: int = 100
        self.ObjMaxSpeed: int = 10

        self.DeadLineX = 50
        self.DeadLineColor = (255, 0, 0)


class TGame():
    def __init__(self, aOptions: TOptions):
        self.Options: TOptions = aOptions
        self.Objects: list[TObj] = []
        self.Bullets: list[TBullet] = []

    def Init(self):
        pygame.init()
        pygame.display.set_caption(self.Options.Version)
        self.ScreenSurf = pygame.display.set_mode([self.Options.ScreenWidth, self.Options.ScreenHeight])

    def Objects_SetRand(self):
        for Obj in self.Objects:
            Obj.Width = random.randint(self.Options.ObjMinSize, self.Options.ObjMaxSize)
            Obj.Height = random.randint(self.Options.ObjMinSize, self.Options.ObjMaxSize)
            Obj.Speed = random.randint(2, self.Options.ObjMaxSpeed)
            Obj.Color = gColor.GetRandSolid()

            X = random.randint(self.Options.DeadLineX, self.Options.ScreenWidth)
            Y = random.randint(self.Options.DeadLineX, self.Options.ScreenHeight)
            Obj.SetPos(X , Y)
            #Obj.SetCenter(random.randint(-200, 200), random.randint(-200, 200))

    def Objects_Add(self, aCount: int = 1):
        Classes = (TRect, TEllipse)
        for i in range(aCount):
            Obj = random.choice(Classes)(self)
            self.Objects.append(Obj)

    def ShowText(self, aPos: tuple, aMsg: str):
        Font = pygame.font.SysFont('Comic Sans MS', 50)
        TextR = Font.render(aMsg, False, gColor.GetRandSolid())
        self.ScreenSurf.blit(TextR, aPos)

    def Run(self):
        Bullet = TBullet(self)
        Bullet.Init()
        self.Bullets.append(Bullet)


        self.ScreenSurf.fill(self.Options.BgColor)
        pygame.display.update()

        IsRun = True
        while (IsRun):
            pygame.time.delay(10)
            self.ScreenSurf.fill(self.Options.BgColor)
            pygame.draw.line(self.ScreenSurf, self.Options.DeadLineColor, (self.Options.DeadLineX, 0), (self.Options.DeadLineX, self.Options.ScreenHeight), width = 2)

            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    IsRun = False
                elif (event.type == pygame.KEYUP):
                    if (event.key == pygame.K_ESCAPE):
                        IsRun = False
                    elif (event.key == pygame.K_r):
                        self.Objects_SetRand()
                        self.Options.BgColor = gColor.GetRandSolid()
                        print('Event key', chr(event.key), len(self.Objects))
                    elif (event.key == pygame.K_t):
                        self.Objects_Add(self.Options.ObjInc)
                        self.Objects_SetRand()
                        print('Event key', chr(event.key), len(self.Objects))

            Keys = pygame.key.get_pressed()

            for Obj in list(self.Objects):
                if (Obj.X < self.Options.DeadLineX) and (len(self.Objects) > self.Options.ObjInc):
                    self.Objects.remove(Obj)

                Obj.OnKey(Keys)
                Obj.Draw()

            for Obj in self.Bullets:
                Obj.MoveHorCycle()
                Obj.CheckToEat()
                Obj.Draw()

            if (len(self.Objects) == 0):
                self.ShowText((100, 100), 'Super !')
                pygame.display.update()
                pygame.time.delay(1000)
                self.Objects_Add(self.Options.ObjInc)
                self.Objects_SetRand()

            pygame.display.update()

        pygame.quit()


class TObj():
    def __init__(self, aGame: TGame):
        self.Game: TGame = aGame

        self.Width: int = 0
        self.Height: int = 0
        self.Color: tuple = (0, 0, 0)
        self.Speed: float = 1.0
        self.X: int = 0
        self.Y: int = 0

    def SetCenter(self, aX: int = 0, aY: int = 0):
        self.X = ((self.Game.Options.ScreenHeight - self.Width) / 2) + aX
        self.Y = ((self.Game.Options.ScreenHeight - self.Height) / 2) + aY

    def SetPos(self, aX: int, aY: int):
        if (aX > 0) and (aX < self.Game.Options.ScreenWidth - self.Width):
            self.X = aX

        if (aY > 0) and (aY < self.Game.Options.ScreenHeight - self.Height):
            self.Y = aY

    def OnKey(self, aKeys: list):
        if (aKeys[pygame.K_LEFT]):
            self.SetPos(self.X - self.Speed, self.Y)
        elif (aKeys[pygame.K_RIGHT]):
            self.SetPos(self.X + self.Speed, self.Y)
        elif (aKeys[pygame.K_UP]):
            self.SetPos(self.X, self.Y - self.Speed)
        elif (aKeys[pygame.K_DOWN]):
            self.SetPos(self.X, self.Y + self.Speed)

    def Draw(self):
        raise NotImplementedError()


class TRect(TObj):
    def Draw(self):
        pygame.draw.rect(self.Game.ScreenSurf, self.Color, (self.X, self.Y, self.Width, self.Height))


class TEllipse(TObj):
    def Draw(self):
        pygame.draw.ellipse(self.Game.ScreenSurf, self.Color, (self.X, self.Y, self.Width, self.Height))


class TBullet(TEllipse):
    def Init(self):
        self.Width = 50
        self.Height = 5
        self.Y = 200
        self.Speed = 6

    def MoveHorCycle(self):
        self.X += self.Speed
        if (self.X > self.Game.Options.ScreenWidth + self.Width):
            self.X = -self.Width

            Pos = [int(self.Height), int(self.Game.Options.ScreenHeight - self.Height)]
            if (Pos[0] > Pos[1]): Pos[1], Pos[0] = Pos[0], Pos[1]
            self.Y = random.randint(*Pos)

    def IsCollision(self, aObj: TObj ) -> bool:
        MidY = self.Y + self.Height / 2
        return (self.X > aObj.X) and (self.X < aObj.X + aObj.Width) and \
               (MidY > aObj.Y) and (MidY < aObj.Y + aObj.Height)

    def Explose(self):
        Bullet = TBullet(self.Game)
        Bullet.Init()
        Bullet.Speed += 1
        self.Game.Bullets.append(Bullet)

        self.Init()
        self.Game.Objects_Add(self.Game.Options.ObjInc)
        self.Game.Objects_SetRand()

    def CheckToEat(self):
        for Obj in list(self.Game.Objects):
            if (self.IsCollision(Obj)):
                self.Width += Obj.Width / 4
                self.Height += Obj.Height / 4
                self.Color = Obj.Color

                if (self.Speed > 1):
                    self.Speed -= 0.25
                else:
                    self.Explose()

                self.Game.Objects.remove(Obj)

def Run():
    Options = TOptions()
    Options.Color = (150, 150, 50)
    Options.ScreenWidth = 1024
    Options.ScreenHeight = 768

    Game = TGame(Options)
    Game.Init()
    Game.Objects_Add(Game.Options.ObjInc)
    Game.Objects_SetRand()

    Game.Run()


print('Key "r" - randomize')
print('Key "t" - add objects')
 
Run()
