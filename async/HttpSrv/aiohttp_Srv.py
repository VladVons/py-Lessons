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

    async def rGetIndex(self, aRequest) -> web.Response:
        self.Cnt += 1
        #Name = aRequest.match_info.get('name')
        Data = {
            'cnt': self.Cnt, 
            'method': aRequest.method, 
            'path': aRequest.path, 
            'path_qs': aRequest.path_qs, 
            'query_string': aRequest.query_string,
            'host': aRequest.host, 'remote': aRequest.remote, 
            'forwarded': aRequest.headers.get('X-FORWARDED-FOR', None)
        }
        Msg = [f'{Key}: {Val}' for Key, Val in Data.items()]
        Msg = ['urls:', '/', '/post/json', '/post/text', ''] + Msg
        print('\n'.join(Msg))
        return web.Response(content_type = 'text/html', text = '<br>'.join(Msg))

    async def rGetPath(self, aRequest) -> web.Response:
        self.Cnt += 1
        print('rGetPath()')
        return await self.rGetIndex(aRequest)

    async def rPostJson(self, aRequest) -> web.json_response:
        self.Cnt += 1
        Post = await aRequest.json()
        Data = {
            'cnt': self.Cnt
        }
        Data.update(Post)

        Msg = [f'{Key}: {Val}' for Key, Val in Data.items()]
        print('\n'.join(Msg))
        return web.json_response(data = Data)

    async def rPostText(self, aRequest) -> web.Response:
        self.Cnt += 1
        Post = await aRequest.read()
        Data =  'Replay: ' + Post.decode('utf-8')
        print(Data)
        return web.Response(text = Data)

    async def Run(self, aPort: int):
        App = web.Application()
        App.add_routes([web.post('/post/json', self.rPostJson)])
        App.add_routes([web.post('/post/text', self.rPostText)])
        App.add_routes([web.get('/get/path', self.rGetPath)])
        App.add_routes([web.get('/{name:.*}', self.rGetIndex)])

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
    WebSrv1 = TWebSrv().Run(8070)
    WebSrv2 = TWebSrv().Run(8071)
    Task2 = asyncio.create_task(ProveA())
    await asyncio.gather(WebSrv1, WebSrv2, Task2)
    #await asyncio.gather(WebSrv1)

asyncio.run(Main())
