#!/usr/bin/micropython


import uasyncio as asyncio

async def bar():
    #await asyncio.sleep(0)
    q1 = 1/0  # Crash

async def foo():
    #await asyncio.sleep(0)
    print('Running bar')
    await bar()
    print('Does not print')  # Because bar() raised an exception

async def main():
    asyncio.create_task(foo())
    for i in range(5):
        print('Working', i)  # Carries on after the exception
        await asyncio.sleep(1)
    q1 = 1/0  # Stops the scheduler
    await asyncio.sleep(0)
    print('This never happens')
    await asyncio.sleep(0)

asyncio.run(main())
