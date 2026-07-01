def print_numbers_with_remainder_4(arr):
    for num in arr:
        if num % 5 == 4:
            print(num, end=" ")

# Test the function with the provided examples
input_arr1 = [19, 10, 44, 3, 11, 129]
input_arr2 = [13, 4]

print("Output 1:")
print_numbers_with_remainder_4(input_arr1)

print("\\nOutput 2:")
print_numbers_with_remainder_4(input_arr2)
