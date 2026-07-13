def reverse_without_space(s):
    # Extract non-space characters and reverse
    non_space_chars = [c for c in s if c != ' '][::-1]

    # Re-insert characters and spaces
    result = []
    non_space_index = 0
    for char in s:
        if char == ' ':
            result.append(' ')
        else:
            result.append(non_space_chars[non_space_index])
            non_space_index += 1

    return ''.join(result)

# Example usage
input_str = "a bc def g"
output_str = reverse_without_space(input_str)
print(output_str)  # Output: "g fe dcb a"
