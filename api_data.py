from alpha_vantage.timeseries import TimeSeries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import io

with open("api_key.txt", "r") as file:
    api_key = file.read()

ts1 = TimeSeries(key=api_key)

print(ts1.get_monthly("AAPL"))
url = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_WEEKLY&symbol=BTC&market=USD&apikey=' + str(api_key) + '&datatype=csv'
r = requests.get(url).content
data1 = BeautifulSoup(r)
print(data1)

data = pd.read_csv(io.StringIO(data1.decode("utf-8")))
print(data)

#apple1, meta_data = ts1.get_intraday("AAPL")


#df_apple1 = pd.DataFrame(apple1).transpose().reset_index()
#print(df_apple1)

