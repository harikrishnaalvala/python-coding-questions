def digit_frequency(string):
    digit_count = {str(i): 0 for i in range(10)}  # Dictionary for digit count
    non_digit_count = 0

    # Counting the digits and non-digit characters
    for char in string:
        if char.isdigit():
            digit_count[char] += 1
        else:
            non_digit_count += 1

    # Constructing the output string
    output = ",".join([f'"{digit}"={count}' for digit, count in digit_count.items() if count > 0])
    output += f",others={non_digit_count}"

    return output

# Test the function with the example
input_string = "raja11223labs"
print("Output:", digit_frequency(input_string)) # output=""1""=2,""2""=2,""3""=1,others=8
