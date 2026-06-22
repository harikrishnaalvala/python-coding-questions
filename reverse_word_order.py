def reverse_word_order(input_str):
    words = []
    current_word = ''

    for char in input_str:
        if char == '.':
            words.append(current_word)
            current_word = ''
        else:
            current_word += char

    # Add the last word if the string does not end with a dot
    if current_word:
        words.append(current_word)

    # Manually reverse the words list
    reversed_words = reverse_list(words)

    # Build the reversed string
    reversed_str = ''
    for word in reversed_words:
        if reversed_str:  # Add a dot before every word except the first one
            reversed_str += '.'
        reversed_str += word

    return reversed_str

def reverse_list(lst):
    reversed_lst = []
    for item in lst:
        reversed_lst = [item] + reversed_lst
    return reversed_lst

# Test the function with the example
input_str = "iam.ccpb.trainee"
output = reverse_word_order(input_str)
print("Output:", output) # trainee.ccpb.iam
