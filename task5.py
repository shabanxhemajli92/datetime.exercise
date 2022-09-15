import datetime
from time import strftime

current_datetime=datetime.datetime.now()
before_15=current_datetime - datetime.timedelta(days=15)
format_date=before_15.strftime("%Y-%m-%-d")
print(format_date)

