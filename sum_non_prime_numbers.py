def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def sum_non_prime_numbers(start, end):
    non_prime_sum = 0

    # Iterate through the numbers in the given range
    for num in range(start, end + 1):
        # Check if the number is not prime
        if not is_prime(num):
            non_prime_sum += num

    return non_prime_sum

# Test the function with an example range
start = 1
end = 20
result = sum_non_prime_numbers(start, end)
print("Sum of non-prime numbers in the range", start, "to", end, ":", result)
