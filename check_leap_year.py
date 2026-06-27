def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def check_leap_year(year):
    if is_leap_year(year):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

# Test the function with examples
input_year1 = 2004
input_year2 = 2022
check_leap_year(input_year1) # 2004 is a leap year
check_leap_year(input_year2) # 2022 is not a leap year
