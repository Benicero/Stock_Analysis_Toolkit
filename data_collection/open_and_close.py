import requests
import pandas as pd 
import pandas_datareader as pdr # gives an error but still works ?
from datetime import datetime

"""
***THIS METHOD IS TECHNICALLY DEPRECATED SO WE SHOULD EVENTUALLY USE ANOTHER ONE***

---return pandas dataframe---
Fields: 
['High' 'Low' 'Open' 'Close' 'Volume' 'Adj Close']

it looks like this data is 2 days behind, but thats ok for now
"""

# variable specifications
symbol = 'IBM'
start = datetime(2000, 1, 1)
end = datetime.today()

# access the data and return pandas dataframe
ibm = pdr.get_data_yahoo(symbols=symbol, start=start, end=end)




print(ibm[-10:])

ibm_max = ibm.loc[ibm['High'].idxmax()]
print(ibm_max)