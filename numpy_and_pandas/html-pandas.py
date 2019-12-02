import pandas as pd
from pandas import DataFrame
from pandas import read_html

#install beutifulsoup4

url = "https://countrycode.org/"
dflist = pd.io.html.read_html(url)

dframe = dflist[0]
print dframe

print dframe.columns.values
