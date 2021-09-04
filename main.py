#imported necessary libraries
import datetime as dt
from selenium import webdriver
import join
import link
import timetable

#initializing location, day and date
driver = "C:\\Users\\admin\\Desktop\\online bot"
date = dt.datetime.now()
day = (date.strftime("%a")) #will give Mon for Monday

#calling functions according to day
if day == "Mon":
    monday()
elif day == "Tue":
    tuesday()
elif day == "Wed":
    wednesday()
if day == "Thu":
    thursday()
elif day == "Fri":
    friday()
elif day == "Sat":
    saturday()
else:
    print("Aaj kya jhadu pocha marne jayega")