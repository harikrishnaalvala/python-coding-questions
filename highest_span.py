def highest_span(arr, num):
    max_span = 0
    first_occurrence = -1
    last_occurrence = -1

    # Traverse the array to find the first and last occurrence of the given number
    for i in range(len(arr)):
        if arr[i] == num:
            if first_occurrence == -1:
                first_occurrence = i
            last_occurrence = i

    # Calculate the span
    if first_occurrence != -1 and last_occurrence != -1:
        max_span = last_occurrence - first_occurrence

    return max_span

# Example usage
arr = [1, 2, 3, 4, 1, 6, 7, 1, 9, 10]
num = 1
print("Highest span of", num, "in the array is:", highest_span(arr, num))
