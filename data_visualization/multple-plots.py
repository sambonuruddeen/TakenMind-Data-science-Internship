import numpy as np
import pandas as pd
from numpy.random import randn
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sms
from pandas import Series

ds = randn(100)
#fig = sms.distplot(ds,bins=15).get_figure()
#fig.savefig('pic1.png')

#fig2 = sms.distplot(ds,hist=False,rug=True,bins=10).get_figure()
#fig2.savefig('pic2.png')

#change parameters of each graph

#fig3 = sms.distplot(ds,bins=15,
  #                  kde_kws= {'color':'red', 'label':'KDE graph'},
 #                   hist_kws= {'label':'Histogram Label', 'color':'green','alpha':0.5}
#
#).get_figure()
#fig3.savefig('pic3.png')

#
s1 = Series(ds,name='s1')
fig4 = sms.distplot(s1,bins=15).get_figure()
fig4.savefig('pic4.png')