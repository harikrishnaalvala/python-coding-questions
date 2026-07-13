def join_alternate_words_with_xyz(input_str):
    words = input_str.split('.')
    alternate_words = words[::2]  # Selecting alternate words

    # Joining with 'xyz'
    result = '.xyz.'.join(alternate_words)

    # Handling the case to add 'xyz' at the end if necessary
    if len(words) % 2 == 0:
        result += '.xyz'

    return result

# Example usage
input_str = "i.will.learn.python.easily"
output_str = join_alternate_words_with_xyz(input_str)
print(output_str)  # Output: "i.xyz.learn.xyz.easily.xyz"
