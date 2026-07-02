def reverse_alternate_wordss(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Iterate through the words and reverse alternate words
    for i in range(len(words)):
        if i % 2 != 0:  # Alternate words (index is odd)
            words[i] = words[i][::-1]  # Reverse the word

    # Join the words back into a sentence
    modified_sentence = ' '.join(words)

    return modified_sentence

# Test the function with an example
sentence = "This is a test sentence to reverse alternate words"
modified_sentence = reverse_alternate_words(sentence)
print("Modified Sentence:", modified_sentence)
