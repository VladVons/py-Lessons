#!/usr/bin/micropython

import uasyncio as asyncio

async def eternity():
    # Sleep for one hour
    await asyncio.sleep(30)
    print('yay!')

async def main():
    print('Wait for at most 2 second')
    try:
        await asyncio.wait_for(eternity(), timeout=2)
    except asyncio.TimeoutError:
        print('timeout!')

asyncio.run(main())
