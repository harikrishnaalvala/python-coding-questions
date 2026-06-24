def count_non_vowel_characters(word):
    word = word.lower()
    non_vowel_counts = {}

    for char in word:
        if char.isalpha() and char not in 'aeiou':
            non_vowel_counts[char] = non_vowel_counts.get(char, 0) + 1

    return non_vowel_counts

# Test the function with the example
input_word = "Hello"
output = count_non_vowel_characters(input_word)
print("Output:", ','.join([f"{char}={count}" for char, count in output.items()])) # Output:H=1,l=2
