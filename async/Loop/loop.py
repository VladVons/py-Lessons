'''
python async loop example
VladVons@gmail.com
2022.05.29
'''


import asyncio

async def TaskA(aSleep: int):
    await asyncio.sleep(aSleep)
    print('TaskA(%s) start' % aSleep)

    Counter = 0
    while True:
        Counter += 1
        print('TaskA(%s) loop' % aSleep, Counter)
        await asyncio.sleep(aSleep)


async def Main(aMaxTasks: int):
    Tasks = []
    for i in range(1, aMaxTasks):
        Tasks.append(asyncio.create_task(TaskA(i)))
    await asyncio.gather(*Tasks)

asyncio.run(Main(10))
