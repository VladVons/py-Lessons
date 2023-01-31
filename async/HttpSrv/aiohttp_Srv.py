'''
python async example
VladVons@gmail.com
2021.03.02
'''


import asyncio
from aiohttp import web


async def ProveA():
    Loops = 0
    while True:
        Loops += 1
        print('ProveA 3s', Loops)
        await asyncio.sleep(3)


class TWebSrv():
    def __init__(self):
        self.Cnt = 0

    async def rHello(self, aRequest):
        self.Cnt += 1
        return web.Response(text = f'Hello, world {self.Cnt}')

    async def Run(self, aPort: int):
        App = web.Application()
        App.add_routes([web.get('/', self.rHello)])

        Runner = web.AppRunner(App)
        try:
            await Runner.setup()
            print('Listen port', aPort)
            Site = web.TCPSite(Runner, host = '0.0.0.0', port = aPort)
            await Site.start()
            while (True):
                await asyncio.sleep(60)
        finally:
            await Runner.cleanup()

async def Main():
    WebSrv1 = TWebSrv().Run(8080)
    WebSrv2 = TWebSrv().Run(8081)
    Task2 = asyncio.create_task(ProveA())
    await asyncio.gather(WebSrv1, WebSrv2, Task2)

asyncio.run(Main())
