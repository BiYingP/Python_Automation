import requests
from datetime import datetime
import time

symbol = input("Enter the stock symbol: ")
from_date = input("Enter the start date in yyyy/mm/dd format: ")
to_date = input("Enter the end date in yyyy/mm/dd format: ")

from_datetime = datetime.strptime(from_date, "%Y/%m/%d")
to_datetime = datetime.strptime(to_date, "%Y/%m/%d")

from_epoch = int(time.mktime(from_datetime.timetuple()))
to_epoch = int(time.mktime(to_datetime.timetuple()))

url =f"https://query1.finance.yahoo.com/v7/finance/download/{symbol}?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true"

header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"} 

content = requests.get(url, headers = header).content

print(content)

with open ('data.csv', 'wb') as file:
	file.write(content)
