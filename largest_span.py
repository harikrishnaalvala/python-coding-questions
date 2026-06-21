def largest_span(lst):
    first_occurrence = {}  # Dictionary to store the first occurrence of elements
    max_span = 0  # Variable to track the maximum span

    for index, element in enumerate(lst):
        if element in first_occurrence:
            # Calculate span for this occurrence
            span = index - first_occurrence[element]
            max_span = max(max_span, span)
        else:
            # Record the first occurrence of this element
            first_occurrence[element] = index

    return max_span

# Test the function with the example
input_list = [1, 9, 6, 3, 1, 5, 4, 9, 2, 5, 1]
print("Largest span:", largest_span(input_list))
