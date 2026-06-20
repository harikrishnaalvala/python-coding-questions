def find_longest_chain_of_ones(input_list):
    max_chain = 0
    current_chain = 0

    for num in input_list:
        if num == 1:
            current_chain += 1
            max_chain = max(max_chain, current_chain)
        else:
            current_chain = 0

    return max_chain

# Test the function with the example
input_list = [0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0]
longest_chain = find_longest_chain_of_ones(input_list)
print("Longest chain of 1's:", longest_chain) # Longest chain of 1's: 3
