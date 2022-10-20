import asyncio
import aiohttp
import json
from flask import Flask

app = Flask(__name__)


async def GetImages(aSession, aTaskId):
    Url = 'http://xkcd.com/%d/info.0.json' % (aTaskId)
    async with aSession.get(Url) as Response:
        Data = (await Response.read()).decode()
        return (Data, aTaskId)


@app.get('/test')
async def uTest():
    Res = ''
    async with aiohttp.ClientSession() as Session:
        Tasks = [GetImages(Session, i) for i in range(1, 20)]
        Arr = await asyncio.gather(*Tasks, return_exceptions=not True)
        for iA1, iA2 in Arr:
            Data = json.loads(iA1)
            Res += '<img src="%s">%s - %d</img><br>' % (Data['img'], Data['title'], iA2)
    return Res


if __name__ == '__main__':
    #from waitress import serve
    #serve(app, host="0.0.0.0", port=8000)

    app.run(debug=True, port=8000)
