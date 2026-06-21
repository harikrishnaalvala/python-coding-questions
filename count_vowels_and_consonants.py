def count_vowels_and_consonants(s):
    vowels = set("aeiouAEIOU")
    consonant_count = {}
    vowel_count = 0

    for char in s:
        if char.isalpha():  # Check if the character is a letter
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count[char] = consonant_count.get(char, 0) + 1

    return consonant_count, vowel_count

# Test the function with the example
input_str = "rajar"
consonant_counts, vowel_count = count_vowels_and_consonants(input_str)

# Formatted output
output = ", ".join(f"{char}={count}" for char, count in consonant_counts.items()) + f", vowel={vowel_count}"
print("Output:", output) # r=2 j=1 vowel=2
