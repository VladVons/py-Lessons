'''
python async loop example
VladVons@gmail.com
2022.05.29
'''


import asyncio
import aiohttp


async def TaskA(aSleep: int):
    await asyncio.sleep(aSleep)
    print('TaskA(%s) start' % aSleep)

    Counter = 0
    while True:
        Counter += 1
        print('TaskA(%s) loop' % aSleep, Counter)
        await asyncio.sleep(aSleep)

async def TaskB(aType: str):
    Url = 'https://loremflickr.com/800/600/%s' % aType
    Counter = 0
    while True:
        try:
            async with aiohttp.ClientSession() as Session:
                async with Session.get(Url) as Response:
                    Data = await Response.read()
        except Exception as E:
            print('Error', E)
            break 
            
        Counter += 1
        File = 'image_%s_%03d.jpg' % (aType, Counter)
        print('Save', Url, File)
        with open(File , 'wb') as F:
            F.write(Data)
        await asyncio.sleep(1)


async def Main():
    ImageType = ['python', 'dog', 'cat', 'girl', 'boy', 'tree', 'beer', 'smile', 'bird', 'war', 'moon', 'sun', 'star']
    Tasks = []
    for i in range(len(ImageType)):
        Tasks.append(asyncio.create_task(TaskA(i+1)))
        Tasks.append(asyncio.create_task(TaskB(ImageType[i])))
    await asyncio.gather(*Tasks)

asyncio.run(Main())
