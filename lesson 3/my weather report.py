# ======================================
# MY WEATHER REPORTER
# File my-weather-reporter.py
# ======================================


# part ! - USER INPUT
city = input("Enter your city name: ")
temp = float(input("Enter today's temperatture in C: "))


# PART 2 - STATMENT
if temp > 35:
      print("warning its very hot today!")

# PART 3 - if-else
if temp > 25:
    print("Great day to go outside!")
else:
    print("Great a jacket before you get out!")


            # PART 4 - if-elif-else
if temp > 35:
    print("Weather: Scorching Hot")
elif temp > 25:
    print("weather: warm and sunny")
elif temp > 15:
    print("weather: cool and breezy")
else:
    print("weather: cold - stay warm!")


                  # PART - datetime MODULE
import datetime
import calendar

now = datetime.datetime.now()
print("City:", city)
print("Time now:", now)

print(calendar.calendar(now.year))