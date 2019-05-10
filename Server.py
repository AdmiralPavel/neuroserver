import asyncio
from aiohttp import web, MultipartReader
import ssl
 
host = 'localhost'
port = '8080'
 
# Это обработчик входящих запросов  
async def foo(request):
    reader = MultipartReader.from_response(request)
    while True:
        part = await reader.next()
        if part is None:
            break
 
        if part.name == 'file':
            contents = await part.read() #Тута вся твоя инфа
            resp = asyncio.run_in_executor(None, bar, contents)
           
   
    return web.Response(text=resp)
 
# Это обработчик изображений (твоя нейросеть)
def bar(contents):
    #contents - байты изображения
    return "Я тут наанализировал что Паша лох"
                           
app = web.Application()
app.router.add_post('/handle', foo)
 
web.run_app(app, host=host, port=port)
