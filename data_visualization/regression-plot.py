import numpy as np
import pandas as pd
from numpy.random import randn
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sms
from pandas import Series

df = sms.load_dataset('diamonds').sample(frac=1).head(100)
print df

sms.lmplot('price','carat',df).savefig('1.png')

#modify
sms.lmplot('price','carat',df,scatter_kws={'marker':'0','color':'green'},line_kws={'color':'red','linewidth': 1}).savefig('2.png')

#higer order trend line
sms.lmplot('price','carat',df,order=4,scatter_kws={'marker':'0','color':'green'},line_kws={'color':'red','linewidth': 1}).savefig('3.png')

#scatter plot without a trendline
sms.lmplot('price','carat',df,fit_reg=False).savefig('4.png')

#hue arguments
sms.lmplot('price','carat',df,hue='cut',markers=['^','v','*',',','s']).savefig('5.png')
sms.lmplot('price','carat',df,hue='cut').savefig('6.png')

#local regression
sms.lmplot('price','carat',df,lowess=True).savefig('7.png')

#regplot -
sms.regplot('price','carat',df).get_figure().savefig('8.png')

#sub plots
image , (plt1,plt2) = plt.subplots(1,2,sharey = True)

sms.regplot('price','carat',df,ax=plt1).get_figure().savefig('9.png')
sms.boxplot(df['carat'],df['depth'],color='green',ax=plt2).get_figure().savefig('9.png')
