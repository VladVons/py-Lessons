#!/usr/bin/env python3


import asyncio

async def Test():
    print('forever')
    while True:
        await asyncio.sleep(0)
        #await asyncio.sleep(0.001)

asyncio.run(Test())
