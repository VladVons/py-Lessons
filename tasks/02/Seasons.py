'''
vladvons@gmail.com
2022.06.08

Python Example
use input() function to get month number in a range from 1 to 12 and show its season name
conditions are:
3, 4, 5 - spring
6, 7, 8 - summer
9, 10, 11 - autumn
12, 1, 2 - winter

'''


class TYear():
    def __init__(self):
        self.Seasons = {
            'spring': [3, 4, 5],
            'summer': [6, 7, 8],
            'autumn': [9, 10, 11],
            'winter': [12, 1, 2]
        }

    def SeasonToMonth(self, aSeason: str) -> list:
        return self.Seasons.get(aSeason.lower(), 'unknown %s' % aSeason)

    def MonthToSeason(self, aMonth: int) -> str:
        for Key, Value in self.Seasons.items():
            if (aMonth in Value):
                return Key

    def AskSeason(self):
        while (True):
            Month = input('Enter a month number: ')
            if (Month == ''):
                print('Quit')
                break
            if (Month.isdigit()):
                Season = self.MonthToSeason(int(Month))
                if (Season):
                    print('Month %s is in %s' % (Month, Season))
                else:
                    print('Invalid month %s' % Month)
            else:
                print('Month must be a digit')


Year = TYear()
print(Year.MonthToSeason(10))

print(Year.SeasonToMonth('summer'))
print(Year.SeasonToMonth('SummeR'))
print(Year.SeasonToMonth('Magadan`'))

Year.AskSeason()
