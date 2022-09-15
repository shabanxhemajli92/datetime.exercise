import datetime
from time import strftime

current_datetime=datetime.datetime.now()
after_7=current_datetime + datetime.timedelta(days=7)
format_date=after_7.strftime("%Y-%m-%-d")
print(format_date)
