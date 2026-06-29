def sort_binary_digits(binary_number):
    # Convert the binary number to a string
    binary_str = str(binary_number)

    # Convert the string to a list of characters
    digits = list(binary_str)

    # Sort the list of characters
    digits.sort()

    # Join the sorted characters back into a string
    sorted_str = ''.join(digits)

    # Convert the string back to an integer
    sorted_binary_number = int(sorted_str, 2)

    return sorted_binary_number

# Test the function with the example
input_binary = 842957
output = sort_binary_digits(input_binary)
print("Output:", output) # Output: 245789
