import pandas as pd
import numpy as np
import pandas_datareader.data as web
from datetime import datetime

f = web.DataReader("GOOGL", "av-daily-adjusted", start=datetime(2016, 10, 1),
   ...:                    end=datetime(2020, 10, 1),
   ...:                    api_key='XGZ3LT2XOAH7BOPT')

f

pd.DatetimeIndex(f.index)

f['2020-01-01':'2020-12-31']

%matplotlib inline
import matplotlib.pyplot as plt
import seaborn; seaborn.set()

close = f.close

close.index = pd.DatetimeIndex(close.index)

close.plot()

close.plot(alpha=.5, style='-')

close.resample('BA').mean().plot(style=':')

close.asfreq('BA').plot(style='--')

close.plot(alpha=0.5, style='-')
close.resample('BA').mean().plot(style=':')
close.asfreq('BA').plot(style='--');
plt.legend(['input', 'resample', 'asfreq'],
loc='upper left');

