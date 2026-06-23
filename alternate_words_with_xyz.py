def alternate_words_with_xyz(input_str):
    current_word = ''
    alternate_words = []
    word_index = 0  # To keep track of the position of the word

    for char in input_str:
        if char == '.':
            if word_index % 2 == 0:  # Check if the word position is even (first, third, etc.)
                alternate_words.append(current_word)
            current_word = ''
            word_index += 1
        else:
            current_word += char

    # Handle the last word if there's no dot at the end
    if word_index % 2 == 0 and current_word:
        alternate_words.append(current_word)

    # Join the alternate words with 'xyz'
    return 'xyz'.join(alternate_words)

# Test the function with the example
input_str = "i.will.learn.python.easily"
output = alternate_words_with_xyz(input_str)
print("Output:", output) # i.xyz.learn.xyz.easily.xyz
