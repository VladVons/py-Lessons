'''
Pyrhon Example
Class extender

VladVons@gmail.com
2023.01.28
'''


from Lib import Decor_AddModules
import Main_Extender


@Decor_AddModules([Main_Extender])
class TMain():
    def __init__(self):
        self.Greet = 'Hello'

    def ShowGreet(self):
        print(self.Greet)

    def ShowGreetLang(self):
        print(self.Greet, self.Lang, '!')


Main = TMain()
Main.ShowGreet()
Main.ShowLang()
Main.ShowGreetLang()
