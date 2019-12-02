import numpy as np
import pandas as pd
from numpy.random import randn
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sms

df = sms.load_dataset('flights')
df2 = df.pivot('year','month','passengers')
print df2

#sms.heatmap(df2).get_figure().savefig('heatmap1.png')

#sms.heatmap(df2,annot=True,fmt='d').get_figure().savefig('heatmap2.png')

sms.heatmap(df2,center=df2.loc[1955,'January']).get_figure().savefig('heatmap3.png')
