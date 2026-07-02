# Iterative Approach
def fibonacci_iterative(n):
    fib_series = [0, 1]  # Initialize with the first two Fibonacci numbers

    # Generate Fibonacci series
    for i in range(2, n):
        next_num = fib_series[-1] + fib_series[-2]
        fib_series.append(next_num)

    return fib_series

# Test the iterative approach
n = 10  # Number of Fibonacci numbers to generate
fib_series_iterative = fibonacci_iterative(n)
print("Fibonacci Series (Iterative):", fib_series_iterative) # Fibonacci Series (Iterative): [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


# Recursive Approach
def fibonacci_recursive(n):
    # Base cases
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    # Recursive case
    prev_series = fibonacci_recursive(n - 1)
    next_num = prev_series[-1] + prev_series[-2]
    return prev_series + [next_num]

# Test the recursive approach
fib_series_recursive = fibonacci_recursive(n)
print("Fibonacci Series (Recursive):", fib_series_recursive) # Fibonacci Series (Recursive): [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
