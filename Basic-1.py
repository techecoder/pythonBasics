from datetime import datetime, timedelta
from colorama import Fore

# variables
firstName = 'Saurabh'
lastName = 'Dixit'
fullName = 'Hello {0} {1} '.format(firstName, lastName)
currentDate = datetime.now()
oneDay = timedelta(days=1)
oneWeek = timedelta(weeks=1)
yesterday = currentDate - oneDay
previousWeekDays = currentDate - oneWeek
date1 = "26/05/2020 15:26:00"  # Date value as string
x = 40
y = 0

# Datetime variables print
print(currentDate)
print(Fore.RED + "Today's date is: ", currentDate)
print(Fore.BLUE + "Today's day is: ", currentDate.day)
print(Fore.GREEN + "Month is: ", currentDate.month)
print("Year is: ", currentDate.year)
print("Hours is: ", currentDate.hour)
print("Second is: ", currentDate.minute)
print(" ")
print(datetime.strptime(date1, "%d/%m/%Y %H:%M:%S"))    # String date value converted into Datetime format
print(" ")
print("Yesterday's Date was: ", yesterday)
print("Previous Weekday was: ", previousWeekDays)
print("")

# Capitalise the first letter of string
print(Fore.YELLOW + "Hello" + " " + firstName.capitalize() + ' ' + lastName.capitalize())
# upper case of enitre string
print(Fore.WHITE + "Hello" + " " + firstName.upper() + ' ' + lastName.upper())
# Lower case of entire string
print("Hello" + " " + firstName.lower() + ' ' + lastName.lower())
print(fullName)  # Print variable

# Exception Handling
try:
    print(x / y)
except Exception as e:
    print(Fore.RED + "Error No 1 is: " + str(e))  # will be executed when error occurs
finally:
    print()
    print(Fore.WHITE + "This is a nice code")  # This is an optional block

try:
    print(x / n)
except Exception as e:
    print(Fore.RED + "The second error is: " + str(e))
################################################################################################
