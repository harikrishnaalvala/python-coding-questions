def is_perfect_square(x):
    sqrt_x = int(x ** 0.5)
    return sqrt_x * sqrt_x == x

def is_fibonacci(num):
    return is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4)

def sum_of_last_fibonacci_numbers(num):
    fib_numbers = [0, 1]
    while fib_numbers[-1] <= num:
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
    return sum(fib_numbers[:-1])

def check_fibonacci_or_sum(num):
    if is_fibonacci(num):
        print(num, "is a Fibonacci number")
    else:
        print(num, "is not a Fibonacci number")
        sum_last_fibonacci = sum_of_last_fibonacci_numbers(num)
        print("Sum of last Fibonacci numbers:", sum_last_fibonacci)

# Test the function with an example
num = 8
check_fibonacci_or_sum(num)
