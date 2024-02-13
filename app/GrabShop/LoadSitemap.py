# Created: 2024.02.13
# Author: Vladimir Vons <VladVons@gmail.com>
# License: GNU, see LICENSE for more details


import asyncio
#
from Lib.SiteMap import TSiteMap

async def GetUrls(aUrl: str):
    SiteMap = TSiteMap()
    Urls = await SiteMap.LoadSiteMap(aUrl)
    with open('urls.txt', 'w') as F:
        Data = '\n'.join(Urls)
        F.write(Data)

async def Save(aUrl: str):
    SiteMap = TSiteMap()
    await SiteMap.SaveSiteMap(aUrl)

async def Run():
    Url = 'https://darstar.com.ua/sitemaps/products/sitemap_ru.xml'
    #await GetUrls(Url)
    await Save(Url)

asyncio.run(Run())
