def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def next_n_leap_years(start_year, n):
    count = 0
    year = start_year + 1  # Start checking from the next year

    while count < n:
        if is_leap_year(year):
            print(year, end=", ")
            count += 1
        year += 1

# Test the function with the example
input_year = 2000
n = 5
print("Output:")
next_n_leap_years(input_year, n)
