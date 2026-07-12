def find_second_minimum(numbers):
    if len(numbers) < 2:
        return "List does not have enough elements"

    # Sort the list
    numbers.sort()

    # Find the second minimum
    min_num = numbers[0]
    for num in numbers:
        if num > min_num:
            return num

    return "No second minimum found"

# Example usage
print(find_second_minimum([4, 5, 1, 3, 7, 8]))  # Output: 3
