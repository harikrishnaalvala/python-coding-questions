def create_short_code(s):
    if not s:  # Check if the string is empty
        return ""

    result = ""
    current_char = s[0]
    count = 1

    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            result += current_char + str(count)
            current_char = char
            count = 1

    # Append the last character and its count
    result += current_char + str(count)

    return result

# Example usage
print(create_short_code("aajjkkp"))
