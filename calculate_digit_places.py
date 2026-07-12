def calculate_digit_places(number):
    num_str = str(number)
    length = len(num_str)
    place_values = []

    for i, digit in enumerate(num_str):
        if digit != '0':  # Exclude zeros as they don't contribute to the place value
            place = digit + '0' * (length - i - 1)
            place_values.append(place)

    return ','.join(place_values)

# Example usage
print(calculate_digit_places(4521))  # Output will be '4000,500,20,1'
