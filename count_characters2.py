def count_characters(s):
    length = len(s)

    for i in range(length):
        # Check if this is the first occurrence of the character
        if s.index(s[i]) == i:
            count = 0
            for j in range(length):
                if s[i] == s[j]:
                    count += 1
            print(f"'{s[i]}': {count}")

# Example usage
count_characters("hello world")
