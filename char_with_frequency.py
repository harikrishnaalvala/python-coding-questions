def char_with_frequency(string):
    if not string:
        return ""

    output = ""
    current_char = string[0]
    count = 1

    for char in string[1:]:  # Start from the second character
        if char == current_char:
            count += 1
        else:
            # Append current character and its count to output
            output += current_char + str(count)
            current_char = char
            count = 1

    # Append the last character and its count
    output += current_char + str(count)

    return output

# Test the function with the example
input_string = "aaabbaccd"
print("Output:", char_with_frequency(input_string))
