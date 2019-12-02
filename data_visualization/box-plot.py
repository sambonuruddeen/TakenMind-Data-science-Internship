import numpy as np
import pandas as pd
from numpy.random import randn
from scipy import stats
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sms

ds1 = randn(80)
#sms.boxplot(ds1,orient='v').get_figure().savefig('box1.png')
sms.boxplot(ds1,whis=np.inf).get_figure().savefig('box2.png')