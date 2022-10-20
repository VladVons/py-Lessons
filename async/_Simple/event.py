#!/usr/bin/python3

import time
import asyncio

event = asyncio.Event()

async def waiter():
    print('Waiting for event')
    await event.wait()  # Pause here until event is set

    print('Waiter got event.')
    event.clear()  # Flag caller and enable re-use of the event

async def main():
    asyncio.create_task(waiter())

    print('time.sleep(2)')
    time.sleep(2)

    print('Clear')
    event.clear()

    print('Waiting 5 sec')
    await asyncio.sleep(5)

    print('Setting event')
    event.set()

    await asyncio.sleep(1)
    # Caller can check if event has been cleared
    print('Event is {}'.format('set' if event.is_set() else 'clear'))

asyncio.run(main())
