def is_perfect_square(x):
    s = int(x**0.5)
    return s*s == x

def is_fibonacci(n):
    # A number is in the Fibonacci series if and only if one of (5*n*n + 4) or (5*n*n - 4) is a perfect square
    return is_perfect_square(5*n*n + 4) or is_perfect_square(5*n*n - 4)

# Test the function with the example
input_num = 8
if is_fibonacci(input_num):
    print("Yes, the given number is in the Fibonacci series")
else:
    print("No, the given number is not in the Fibonacci series")
