from collections import Counter

def count_characters(s):
    # Count the characters in the string
    character_count = Counter(s)

    # Display the count of each character
    return character_count.items()

# Example usage
a=count_characters("hello world")
print(dict(a)) # {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
