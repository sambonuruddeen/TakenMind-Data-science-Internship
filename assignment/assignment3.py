import numpy as np
import pandas as pd
from numpy.random import randn
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sms

df = pd.read_csv('dataset.csv')


df2 = df.pivot_table(values='lifeExp', index=df.continent, columns=df.year)
print df2
sms.heatmap(df2,annot=True).get_figure().savefig('assignment3.png')