#function to calculate leap year
def is_leap_year(year):
    if (year % 4 == 0 and year %100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    
year = int(input("Enter the year:"))

#Testing
if is_leap_year:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

    


