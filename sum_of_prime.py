def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def sum_of_prime(numbers):
    prime_sum = 0
    for num in numbers:
        if  is_prime(num):
            prime_sum += num
    return prime_sum

# Test the function with the example
input_array = [4, 2, 5, 7, 1]
output = sum_of_prime(input_array)
print("Output:", output) # 14
