def find_second_largest(arr):
    # Initialize first_max and second_max to negative infinity
    first_max = float('-inf')
    second_max = float('-inf')

    # Iterate through the array
    for num in arr:
        # Update first_max and second_max
        if num > first_max:
            second_max = first_max
            first_max = num
        elif num > second_max and num != first_max:
            second_max = num

    return second_max

# Test the function
arr = [4, 6, 3, 94, 9]
second_largest = find_second_largest(arr)
print("Second largest number:", second_largest)
