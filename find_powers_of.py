def is_power_of(base, num):
    if num <= 0:
        return False
    while num % base == 0:
        num /= base
    return num == 1

def find_powers_of(base, nums):
    powers = []
    for num in nums:
        if is_power_of(base, num):
            powers.append(num)
    return powers

# Test the function with the example
input_nums = [3, 5, 27, 15]
base = 3
output = find_powers_of(base, input_nums)
print("Output:", output) # Output: [3,27]
