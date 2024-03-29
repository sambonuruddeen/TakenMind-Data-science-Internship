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

#sms.clustermap(df2).savefig('cluster1.png')

#sms.clustermap(df2,col_cluster=False).savefig('cluster2.png')

#standasrdize by rows
sms.clustermap(df2,standard_scale=1).savefig('cluster4.png')
