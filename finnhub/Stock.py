# Class to represent all stock atributes


import requests
import datetime

# globals


class Stock:

    def __init__(self, ticker='', resolution='M'):
        self.ticker = ticker
        self.resolution = resolution
        self.data = {}

    def history(self, timeframe=365):
        finnhubAdd = 'https://finnhub.io/api/v1/'
        key = 'bvul16v48v6pkq83um80'
        start = int((datetime.datetime.now() - datetime.timedelta(days=timeframe)).timestamp())
        end = int(datetime.datetime.now().timestamp())
        print(start, end)
        requestString = finnhubAdd+'stock/candle?'+'symbol='+self.ticker+'&resolution='+self.resolution+'&from='+str(start)+'&to='+str(end)+'&token='+key
        r = requests.get(requestString)
        return r

    def getValue(self):
        pass


