import requests
from bs4 import BeautifulSoup
import time
import asyncio
import aiohttp

STOCKS = ['https://www.nasdaq.com/symbol/aapl', 'https://www.nasdaq.com/symbol/fb', 'https://www.nasdaq.com/symbol/msft', 'https://www.nasdaq.com/symbol/googl', 'https://www.nasdaq.com/symbol/appn', 'https://www.nasdaq.com/symbol/team']

def _render_response(res):
	soup = BeautifulSoup(res, 'html.parser')
	company = soup.find('div', {'id': 'qwidget_pageheader'}).text
	price = soup.find('div', {'id': 'qwidget_lastsale'}).text
	print(company)
	print(price)

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def gather_tasks():
	async with aiohttp.ClientSession() as session:
		# creating corountines for asyncio to gather
		coroutines = [fetch(session, stock) for stock in STOCKS]
		return await asyncio.gather(*coroutines)

async def fetch_end_render():
	for i, response in enumerate(await gather_tasks()):
		_render_response(response)

start = time.time()
loop = asyncio.get_event_loop()
# Blocking call which returns when the main() coroutine is done
loop.run_until_complete(fetch_end_render())
loop.close()
print(f'{time.time()-start}')