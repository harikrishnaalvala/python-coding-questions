def second_max_difference(arr):
    # Sort the array in ascending order
    arr.sort()

    # Calculate the maximum difference between the last and first elements
    first_max_diff = arr[-1] - arr[0]

    # Initialize variables to store the first and second maximum differences
    first_max = float('-inf')
    second_max = float('-inf')

    # Iterate through the array to find the second maximum difference
    for i in range(len(arr) - 1):
        diff = arr[i+1] - arr[i]
        if diff > first_max:
            second_max = first_max
            first_max = diff
        elif diff > second_max and diff != first_max:
            second_max = diff

    return second_max

# Test the function with the example array
arr = [14, 12, 70, 15, 95, 65, 22, 30]
output = second_max_difference(arr)
print("Output:", output)
