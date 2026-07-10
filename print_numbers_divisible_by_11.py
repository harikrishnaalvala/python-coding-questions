def print_numbers_divisible_by_11(start, end):
    
    for num in range(start, end + 1):
        if num % 11 == 0:
            print(num,end=" ")

# Test case
start_num = 1
end_num = 100
print_numbers_divisible_by_11(start_num, end_num) # 11 22 33 44 55 66 77 88 99 
