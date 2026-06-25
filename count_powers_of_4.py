def count_powers_of_4():
    count = 0
    num = 1

    while num <= 10:
        num *= 4
        count += 1

    return count

# Test the function
output = count_powers_of_4()
print("Count of powers of 4 up to 10:", output)
