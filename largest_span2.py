def largest_span(arr):
    max_span = 0
    last_zero_index = -1
    last_one_index = -1

    for i in range(len(arr)):
        if arr[i] == 0:
            last_zero_index = i
        elif arr[i] == 1:
            last_one_index = i

        current_span = last_one_index - last_zero_index

        if current_span > max_span:
            max_span = current_span

    return max_span

# Example usage
arr = [0, 1, 1, 1, 0, 0, 1, 1, 0, 1]
print("Largest span between two occurrences of 1:", largest_span(arr)) # Largest span between two occurrences of 1: 3
