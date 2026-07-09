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

def closest_primes(num):
    if is_prime(num):
        print(num)
        return

    smaller_prime = None
    greater_prime = None

    # Find the closest smaller prime
    smaller = num - 1
    while smaller > 1:
        if is_prime(smaller):
            smaller_prime = smaller
            break
        smaller -= 1

    # Find the closest greater prime
    greater = num + 1
    while True:
        if is_prime(greater):
            greater_prime = greater
            break
        greater += 1

    # Print the results
    if smaller_prime and greater_prime:
        print(smaller_prime, greater_prime)
    elif smaller_prime:
        print(smaller_prime)
    elif greater_prime:
        print(greater_prime)

# Test cases
num1 = 32
print("Input#1:", num1)
print("Output#1:", end=" ")
closest_primes(num1)

num2 = 30
print("\\nInput#2:", num2)
print("Output#2:", end=" ")
closest_primes(num2)
