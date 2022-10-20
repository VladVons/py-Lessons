#!/usr/bin/python3

import asyncio


class TEvent():
    def __init__(self, aParent):
        #self.Parent = aParent
        self.Event = asyncio.Event()

    async def Waiter1(self, aId):
        while True:
            print('Waiter A', aId)
            await self.Event.wait()
            print('Waiter B', aId)

            await asyncio.sleep(1)

    async def Waiter2(self):
        Cnt = 0

        while True:
            Cnt += 1
            if (Cnt % 2 == 0): 
                print('Waiter2 set')
                self.Event.set()
            else:
                print('Waiter2 clear')
                self.Event.clear()
            await asyncio.sleep(5)


class TMain():
    def __init__(self):
        self.Event = asyncio.Event()

    async def Main(self):
        Event = TEvent(self)
        asyncio.create_task(Event.Waiter2())
        Tasks = [asyncio.create_task(Event.Waiter1(i)) for i in range(3)]
        await asyncio.gather(*Tasks)


asyncio.run(TMain().Main())

