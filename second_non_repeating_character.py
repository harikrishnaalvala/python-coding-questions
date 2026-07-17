def second_non_repeating_character(s):
    # Count frequency of each character
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Find the second non-repeating character
    non_repeating_chars = [char for char in char_count if char_count[char] == 1]
    
    if len(non_repeating_chars) < 2:
        return "No second non-repeating character"
    else:
        return non_repeating_chars[1]

# Test the function with provided examples
test_cases = ["amazon", "raju", "aabbcc", "aabbc"]
for test in test_cases:
    print(f"Input: {test} Output: {second_non_repeating_character(test)}")

""" Input: amazon Output: z
Input: raju Output: a
Input: aabbcc Output: No second non-repeating character
Input: aabbc Output: No second non-repeating character

"""
