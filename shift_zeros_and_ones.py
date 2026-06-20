def shift_zeros_and_ones(input_str):
    # Count the number of 0's and 1's
    count_0 = input_str.count('0')
    count_1 = input_str.count('1')

    # Construct the output string
    output_str = '0' * count_0 + '1' * count_1
    return output_str

# Test the function with the example
input_str = "010101101001011"
output = shift_zeros_and_ones(input_str)
print("Output:", output) #000000011111111
