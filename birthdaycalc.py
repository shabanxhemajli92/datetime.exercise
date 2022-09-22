from datetime import datetime
import datetime
from datetime import date

bday_input=input("Type in your birthday: ")
some_objct = datetime.datetime.fromisoformat(bday_input)
todays_date=datetime.datetime.now()
age_years=(todays_date-some_objct)

days=age_years.days

years = days // 365
weeks = days // 7
months = days // 30

print("Your duration in the world so far is:",years,"years","or",weeks,"weeks","or",months,"months since your mother validated your existance")
