def second_largest_difference(nums):
    if len(nums) < 2:
        return None  # Not enough elements for a meaningful difference

    max_num = max(nums)  # Find the maximum number
    differences = [max_num - num for num in nums]  # Calculate differences

    # Remove the largest difference (which is always 0 since it's max_num - max_num)
    differences.remove(0)

    # Find the second largest difference
    return max(differences)

# Test the function with the example
input_array = [1, 2, 3, 4, 5]
print("Second most largest difference:", second_largest_difference(input_array)) # 3
