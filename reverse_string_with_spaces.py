def reverse_string_with_spaces(input_str):
    words = input_str.split()  # Split the string into words based on spaces
    reversed_words = words[::-1]  # Reverse the order of the words
    reversed_str = ' '.join(reversed_words)  # Join the reversed words with spaces between them
    return reversed_str

# Test the function with the example
input_str = "a bc def g"
output = reverse_string_with_spaces(input_str)
print("Output:", output)
