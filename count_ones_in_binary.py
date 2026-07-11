def count_ones_in_binary(number):
    # Convert number to its binary representation
    binary_representation = bin(number)

    # Count the number of 1s
    count_of_ones = binary_representation.count('1')

    return count_of_ones

# Example usage
print(count_ones_in_binary(10))  # Output will be 2
