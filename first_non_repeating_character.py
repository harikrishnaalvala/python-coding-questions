def first_non_repeating_char(string):
    char_count = {}

    # Count the occurrences of each character
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Find the first non-repeating character
    for char in string:
        if char_count[char] == 1:
            return char

    return None  # In case there's no non-repeating character

# Test the function with the example
input_string = "amazon"
print("First non-repeating character:", first_non_repeating_char(input_string)) #m
