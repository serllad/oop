import asyncio

@asyncio.coroutine
def hello():
    print('hello world')
    r=yield from asyncio.sleep(1)
    print('hello again')

l=asyncio.get_event_loop()
tasks=[hello(),hello()]
l.run_until_complete(asyncio.wait(tasks))
l.close()
