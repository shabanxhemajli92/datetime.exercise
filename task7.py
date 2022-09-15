from datetime import datetime
import time

start_date=datetime(year=2020,month=1,day=25)
date_format=start_date.strftime("%d %B ,%Y" )
print("Hello Friedrich, your rent of 300 € is due on",date_format)