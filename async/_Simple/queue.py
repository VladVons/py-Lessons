#!/usr/bin/python3 -B

import asyncio
import random
import time


async def worker(name, queue):
    print('Start', name)

    Cnt = 0
    while True:
        print(f'worker loop begin {name}')

        # Get a "work item" out of the queue.
        sleep_for = await queue.get()

        # Sleep for the "sleep_for" seconds.
        await asyncio.sleep(sleep_for)

        # Notify the queue that the "work item" has been processed.
        queue.task_done()

        print(f'worker loop end {name} waits {sleep_for:.2f}')

        Cnt += 1
        if (Cnt % 2 == 0):
            #queue.put_nowait(3)
            pass
    print('Finish', name)

async def main():
    global IsRun

    # Create a queue that we will use to store our "workload".
    queue = asyncio.Queue()
    print('max size', queue.maxsize)

    # Generate random timings and put them into the queue.
    total_sleep_time = 0
    for _ in range(10):
        sleep_for = random.uniform(0.05, 1.0)
        total_sleep_time += sleep_for
        queue.put_nowait(sleep_for)
        #queue.put(sleep_for)

    # Create three worker tasks to process the queue concurrently.
    tasks = []
    for i in range(3):
        task = asyncio.create_task(worker(f'{i}', queue))
        tasks.append(task)

    # Wait until the queue is fully processed.
    started_at = time.monotonic()
    await queue.join()
    total_slept_for = time.monotonic() - started_at

    # Cancel our worker tasks.
    print('cancel task')
    for task in tasks:
        task.cancel()

    print('====')
    print(f'3 workers slept in parallel for {total_slept_for:.2f} seconds')
    print(f'total expected sleep time: {total_sleep_time:.2f} seconds')


asyncio.run(main())
