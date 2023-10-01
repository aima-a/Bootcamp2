# Intro Program
print("Hello, World!")

# Welcome Message
a = (input("Please enter your name: "))
print(f"Nice to meet you, {a}")

# Calendar program
import calendar

# Input year and month from the user
year = int(input("Enter the year (e.g., 2023): "))
month = int(input("Enter the month (1-12): "))

# Create a calendar for the specified year and month
cal = calendar.month(year, month)

# Display the calendar
print(f"Calendar for {calendar.month_name[month]} {year}:\n")
print(cal)

