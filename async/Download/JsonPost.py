import asyncio
import aiohttp
import json


async def Send1(aUrl: str, aData: dict):
    print('Send1()', aData)
    async with aiohttp.ClientSession() as Session:
        async with Session.post(
            aUrl,
            #data=json.dumps(aData), 
            data=aData, 
        ) as Response:
            Data = await Response.json()
            print('response', Data)

async def Send2(aUrl: str, aData: dict):
    print('Client Send2()', aData)
    async with aiohttp.ClientSession() as Session:
        async with Session.post(aUrl, json = aData) as Response:
            Data = await Response.json()
            print('response', Data)

async def Send3(aUrl: str, aData: dict):
    headers = {
        "Content-Type": "application/json"
    }
    auth = aiohttp.BasicAuth('username', 'api_key')

    #headers = None
    async with aiohttp.ClientSession(
        headers = headers,
        auth = auth
    ) as Session:
        async with Session.post(
            aUrl,
            json = aData,
            #data=aData, 
            #headers = headers
        ) as Response:
            #Data = await Response.read()
            #Data = await Response.text()
            Data = await Response.json()
            print('response', Data)

async def Run():
    #Url = 'http://localhost/api/test:8080'
    Url = 'http://localhost:8081/get_task'

    for i in range(100):
        Data = {'str': 'hello', 'int': i, 'bool': True}
        await Send2(Url, Data)
        await asyncio.sleep(3)

asyncio.run(Run())

