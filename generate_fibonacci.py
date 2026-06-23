def generate_fibonacci(n):
    if n <= 0:
        return []

    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)

    return fib_sequence

# Test the function with the example
input_num = 8
output = generate_fibonacci(input_num)
print("Fibonacci numbers:", ', '.join(map(str, output))) #  0,1,1,2,3,5,8,13
