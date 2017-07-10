import time
import datetime
print "current time and date",datetime.datetime.now()
print "current year",datetime.date.today().strftime("%Y")
print "month of year",datetime.date.today().strftime("%B")
print "week number of year",datetime.date.today().strftime("%W")
print "weekday of the week",datetime.date.today().strftime("%w")
print "Day of the year",datetime.date.today().strftime("%j")
print "Day of the month",datetime.date.today().strftime("%d")
print "Day of week:",datetime.date.today().strftime("%A")

