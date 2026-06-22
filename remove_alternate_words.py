def remove_alternate_words(input_str):
    result = []
    current_word = ''
    keep_word = True  # Start with keeping the first word

    for char in input_str:
        if char == '.':
            if keep_word:
                result.append(current_word)
            current_word = ''
            keep_word = not keep_word  # Toggle the flag to keep or skip the next word
        else:
            current_word += char

    # Add the last word if needed (and if it's not empty)
    if keep_word and current_word:
        result.append(current_word)

    return '.'.join(result)

# Test the function with the example
input_str = "i.like.this.programme.very.much"
output = remove_alternate_words(input_str)
print("Output:", output) #  i.this.very
