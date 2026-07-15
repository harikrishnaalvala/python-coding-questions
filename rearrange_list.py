def rearrange_list(input_list):
    non_dash_list = []
    dash_list = []

    # Separate non-dash elements and dash elements
    for item in input_list:
        if item != '-':
            non_dash_list.append(item)
        else:
            dash_list.append(item)

    # Concatenate non-dash list with dash list
    output_list = non_dash_list + dash_list

    return output_list

# Example usage
input_list = ['a', 'b', '-', 'c', '-', '-', 'd', '-']
print(rearrange_list(input_list))  # Output: ['a', 'b', 'c', 'd', '-', '-', '-', '-']
