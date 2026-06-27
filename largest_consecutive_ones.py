def largest_consecutive_ones(input_str):
    max_count = 0
    current_count = 0

    for char in input_str:
        if char == '1':
            current_count += 1
        else:
            max_count = max(max_count, current_count)
            current_count = 0

    return max_count

# Test the function with the example
input_str = "0000110111"
output = largest_consecutive_ones(input_str)
print("Output:", output) # Output: 3
