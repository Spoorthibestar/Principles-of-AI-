# Function to check if a year is a leap year
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Input a year
year = int(input("Enter a year: "))

# Check if the year is a leap year
if is_leap_year(year):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
