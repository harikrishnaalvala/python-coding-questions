def move_zeros(arr):
    zero_index = 0

    for i in range(len(arr)):
        if arr[i] == 0:
            # Swap the current element (zero) with the element at zero_index
            arr[i], arr[zero_index] = arr[zero_index], arr[i]
            # Increment zero_index to point to the next non-zero position
            zero_index += 1

    return arr

# Example usage
print(move_zeros([3, 5, 0, 6, 0, 0, 6, 0]))  # Output: [0, 0, 0, 0, 3, 5, 6, 6]
