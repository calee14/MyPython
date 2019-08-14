import requests
from bs4 import BeautifulSoup
import time

STOCKS = ['https://www.nasdaq.com/symbol/aapl', 'https://www.nasdaq.com/symbol/fb', 'https://www.nasdaq.com/symbol/msft', 'https://www.nasdaq.com/symbol/googl', 'https://www.nasdaq.com/symbol/appn', 'https://www.nasdaq.com/symbol/team']

def _render_response(res):
	soup = BeautifulSoup(res, 'html.parser')
	company = soup.find('div', {'id': 'qwidget_pageheader'}).text
	price = soup.find('div', {'id': 'qwidget_lastsale'}).text
	print(company)
	print(price)

def get_stocks_info():
	for stock in STOCKS:
		response = requests.get(stock).text
		_render_response(response)

start = time.time()
get_stocks_info()
print(f'{time.time()-start}')