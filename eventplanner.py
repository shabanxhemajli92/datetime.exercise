from datetime import datetime
import datetime
from datetime import date

event_date=input("Type in the date of the event: ")
some_objct = datetime.datetime.fromisoformat(event_date)
todays_date=datetime.datetime.now()
date_of_event=(some_objct-todays_date)
print(date_of_event)
days=int(input("Enter the days Day:"))

years = days // 365
weeks = (days - (years* 365)) // 7
day = (days - (years* 365)) - (weeks * 7)

print("The event takes place in:",years,"years",weeks,"weeks","and",day,"days")