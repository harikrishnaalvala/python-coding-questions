def is_armstrong_number(num):
    # Count the number of digits
    num_str = str(num)
    num_digits = len(num_str)

    # Compute the sum of each digit raised to the power of the number of digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)

    # Check if the sum is equal to the original number
    return armstrong_sum == num

# Example usage
num = 153
print(f"{num} is Armstrong number:", is_armstrong_number(num))#  153 is Armstrong number: True
