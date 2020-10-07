(time)=
# Time Series / Dates

Key ways of thinking about time in python:

- **Timestamp**: An instant in time
- **Period**: Some established interval of time, usually a month, year. Special case of interval
- **Interval**: An arbitrary interval of time.
- **Experimental / Elapsed time**: Represents elapsed time from some chosen start point.

Important Native-Python Packages concering date:

- [`datetime`](https://docs.python.org/3/library/datetime.html)
- [`dateutil`](https://dateutil.readthedocs.io/en/stable/)

from datetime import datetime
print(f'datetime.now() : {datetime.now()}')
print(f'datetime.now().year : {datetime.now().year}')

from dateutil import parser
date = parser.parse("4th of July, 2015")
date

Types available in the datetime module:

- `date` -   Date object (only concerned with calendar type dates)
- `time` -   Time object concerned with time of a date
- `datetime` -  Combo of both
- `timedelta` - Differences between to datetime objects
- `tzinfo` - Time zone things

(timestr)=
## Strings and strftime

Once you have a datetime object or some date ready to be converted into one, it is easy to convert and format into a string

stamp = datetime.now()
print(str(stamp))

stamp.strftime('%Y-%m')

(strf)=
### Strftime

**strftime** allows you to select certain parts of the datetime object with using the special formatting codes. Here is a list of common ones: (ISO C89 compatible)

- `%Y` : 4 digit year
- `%y` : 2 digit year
- `%m` : 2 digit month
- `%d` : 2 digit day
- `%H` : military time hour
- `%h` : 12 hour [01,12]
- `%M` : 2 digit minute [00,59]
- `%S` : seconds [00,61]
- `%w` : weekday as an integer
- `%F` : shortcut for `%Y-%m-%d`
- `%D` : shortcut for `%d/%m/%y`


Here is a list of useful locale-specific **strftime** codes:

- `%a` : abbreviated day name
- `%A` : Full-length day name
- `%b` : abbreviated month name
- `%B` : Full month name
- `%c` : full date-time (Tue 01 May 2012 04:20:57 PM’)
- `%p` : locale equivalent of a.m./p.m.
- `%x` : locale-appropriate formatted date (%c)
- `%X` : locale-appropriate time

(datetime64)=
## Numpy [datetime64](https://numpy.org/doc/stable/reference/arrays.datetime.html)

Like most native python objects and and processes - problems with efficiency and speed arise when dealing with large quantities and loops. 

The dypte **datetime64** was developed in order to address these problems.

The `datetime64` datatype encodes dates as 64 bit integers (which allows dates to be represented compactly)

import numpy as np
date = np.array('2020-07-04', dtype='datetime64[D]')
date

Dates in this format allow for vectorized operations. 
````{margin}
```{note}
Recall that alot of the speed attainable in `numpy` is due to the uniformity 
of dtype in numpy arrays
```
````

date + np.arange(6)

`datetime64` and `timedelta` are both built upon a **fundamental time unit** and so the range of encodable dates = 

$$ 2^{64} \cdot (t_{u}) $$

where $t_{u}$ is the smallest unit of time measured **(time resolution)** and the product above is the **max time span**  

$ns = 10^{-9}$ (nanoseconds) are the default ftu. but there are quite a few codes that can be used.

np.datetime64('2020-08-11', 'ns')

Here are the various codes for `datetime64`:  

- `Y` : year
- `M` : month
- `W` : ...
- `D` : 
- `h` : 
- `m` :
- `s` :
- `ms` : millisecond
- `us` : microsecond $10^{-6}$ one millionth of a second
- `ns` : nanosecond
- `ps` : picosecond $10^{-12}$ one trillionth of a second
- `fs` : femtosecond
- `as` : attosecond $10^{-18}$ one quintillionth of a second

(pandasdate)=
## Dates and Times in Pandas

Pandas builds upon `datetime`, `dateutils`, and `datetime64` to provide objects such as `Timestamp` that takes the best part of each:  

The flexibility and ease of use of native `python3` packages, and the efficient storage and vectorized interface of `numpy`

import pandas as pd
date = pd.to_datetime('11 of August, 2020')
date

date.strftime("%A")

date + pd.to_timedelta(np.arange(5), "D")

(timeindex)=
### Indexing by Timestamp

The power of datetime in pandas becomes apparent when we begin to index by timestamp allowing us to parse data easily w.r.t. time.  

We do this by constructing an a DatetimeIndex and using that as our index for our series/df. We can accomplish this explicitly by passing an array of properly formatted
timestamps to `pd.DatetimeIndex()` or using pandas excellent `pd.to_datetime()` function:

index1 = pd.DatetimeIndex(['2020-08-11', '2020-08-12', '2020-08-13'])
index1

dates = ['August 11th, 2020', 'August 12th, 2020', 'August 13th, 2020']
index2 = pd.to_datetime(dates)
index2

(datastructures)=
### Time Data Structures in Pandas

`Timestamp`: essentially a replacement for native python `datetime` based on more efficient `datetime64` datatype  

`DatetimeIndex` : Index data structure associated with `Timestamp`

---

`Period`: A fixed-frequency interval into which `Timestamps` either fall or do not.  

`PeriodIndex`: Associated Index data structure/

---

`Timedelta`: a duration, small amount of elapsed time from some reference.  

`TimedeltaIndex`: Associated index data structure.

---

`Timestamp` and `DatetimeIndex` are the fundamental date/time objects in pandas.  

Although they can be invoked directly it is much more common to use the `pd.to_datetime()` function, **which can parse a wide variety of formats.**

```{note}
Any `DatetimeIndex` can be converted to a `PeriodIndex` with the `pd.to_period()` function with the addition of the desired
frequency code (ex. 'D').
```

(dateseq)=
### Functions that allow for creation of Date Sequences

`pd.date_range()`  
`pd.period_range()`  
`pd.timedelta_range()`

Like the native python `range()` function these calls allow for specification of start, stop and step/frequency to create a sequence of date/time objects.

pd.date_range('2020-08-11', '2020-08-17')

pd.date_range('2020-08-11', periods=7, freq="D")

pd.period_range('2020-01', periods=6, freq="M")

pd.timedelta_range(0, periods=10, freq='H')

(freqcodes)=
### Frequency Codes

#### Conventional Time

`D` : Calendar Day  
`W` : Weekly  
`M` : Month End  
`A` : Year End  
`H` : Hourly  
`T` : Minutes  
`S` : Seconds  
`L` : Milliseconds  
`U` : Microseconds  
`N` : Nanoseconds  

#### Business Time

`B` : Business Day  
`BM` : Business Month End  
`BQ` : Business Quarter End  
`BA` : Business Year End 

```{important}
Adding `S` to any monthly, quarterly or annual period will change the marker from the end of the period to the beginning.

ex. `MS` or `BMS`
```

#### Other Modifications to Ranges/Periods

In addition to changing the start or ending of a period as a split point you have other flexibility.  

You can change the month used to mark any quarterly or annual code by adding a 3-letter suffix code to the original:  

`Q-JAN`, `BQS-APR`, `A-FEB`, `BAS-APR`  

You can also modify the split points of other periods such as week:  

`W-SUN`, `W-TUE`

(offsets)=
#### Offsets

[pandas offset documentation](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#time-date-components)

Pandas allows us to specify offsets which help select dates in a range based on some criterion.

from pandas.tseries.offsets import BDay
pd.date_range('2020-10-04', periods=5, freq=BDay()) # selects the next 5 business days on or after intial date

