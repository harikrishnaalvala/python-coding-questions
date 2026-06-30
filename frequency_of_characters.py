def frequency_of_characters(input_str):
    # Initialize dictionary to store frequencies
    freq_dict = {'b': 0, 'f': 0, 'j': 0, 'p': 0, 'v': 0}

    # Convert input string to lowercase
    input_str = input_str.lower()

    # Iterate through each character in the string
    for char in input_str:
        # Check if the character is one of the target characters
        if char in freq_dict:
            # Increment the frequency count for the character
            freq_dict[char] += 1

    # Calculate the total count of target characters
    total_count = sum(freq_dict.values())

    # Return the dictionary of frequencies along with the total count
    return freq_dict, total_count

# Test the function with examples
input_str1 = "rajasoftwarelabs"
input_str2 = "Buffet"
output1, total_count1 = frequency_of_characters(input_str1)
output2, total_count2 = frequency_of_characters(input_str2)

print("Output 1:", output1, "Total:", total_count1)
print("Output 2:", output2, "Total:", total_count2)
