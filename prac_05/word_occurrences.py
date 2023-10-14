"""
Word Occurrences
Estimate: 40 minutes
Actual:  120  minutes
"""
user_sentence = input("Enter a sentence: ")  # string
words = user_sentence.split(" ")  # split a string into a list of substrings
word_to_count = {}  # An empty dictionary to store word counts
for word in words:  # iterate each word in words list
    if word in word_to_count:  # if the word is in the dictionary
        word_to_count[word] += 1  # add one to count
    else:
        word_to_count[
            word] = 1  # first time see the word, add the word as a key in the dictionary, set its count to one

words = list(word_to_count.keys())

max_length = max(len(word) for word in words)
for word in sorted(words):
    print(f"{word:{max_length}} : {word_to_count[word]}")
