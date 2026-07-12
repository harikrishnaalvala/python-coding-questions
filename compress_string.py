def compress_string(s):
    if not s:
        return ""

    compressed = []
    current_char = s[0]
    count = 1

    for char in s[1:]:
        if char == current_char:
            count += 1
        else:
            compressed.append(current_char + str(count))
            current_char = char
            count = 1

    # Append the last character and its count
    compressed.append(current_char + str(count))

    # Convert list to string and check if compressed string is shorter
    compressed_str = ''.join(compressed)
    return compressed_str if len(compressed_str) < len(s) else s

# Example usage
print(compress_string("aabcccccaaa"))  # Output: a2b1c5a3
print(compress_string("abcd"))         # Output: abcd
