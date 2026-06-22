def reverse_alternate_words(input_str):
    result = []
    current_word = ''
    word_index = 0  # To keep track of the position of the word

    for char in input_str:
        if char == '.':
            if word_index % 2 == 1:  # Check if the word position is odd (second, fourth, etc.)
                current_word = reverse_string(current_word)  # Reverse the word
            result.append(current_word)
            current_word = ''
            word_index += 1  # Move to the next word
        else:
            current_word += char

    # Handle the last word if there's no dot at the end
    if current_word:
        if word_index % 2 == 1:
            current_word = reverse_string(current_word)
        result.append(current_word)

    return '.'.join(result)

def reverse_string(s):
    reversed_str = ''
    for char in s:
        reversed_str = char + reversed_str  # Prepend character to build the reversed string
    return reversed_str

# Test the function with the example
input_str = "i.like.this.programme.very.much"
output = reverse_alternate_words(input_str)
print("Output:", output)
