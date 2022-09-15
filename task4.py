from datetime import datetime
date_toconvert=input("type in the date to convert: ")
date_converter=datetime.strptime(date_toconvert,"%b %d %Y %H:%M")
print("The date and time is:",date_converter)