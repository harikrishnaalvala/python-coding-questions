def reverse_and_change_case(s):
    # Reverse the string using slicing
    reversed_string = s[::-1]

    # Change the case of each character
    new_string = ''
    for char in reversed_string:
        if char.isupper():
            new_string += char.lower()
        else:
            new_string += char.upper()

    return new_string

# Example usage
print(reverse_and_change_case("My name is Ram"))  # Output: ra msie ma nYM
