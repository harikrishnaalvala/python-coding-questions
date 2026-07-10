def print_numbers_divisible_by_11(start, end):
    print("Numbers divisible by 11:")
    for num in range(start, end + 1):
        if num % 11 == 0:
            print(num)

# Test case
start_num = 1
end_num = 100
print_numbers_divisible_by_11(start_num, end_num)
