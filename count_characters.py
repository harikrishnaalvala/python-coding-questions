from collections import Counter

def count_characters(s):
    # Count the characters in the string
    character_count = Counter(s)

    # Display the count of each character
    for char, count in character_count.items():
        print(f"'{char}': {count}")

# Example usage
count_characters("hello world")
