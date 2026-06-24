def print_alternatively(list1, list2):
    result = ""
    min_len = min(len(list1), len(list2))

    for i in range(min_len):
        result += str(list1[i]) + str(list2[i])

    # Append remaining elements from longer list, if any
    if len(list1) > len(list2):
        result += ''.join(map(str, list1[min_len:]))
    elif len(list2) > len(list1):
        result += ''.join(map(str, list2[min_len:]))

    return result

# Test the function with the example
input_list1 = [6, 7, 'a', 'h']
input_list2 = ['a', 'b', 'u', 'I', 'k', 'h']
output = print_alternatively(input_list1, input_list2)
print("Output:", output) # 6a7bauhlkh
