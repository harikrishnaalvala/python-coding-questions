def all_characters_unique(input_str):
    seen = set()
    for char in input_str:
        if char in seen:
            return "false"
        seen.add(char)
    return "true"

# Test the function with examples
input_str_1 = "abcde"
input_str_2 = "hello"
print("All characters in", input_str_1, "are unique:", all_characters_unique(input_str_1)) 
print("All characters in", input_str_2, "are unique:", all_characters_unique(input_str_2))


