def is_cyclic_string(s):
    # Double the string
    doubled_string = s + s

    # Check if original string is substring of doubled string
    return s in doubled_string

# Example usage
input_string = "abcabc"
print(is_cyclic_string(input_string))  # Output: True

input_string = "abcd"
print(is_cyclic_string(input_string))  # Output: False
