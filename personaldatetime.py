from datetime import datetime
import datetime
import time
import colorama
import os
colorama.init()


print(colorama.Back.LIGHTMAGENTA_EX+"#########Welcome to History viewer############"+colorama.Back.RESET)

print("There are four dates to be displayed:D1,D2,D3,D4 or type end to exit")
inp_var=""
while inp_var != "end" :
    inp_var=input(colorama.Fore.BLUE+"Type in date to view historic event: "+colorama.Fore.RESET)
    os.system("clear")
    time.sleep(2)
    


    d1=datetime.datetime(1833,2,1)
    d2=datetime.datetime(1957,2,1)
    d3=datetime.datetime(1958,2,1)
    d4=datetime.datetime(1991,2,20)

    if inp_var=="d1":
        print(colorama.Fore.CYAN+"on this",str(d1),"Ada Lovelace invents the first ever machine algorithm "+colorama.Fore.RESET)
    elif inp_var=="d2":
        print(colorama.Fore.GREEN+"on this",str(d2),"Fortran was invented"+colorama.Fore.RESET)
    elif inp_var=="d3":
        print(colorama.Fore.LIGHTYELLOW_EX+"on this",str(d3),"First Algorithmic language was created"+colorama.Fore.RESET)
    elif inp_var=="d4":
        print("on this",str(d4),"Guido van Rossum invents Python")
    



