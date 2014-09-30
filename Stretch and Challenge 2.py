#Ferhat Yeter
#
#


days = int(input("Please enter the day in the form DD: "))
month = int(input("Please enter the months in the form MM: "))
year = int(input("Please enter the year in the form YY: "))

if days == 1 or days == 21 or days == 31:
    days_after = "st"

elif days == 2 or days == 22:
    days_after = "nd"
	
elif days == 3 or days == 23:
    days_after = "rd"
else:
    days_after = "th"

if month == 1:
    months = "January"
elif month == 2:
    months = "February"
elif month == 3:
    months = "March"
elif month == 4:
    months = "April"
elif month == 5:
    months = "May"
elif month == 6:
    months = "June"
elif month == 7:
    months = "July"
elif month == 8:
    months = "August"
elif month == 9:
    months = "September"
elif month == 10:
    months = "October"
elif month == 11:
    months = "November"
elif month == 12:
    months = "December"
else:
    print("The number you have entered is not valid")



print("{0}{1} {2} 20{3}".format(days,days_after,months,year))
