def non_repeating_characters(input_str):
    char_count = {}

    # Count the occurrences of each character in the string
    for char in input_str:
        char_count[char] = char_count.get(char, 0) + 1

    # Iterate through the string again and append non-repeating characters to a new string
    non_repeating_chars = ""
    for char in input_str:
        if char_count[char] == 1:
            non_repeating_chars += char

    return non_repeating_chars

# Test the function with the example
input_str = "daddy"
output = non_repeating_characters(input_str)
print("Output:", output)
