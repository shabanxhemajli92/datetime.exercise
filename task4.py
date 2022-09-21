from datetime import datetime
import datetime
#date_toconvert=input("type in the date to convert: ")
time_now=datetime.datetime.now()
date_converter=time_now.strftime("%b %d %Y %H:%M")
print("The date and time is:",date_converter)

datetime.datetime.st