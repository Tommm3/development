import pytz
from datetime import datetime

tz = pytz.timezone('UTC')

date = datetime(2020, 9, 21, 19, 11, 0)

local_tz = tz.localize(date)

utc_tz = local_tz.astimezone(pytz.timezone('Europe/Warsaw'))

print(utc_tz)
