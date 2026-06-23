def is_perfect_square(x):
    s = int(x**0.5)
    return s*s == x

def is_fibonacci(n):
    # A number is a Fibonacci number if and only if one of (5*n*n + 4) or (5*n*n - 4) is a perfect square
    return is_perfect_square(5*n*n + 4) or is_perfect_square(5*n*n - 4)

def sum_even_fibonacci(n):
    if n <= 0:
        return 0
    a, b = 0, 1
    sum_even = 0

    while a <= n:
        if a % 2 == 0:
            sum_even += a
        a, b = b, a + b

    return sum_even

def fibonacci_or_sum(n):
    if is_fibonacci(n):
        return n
    else:
        return sum_even_fibonacci(n)

# Test the function with the example
input_num = 8
output = fibonacci_or_sum(input_num)
print("Output:", output # 8
