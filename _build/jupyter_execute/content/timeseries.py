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

strftime allows you to select certain parts of the datetime object with using the special formatting codes. Here is a list of common ones:

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


