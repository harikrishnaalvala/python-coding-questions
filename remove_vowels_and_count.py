def remove_vowels_and_count(s):
    vowels = set("aeiouAEIOU")
    no_vowels = []
    vowel_count = 0
    consonant_count = 0

    for char in s:
        if char in vowels:
            vowel_count += 1
        elif char.isalpha():  # Check if the character is a letter
            no_vowels.append(char)
            consonant_count += 1

    return "".join(no_vowels), vowel_count, consonant_count

# Test the function with an example
input_str = "Hello World"
no_vowels_str, vowel_count, consonant_count = remove_vowels_and_count(input_str)

print("String without vowels:", no_vowels_str)
print("Vowel count:", vowel_count)
print("Consonant count:", consonant_count)
