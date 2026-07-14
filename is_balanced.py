def is_balanced(expression):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map.keys():
            if stack == [] or bracket_map[char] != stack.pop():
                return 'not balanced'

    return 'balanced' if not stack else 'not balanced'

# Example usage
input_expression = "[]{}"
print(is_balanced(input_expression))  # Output: 'balanced'

input_expression = "([){]"
print(is_balanced(input_expression))  # Output: 'not balanced'
