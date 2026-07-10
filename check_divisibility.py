def check_divisibility(number):
    # Check if the number is divisible by both 7 and 11
    if number % 7 == 0 and number % 11 == 0:
        print("Cool Dude")
    else:
        print("The number is not divisible by both 7 and 11")

# Example usage
check_divisibility(77)  # 77 is divisible by both 7 and 11
check_divisibility(14)  # 14 is not divisible by 11
