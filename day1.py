Integrated new line and tab practice
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")
# Display current date
import datetime
now = datetime.datetime.now()
print(now)
# Compute radius when number entered
from math import pi
radius = float(input("Enter radius here:"))
print("The area of circle with radius " + str(radius)+ " is: "+ str(pi * radius**2))
# user's first and last name and print them in reverse order
firstName = input("Enter first name: ")
lastName = input("Enter last name: ")
print(lastName.capitalize() + " " + firstName.capitalize())
#  accept a filename from the user and print the extension
fileName = input("Enter the filename: ")
file_ext = fileName.split('.')
print("The extension of the file is: " + repr(file_ext[-1]))
Display the first and last color in a list
colors = ["red",'blue','green','purple','orange','yellow']
print(colors[0].capitalize()+" and "+ colors[-1].capitalize())
# print the calendar of a month
import calendar
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
print(calendar.month(year,month))
# Calculate the days between two dates
from datetime import date
first_date = date(2022,1,1)
last_date = date(2022,5,11)
days_between = last_date - first_date
print(days_between.days)
Alpha sort and cutting
countries = ['vietnam','singapore','laos','cambodia','indonesia','malaysia','myanmar','brunei']
countries.sort()
print(countries)
print(countries[0].capitalize() + " and "+ countries[-1].capitalize())
countries.append('thailand')
print(countries[0].capitalize() + " and "+ countries[-1].capitalize())

