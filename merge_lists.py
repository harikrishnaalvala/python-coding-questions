def merge_lists(list1, list2):
    merged_list = []
    len1, len2 = len(list1), len(list2)

    # Iterating and merging
    for i in range(max(len1, len2)):
        if i < len1:
            merged_list.append(list1[i])
        if i < len2:
            merged_list.append(list2[i])

    return merged_list

# Test the function with the example
input_list1 = [1, 2, 3, 4]
input_list2 = ['a', 'b']
output = merge_lists(input_list1, input_list2)
print("Output:", output) # [1,a,2,b,3,4]
