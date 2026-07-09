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

def sum_of_non_primes(arr):
    total_sum = 0
    for num in arr:
        if not is_prime(num):
            total_sum += num
    print("sum=", total_sum)

# Test cases
arr1 = [1, 14, 5, 7]
print("Output:", end=" ")
sum_of_non_primes(arr1)

arr2 = [2, 10, 13, 9]
print("Output:", end=" ")
sum_of_non_primes(arr2)
