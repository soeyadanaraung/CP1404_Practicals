"""
Word Occurrences
"""

word_to_count = {}

text = input("Text: ")
words = text.split()
words.sort()

for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1

for word, count in word_to_count.items():