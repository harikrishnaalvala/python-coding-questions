def replace_alternate_words(input_str):
    # Initialize an empty string to store the modified string
    modified_str = ""

    # Initialize a flag to keep track of whether to replace the word or not
    replace_flag = True

    # Split the input string into words based on the dot delimiter
    words = []
    word = ""
    for char in input_str:
        if char == ".":
            words.append(word)
            word = ""
        else:
            word += char
    words.append(word)  # Add the last word

    # Iterate through the words and replace alternate words with "abc"
    for i in range(len(words)):
        if replace_flag:
            modified_str += words[i] + "."
        else:
            modified_str += "abc."
        replace_flag = not replace_flag

    # Remove the last dot from the modified string
    modified_str = modified_str[:-1]

    return modified_str

# Test the function with the example
input_str = "i.like.this.program.very.much"
output = replace_alternate_words(input_str)
print("Output:", output) #Output: “i.abc.this.abc.very.abc”
