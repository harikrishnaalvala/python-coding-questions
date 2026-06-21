def find_second_largest(nums):
    if len(nums) < 2:
        return None  # Not enough elements for a second largest

    largest = second_largest = float('-inf')  # Initialize to negative infinity

    for num in nums:
        if num > largest:
            second_largest, largest = largest, num
        elif largest > num > second_largest:
            second_largest = num

    return second_largest if second_largest != float('-inf') else None

# Test the function with the example
input_list = [4, 6, 3, 94, 9]
print("Second largest number:", find_second_largest(input_list)) #9
