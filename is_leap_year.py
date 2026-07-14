def is_leap_year(year):
    # Leap year if divisible by 4
    if year % 4 == 0:
        # But if it's a centennial year, it must also be divisible by 400
        if year % 100 == 0:
            return year % 400 == 0
        return True
    return False

# Example usage
year = 2004
if is_leap_year(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
