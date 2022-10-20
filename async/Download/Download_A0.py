'''
python async example
VladVons@gmail.com
2022.04.20
'''

import asyncio
import aiohttp


async def GetUrlJson(aUrl: str):
    async with aiohttp.ClientSession() as Session:
        async with Session.get(aUrl) as Response:
            return await Response.json()

async def Task_1():
    Url = 'https://random-data-api.com/api/address/random_address'
    while True:
        Data = await GetUrlJson(Url)
        print('Task_1', 'Country: %s, City: %s, Street %s' % (Data['country'], Data['city'], Data['street_name']))
        await asyncio.sleep(3)

async def Task_2():
    Cnt = 0
    while True:
        Cnt += 1
        print('Task_2', Cnt)
        await asyncio.sleep(1)

async def Main():
    print('Welcome to python async !')
    await asyncio.gather(Task_1(), Task_2())

asyncio.run(Main())
