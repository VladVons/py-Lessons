#!/usr/bin/micropython

import uasyncio as asyncio

async def task2(i, lock):
    while 1:
        async with lock:
            print("Acquired lock in task", i)
            await asyncio.sleep(1)

async def task(i, lock):
    while 1:
        await lock.acquire()
        print("Acquired lock in task", i)
        await asyncio.sleep(0.5)
        lock.release()

async def killer():
    await asyncio.sleep(10)

loop = asyncio.get_event_loop()

lock = asyncio.Lock()  # The global Lock instance

loop.create_task(task2(1, lock))
loop.create_task(task2(2, lock))
loop.create_task(task2(3, lock))

loop.run_until_complete(killer())  # работать 10s
