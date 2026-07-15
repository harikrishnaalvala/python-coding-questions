def sum_divisible_by_3_and_5():
    total_sum = 0

    # Iterate through numbers from 1 to 1000
    for num in range(1, 1001):
        # Check if the number is divisible by both 3 and 5
        if num % 3 == 0 and num % 5 == 0:
            total_sum += num

    return total_sum

# Calculate and print the sum
result = sum_divisible_by_3_and_5()
print("Sum of numbers divisible by both 3 and 5 between 1 and 1000:", result) # Sum of numbers divisible by both 3 and 5 between 1 and 1000: 33165
