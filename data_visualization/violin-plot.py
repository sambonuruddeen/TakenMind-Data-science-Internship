import numpy as np
import pandas as pd
from numpy.random import randn
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sms

ds = randn(80)

#sms.violinplot(ds).get_figure().savefig('violin1.png')

sms.violinplot(ds,bw=0.2).get_figure().savefig('violin2.png')

#multiple
sms.violinplot(ds,inner='stick').get_figure().savefig('violin3.png')