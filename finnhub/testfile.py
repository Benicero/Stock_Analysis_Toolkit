# testfile for functions that cannot easily be tested with a test suite
import Stock
import matplotlib.pyplot as plt
import finplot as fplt
import pandas as pd
import yfinance

# Purpose: Test the history method in the Stock class
# Currect Behavior: Display Tesla stock data from the last year in the terminal
def getStockHistory(s):
    stock = Stock.Stock(s)
    t = stock.history()
    # print(t.json())
    # plt.plot(t.json()['o'])
    # plt.plot(t.json()['h'])
    # plt.plot(t.json()['l'])
    # plt.plot(t.json()['c'])
    # plt.title(stock.ticker)
    # plt.show()
    # df = t.json()
    # df = pd.read_json(t.json())
    # df = pd.DataFrame.from_dict(t.json())
    # print(df)
    # fplt.candlestick_ochl(df[['o', 'c', 'h', 'l']])
    # fplt.show()

    df = f = yfinance.download('XRP')
    fplt.candlestick_ochl(df[['Open', 'Close', 'High', 'Low']])
    fplt.show()

if __name__ == "__main__":
    getStockHistory('TSLA')
