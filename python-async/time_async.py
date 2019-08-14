import time
import asyncio

async def two():
	print('starting two')
	await asyncio.sleep(2)
	print('hey two')
	return 2

async def four():
	print('starting four')
	await asyncio.sleep(4)
	print('hey four')
	return 4

async def main():
	print(await asyncio.gather(two(), four()))

start = time.time()
loop = asyncio.get_event_loop()
# Blocking call which returns when the main() coroutine is done
loop.run_until_complete(main())
loop.close()
print(f'{time.time()-start}')