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

def closest_prime(n):
    smaller_prime = None
    larger_prime = None

    # Check smaller primes
    for i in range(n - 1, 1, -1):
        if is_prime(i):
            smaller_prime = i
            break

    # Check larger primes
    i = n + 1
    while True:
        if is_prime(i):
            larger_prime = i
            break
        i += 1

    # Print the closest prime(s)
    if smaller_prime is None:
        print(larger_prime)
    elif larger_prime is None:
        print(smaller_prime)
    else:
        print(f"{smaller_prime},{larger_prime}")

# Test the function with examples
input_num = 4
closest_prime(input_num) #3
