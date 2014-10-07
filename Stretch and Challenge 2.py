#Ferhat Yeter
#
#

date = input("Please enter the date in the form DD MM YY: ")

days = date[:2]
month = date[3:5]
year = date[6:8]

year = int(year)



if year > 31:
    century = "19"
else:
    century = "20"

if days[0] == "0":
    days = days[1]


if days == "1" or days == "21" or days == "31":
    days_after = "st"

elif days == "2" or days == "22":
    days_after = "nd"
	
elif days == "3" or days == "23":
    days_after = "rd"
else:
    days_after = "th"

if month == "01" or "1":
    months = "January"
elif month == "02" or "2":
    months = "February"
elif month == "03" or "3":
    months = "March"
elif month == "04" or "4":
    months = "April"
elif month == "05" or "5":
    months = "May"
elif month == "06" or "6":
    months = "June"
elif month == "07" or "7":
    months = "July"
elif month == "08" or "8":
    months = "August"
elif month == "09" or "9":
    months = "September"
elif month == "10":
    months = "October"
elif month == "11":
    months = "November"
elif month == "12":
    months = "December"
else:
    print("The number you have entered is not valid")


print("{0}{1} {2} {3}{4}".format(days,days_after,months,century,year))
