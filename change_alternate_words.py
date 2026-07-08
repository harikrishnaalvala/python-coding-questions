def change_alternate_words(array, format_word):
    for i in range(len(array)):
        if i % 2 != 0:
            array[i] = format_word
    return array

# Test the function with an example
array = ["apple", "banana", "orange", "grape"]
format_word = "fruit"
modified_array = change_alternate_words(array, format_word)
print("Modified Array:", modified_array)
