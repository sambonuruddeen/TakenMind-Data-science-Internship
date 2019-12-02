import numpy as np
import pandas as pd
from pandas import Series, DataFrame

url = "https://en.wikipedia.org/wiki/Pivot_table"
dflist = pd.io.html.read_html(url)
df = dflist[0]
print df

#new_header = df.iloc[0] #grab first row for the header
#df = df[1:] #takethe data less the row
#df.columns = new_header #set the header row as the df header

#print df
print df.pivot('Date of sale','Sales person', 'Total price')