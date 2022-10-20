#!/usr/bin/micropython

import uasyncio as asyncio


#async def foo():
async def foo():
    while True:
        print('In foo')
        await asyncio.sleep(1)
        #yield from asyncio.sleep(1)


async def bar():
    foo_task = asyncio.create_task(foo())  # Create task from task
    #await asyncio.gather(foo_task)

    await asyncio.sleep(5)  # Show it running
    foo_task.cancel()
    #await asyncio.sleep(0)
    print('foo is now cancelled. wait 4 for proof')
    await asyncio.sleep(4)  # Proof!

asyncio.run(bar())
