import pygame


def Run():
    ScreenColor = (200,200,20)
    ScreenWidth = 1024
    ScreenHeight = 768

    pygame.init()
    pygame.display.set_caption('Snake')
    Screen = pygame.display.set_mode([ScreenWidth, ScreenHeight])

    BallWidth = 40
    BallHeight = 20
    BallX = (ScreenWidth - BallWidth) / 2
    BallY = (ScreenHeight - BallHeight) / 2
    BallSpeed = 5

    Screen.fill(ScreenColor)
    pygame.display.update()

    IsRun = True
    while (IsRun):
        pygame.time.delay(10)
        Screen.fill(ScreenColor)

        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                IsRun = False
            #if (event.type in [pygame.KEYDOWN, pygame.KEYUP]):

        Keys = pygame.key.get_pressed()
        if (Keys[pygame.K_ESCAPE]):
            IsRun = False
        elif (Keys[pygame.K_LEFT]) and (BallX > 0):
            BallX -= BallSpeed
        elif (Keys[pygame.K_RIGHT]) and (BallX < ScreenWidth - BallWidth):
            BallX += BallSpeed

        pygame.draw.rect(Screen, (255, 0, 0), (BallX, BallY, BallWidth, BallHeight))

        pygame.display.update()

    pygame.quit()


Run()
